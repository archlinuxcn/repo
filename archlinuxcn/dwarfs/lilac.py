#!/usr/bin/env python3
from lilaclib import *

patchfile = """From 8afc7f032bf3afa601edd315c736ace1a87f0db4 Mon Sep 17 00:00:00 2001
From: Marcus Holland-Moritz <github@mhxnet.de>
Date: Mon, 2 Nov 2026 16:16:52 +0100
Subject: [PATCH] fix(filesystem_extractor): FATAL archives must not be closed
 since 3.8.10

---
 src/utility/filesystem_extractor.cpp | 128 +++++++++++++++++++++------
 1 file changed, 103 insertions(+), 25 deletions(-)

diff --git a/src/utility/filesystem_extractor.cpp b/src/utility/filesystem_extractor.cpp
index 6829704a1..699678f91 100644
--- a/src/utility/filesystem_extractor.cpp
+++ b/src/utility/filesystem_extractor.cpp
@@ -28,8 +28,10 @@
 
 #include <array>
 #include <condition_variable>
+#include <exception>
 #include <memory>
 #include <mutex>
+#include <string_view>
 #include <thread>
 #include <unordered_set>
 
@@ -62,6 +64,7 @@
 #include <dwarfs/utility/filesystem_extractor_archive_format.h>
 #include <dwarfs/vfs_stat.h>
 
+#include <dwarfs/internal/synchronized.h>
 #include <dwarfs/internal/thread_util.h>
 #include <dwarfs/internal/worker_group.h>
 
@@ -244,32 +247,77 @@ class filesystem_extractor_ final : public filesystem_extractor::impl {
   }
 
   void close() override {
-    if (!a_reg_.empty()) {
-      for (auto& ar : a_reg_) {
-        LOG_DEBUG << "closing regular file disk archive";
-        check_result(ar, ::archive_write_close(ar.get()));
+    // Defer errors until all resources have been released.
+    std::exception_ptr first_error;
+
+    auto save_error = [&] {
+      if (!first_error) {
+        first_error = std::current_exception();
+      }
+    };
+
+    auto close_archive = [&](archive_ptr& ar) {
+      if (!ar) {
+        return;
       }
-      LOG_TRACE << "freeing regular file disk archives";
-      a_reg_.clear();
+
+      auto* a = ar.get();
+      bool const fatal = fatal_archives_.lock()->erase(a) != 0;
+
+      if (fatal) {
+        // Since libarchive 3.8.10, archive_write_close() rejects archives
+        // in ARCHIVE_STATE_FATAL.
+        LOG_DEBUG << "skipping close of failed libarchive writer";
+      } else {
+        try {
+          check_result(ar, ::archive_write_close(a), "archive_write_close");
+        } catch (...) {
+          save_error();
+        }
+
+        // check_result() may have recorded a new ARCHIVE_FATAL above.
+        fatal_archives_.lock()->erase(a);
+      }
+
+      ar.reset();
+    };
+
+    for (auto& ar : a_reg_) {
+      LOG_DEBUG << "closing regular file disk archive";
+      close_archive(ar);
     }
 
+    LOG_TRACE << "freeing regular file disk archives";
+    a_reg_.clear();
+
     if (a_) {
       LOG_DEBUG << "closing archive";
-      check_result(a_, ::archive_write_close(a_.get()));
-      LOG_TRACE << "freeing archive";
-      a_.reset();
+      close_archive(a_);
     }
 
-    if (iot_) {
-      LOG_TRACE << "closing pipe[1]";
-      closefd(pipefd_[1]);
+    auto close_pipe = [&](int& fd) {
+      try {
+        closefd(fd);
+      } catch (...) {
+        save_error();
+      }
+    };
+
+    // The pipe's write end must be closed to let pump() observe EOF.
+    LOG_TRACE << "closing pipe[1]";
+    close_pipe(pipefd_[1]);
 
+    if (iot_) {
       LOG_TRACE << "joining I/O thread";
       iot_->join();
       iot_.reset();
+    }
+
+    LOG_TRACE << "closing pipe[0]";
+    close_pipe(pipefd_[0]);
 
-      LOG_TRACE << "closing pipe[0]";
-      closefd(pipefd_[0]);
+    if (first_error) {
+      std::rethrow_exception(first_error);
     }
   }
 
@@ -382,24 +430,49 @@ class filesystem_extractor_ final : public filesystem_extractor::impl {
     }
   }
 
-  void check_result(struct archive* a, int res) {
+  void check_result(struct archive* a, int res,
+                    std::optional<std::string_view> operation = std::nullopt,
+                    ::archive_entry* entry = nullptr) {
+    if (res == ARCHIVE_OK || res == ARCHIVE_EOF) {
+      return;
+    }
+    auto const* error = ::archive_error_string(a);
+    auto const* message = error ? error : "unknown libarchive error";
     switch (res) {
     case ARCHIVE_OK:
     case ARCHIVE_EOF:
     default:
       break;
     case ARCHIVE_WARN:
-      LOG_WARN << std::string(::archive_error_string(a));
+      LOG_WARN << message;
       break;
+    case ARCHIVE_FATAL: {
+      // Remember which writers must not be closed. Also, explicitly call
+      // archive_write_fail() to ensure that the archive is marked as failed.
+      ::archive_write_fail(a);
+      fatal_archives_.lock()->insert(a);
+      [[fallthrough]];
+    }
     case ARCHIVE_RETRY:
     case ARCHIVE_FAILED:
-    case ARCHIVE_FATAL:
-      throw archive_error(std::string(::archive_error_string(a)));
+      if (operation.has_value()) {
+        auto const* format = ::archive_format_name(a);
+        auto const* entry_path =
+            entry ? ::archive_entry_pathname(entry) : nullptr;
+        LOG_ERROR << fmt::format(
+            "libarchive {}{} returned {} (format {}, errno {}): {}",
+            operation.value(),
+            entry_path ? fmt::format(" [{}]", entry_path) : "", res,
+            format ? format : "unknown", ::archive_errno(a), message);
+      }
+      throw archive_error(message);
     }
   }
 
-  void check_result(archive_ptr const& a, int res) {
-    check_result(a.get(), res);
+  void check_result(archive_ptr const& a, int res,
+                    std::optional<std::string_view> operation = std::nullopt,
+                    ::archive_entry* entry = nullptr) {
+    check_result(a.get(), res, operation, entry);
   }
 
   LOG_PROXY_DECL(debug_logger_policy);
@@ -410,6 +483,7 @@ class filesystem_extractor_ final : public filesystem_extractor::impl {
   std::unique_ptr<output_stream> out_;
   std::array<int, 2> pipefd_{-1, -1};
   std::unique_ptr<std::thread> iot_;
+  synchronized<std::unordered_set<::archive*>> fatal_archives_;
   sparse_file_mode sparse_mode_{sparse_file_mode::auto_detect};
   std::atomic<uint64_t> bytes_written_{0};
   std::mutex mutable bytes_total_mx_;
@@ -533,7 +607,8 @@ bool filesystem_extractor_<LoggerPolicy>::extract(
                 }
               }
 
-              check_result(a, ::archive_write_header(a, ae.get()));
+              check_result(a, ::archive_write_header(a, ae.get()),
+                           "archive_write_header", ae.get());
 
               if (sparse_mode == sparse_file_mode::sparse_disk) {
                 extents.erase(std::remove_if(extents.begin(), extents.end(),
@@ -556,7 +631,7 @@ bool filesystem_extractor_<LoggerPolicy>::extract(
                 auto const rv = write_range_data(sparse_mode, a, r.data(),
                                                  r.size(), ext.range.offset());
 
-                check_result(a, rv);
+                check_result(a, rv, "archive_write_data", ae.get());
 
                 if (std::cmp_not_equal(rv, static_cast<la_ssize_t>(r.size()))) {
                   throw archive_error(
@@ -580,7 +655,8 @@ bool filesystem_extractor_<LoggerPolicy>::extract(
 
               assert(extents.empty());
 
-              check_result(a, ::archive_write_finish_entry(a));
+              check_result(a, ::archive_write_finish_entry(a),
+                           "archive_write_finish_entry", ae.get());
             } catch (archive_error const& e) {
               LOG_ERROR << exception_str(e);
               ++hard_error;
@@ -597,8 +673,10 @@ bool filesystem_extractor_<LoggerPolicy>::extract(
     } else {
       aptr->add_job([this, ae = std::move(ae), &hard_error](struct archive* a) {
         try {
-          check_result(a, ::archive_write_header(a, ae.get()));
-          check_result(a, ::archive_write_finish_entry(a));
+          check_result(a, ::archive_write_header(a, ae.get()),
+                       "archive_write_header", ae.get());
+          check_result(a, ::archive_write_finish_entry(a),
+                       "archive_write_finish_entry", ae.get());
         } catch (...) {
           LOG_ERROR << exception_str(std::current_exception());
           ++hard_error;
"""

def pre_build():
    aur_pre_build(maintainers=['KokaKiwi'])
    pkgver, _ = get_pkgver_and_pkgrel()
    pkgver: str
    need_patch = pkgver == '0.15.8'
    if need_patch:
        with open('0001-fix-filesystem_extractor.patch', 'w') as f:
            f.write(patchfile)
    for line in edit_file('PKGBUILD'):
        line: str
        if '--exclude-regex' in line and line.endswith("'"):
            print(line[:-1] + "|mkdwarfs_log_mem_usage_test\\.log_memory_usage'")
        elif need_patch:
            if line.startswith('source'):
                print(line[:-1] + ' 0001-fix-filesystem_extractor.patch)')
            elif line.startswith('sha256sum'):
                print(line[:-1] + " 'da8fd28f3ddc853b4ddfe0ecb1b121856318b7458c61c5a985dba7e94e2f498c')")
            elif line.startswith('b2sum'):
                print(line[:-1] + " '253c98d982d48034c3ba547c32c1327b83461ad9999be2a0815a87751af50e36dd37def4606750b88461efca45f49f3b6ec6f54232e3a977acd218ec34334b01')")
            elif line.startswith('build()'):
                print("""
    prepare() {
      cd "$pkgname-$pkgver"
      # Upstream fix for incompatibility with latest libarchive
      patch -p1 -l -F3 < ../0001-fix-filesystem_extractor.patch
    }""")
                print(line)
            else:
                print(line)
        else:
            print(line)
