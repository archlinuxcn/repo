diff --git a/kernel/common/inc/nv-linux.h b/kernel/common/inc/nv-linux.h
index 10fc418..22ef968 100644
--- a/kernel/common/inc/nv-linux.h
+++ b/kernel/common/inc/nv-linux.h
@@ -175,7 +175,11 @@ static inline uid_t __kuid_val(kuid_t uid)
 
 #if defined(NV_VM_INSERT_PAGE_PRESENT)
 #include <linux/pagemap.h>
+#if LINUX_VERSION_CODE < KERNEL_VERSION(4, 16, 0)
 #include <linux/dma-mapping.h>
+#else
+#include <linux/dma-direct.h>
+#endif
 #endif
 
 #if defined(CONFIG_SWIOTLB) && defined(NVCPU_AARCH64)
diff --git a/kernel/conftest.sh b/kernel/conftest.sh
index b23dbb4..42dc576 100755
--- a/kernel/conftest.sh
+++ b/kernel/conftest.sh
@@ -1906,7 +1906,12 @@ compile_test() {
             # Determine if the phys_to_dma function is present.
             #
             CODE="
+            #include <linux/version.h>
+#if LINUX_VERSION_CODE < KERNEL_VERSION(4, 16, 0)
             #include <linux/dma-mapping.h>
+#else
+            #include <linux/dma-direct.h>
+#endif
             void conftest_phys_to_dma(void) {
                 phys_to_dma();
             }"
