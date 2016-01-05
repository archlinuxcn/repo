Index: pam_unix2-2.9.1/src/read-files.c
===================================================================
--- pam_unix2-2.9.1.orig/src/read-files.c
+++ pam_unix2-2.9.1/src/read-files.c
@@ -30,8 +30,14 @@
 #include <errno.h>
 #include <fcntl.h>
 #include <nss.h>
-#include <bits/libc-lock.h>
+#include <pthread.h>
 #define __libc_lock_t pthread_mutex_t
+#define __libc_lock_define_initialized(CLASS,NAME) \
+  CLASS __libc_lock_t NAME = PTHREAD_MUTEX_INITIALIZER;
+#define __libc_lock_lock(NAME) \
+  pthread_mutex_lock, (&(NAME))
+#define __libc_lock_unlock(NAME) \
+  pthread_mutex_unlock, (&(NAME))
 
 #include "read-files.h"
 
