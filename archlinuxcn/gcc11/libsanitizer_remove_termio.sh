#!/usr/bin/bash

set -e
set -u

# Fri 24 Oct 2025 03:31:47 AM EDT
# Produce patches to remove libsanitizer code for glibc 2.42
# for gcc4.9-gcc11
# gcc4.8 has an early version of libsanitizer with different code
# gcc4.7 has no libsanitizer

c78='From 6afd8bac7f8e7b95984b5a1be4bb5ec71c33f44f Mon Sep 17 00:00:00 2001
Message-ID: <6afd8bac7f8e7b95984b5a1be4bb5ec71c33f44f.1753477523.git.sam@gentoo.org>
From: Florian Weimer <fweimer@redhat.com>
Date: Fri, 2 May 2025 17:41:43 +0200
Subject: [PATCH 1/2] libsanitizer: Fix build with glibc 2.42

The termio structure will be removed from glibc 2.42.  It has
been deprecated since the late 80s/early 90s.

Cherry-picked from LLVM commit 59978b21ad9c65276ee8e14f26759691b8a65763
("[sanitizer_common] Remove interceptors for deprecated struct termio
(#137403)").

Co-Authored-By: Tom Stellard <tstellar@redhat.com>

libsanitizer/

\t* sanitizer_common/sanitizer_common_interceptors_ioctl.inc: Cherry
\tpicked from LLVM commit 59978b21ad9c65276ee8e14f26759691b8a65763.
\t* sanitizer_common/sanitizer_platform_limits_posix.cpp: Likewise.
\t* sanitizer_common/sanitizer_platform_limits_posix.h: Likewise.

(cherry picked from commit 1789c57dc97ea2f9819ef89e28bf17208b6208e7)
---
 .../sanitizer_common_interceptors_ioctl.inc               | 8 --------
 .../sanitizer_common/sanitizer_platform_limits_posix.cpp  | 3 ---
 .../sanitizer_common/sanitizer_platform_limits_posix.h    | 1 -
 3 files changed, 12 deletions(-)
'

c79='From a8bb9c3f8a6ac155250cdcc3edc55ee24561670f Mon Sep 17 00:00:00 2001
Message-ID: <a8bb9c3f8a6ac155250cdcc3edc55ee24561670f.1753477523.git.sam@gentoo.org>
In-Reply-To: <6afd8bac7f8e7b95984b5a1be4bb5ec71c33f44f.1753477523.git.sam@gentoo.org>
References: <6afd8bac7f8e7b95984b5a1be4bb5ec71c33f44f.1753477523.git.sam@gentoo.org>
From: Sam James <sam@gentoo.org>
Date: Fri, 25 Jul 2025 19:45:18 +0100
Subject: [PATCH 2/2] [sanitizer_common] Remove reference to obsolete termio
 ioctls (#138822)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit

Cherry picked from LLVM commit c99b1bcd505064f2e086e6b1034ce0b0c91ea5b9.

The termio ioctls are no longer used after commit 59978b21ad9c
("[sanitizer_common] Remove interceptors for deprecated struct termio
(#137403)"), remove them.  Fixes this build error:

../../../../libsanitizer/sanitizer_common/sanitizer_platform_limits_posix.cpp:765:27: error: invalid application of ‘sizeof’ to incomplete type ‘__sanitizer::termio’
  765 |   unsigned IOCTL_TCGETA = TCGETA;
      |                           ^~~~~~
../../../../libsanitizer/sanitizer_common/sanitizer_platform_limits_posix.cpp:769:27: error: invalid application of ‘sizeof’ to incomplete type ‘__sanitizer::termio’
  769 |   unsigned IOCTL_TCSETA = TCSETA;
      |                           ^~~~~~
../../../../libsanitizer/sanitizer_common/sanitizer_platform_limits_posix.cpp:770:28: error: invalid application of ‘sizeof’ to incomplete type ‘__sanitizer::termio’
  770 |   unsigned IOCTL_TCSETAF = TCSETAF;
      |                            ^~~~~~~
../../../../libsanitizer/sanitizer_common/sanitizer_platform_limits_posix.cpp:771:28: error: invalid application of ‘sizeof’ to incomplete type ‘__sanitizer::termio’
  771 |   unsigned IOCTL_TCSETAW = TCSETAW;
      |                            ^~~~~~~

(cherry picked from commit 50cff2194bcb8321414437169d443bf48695972c)
---
 .../sanitizer_common/sanitizer_platform_limits_posix.cpp      | 4 ----
 .../sanitizer_common/sanitizer_platform_limits_posix.h        | 4 ----
 2 files changed, 8 deletions(-)
'

# "$1" gcc folder
# "$2" sed patch
# "$3" output patch
# "$4" extra message
_fn_patch() {
  rm -rf 'a' 'b'
  pushd "$1/libsanitizer/sanitizer_common"
  rm -f *.orig *.rej
  popd
  ln -sr "$1" 'a'
  cp -pr "$1" 'b'
  pushd 'b/libsanitizer/sanitizer_common'
  local f=(
    'sanitizer_common_interceptors_ioctl.inc'
    sanitizer_platform_limits_posix.*
  )
  set -x
  sed -E -e "$2" -i "${f[@]}"
  set +x
  popd
  printf '%b\nAdapted from gcc12 to %s by Chris Severance aur.severach aATt spamgourmet dott com\n\n' "$4" "$1" > "$3"
  set +e
  diff -pNaru3 'a' 'b' >> "$3"
  set -e
  rm -rf 'a' 'b'
}

p='/\bstruct_termio_sz\b/ d'
_fn_patch "$1" "${p}" 'new-78_all-libsanitizer-Fix-build-with-glibc-2.42.patch' "${c78}"
p='/\bIOCTL_TCGETA\b|\bIOCTL_TCSETA\b|\bIOCTL_TCSETAF\b|\bIOCTL_TCSETAW\b/ d'
_fn_patch "$1" "${p}" 'new-79_all-sanitizer_common-Remove-reference-to-obsolete-termio.patch' "${c79}"
