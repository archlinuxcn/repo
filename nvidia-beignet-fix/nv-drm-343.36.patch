diff --git a/kernel/nv-drm.c b/kernel/nv-drm.c
index c0b41a0..700c193 100644
--- a/kernel/nv-drm.c
+++ b/kernel/nv-drm.c
@@ -128,6 +128,8 @@ static struct drm_driver nv_drm_driver = {
     .gem_prime_vmap = nv_gem_prime_vmap,
     .gem_prime_vunmap = nv_gem_prime_vunmap,
 
+    .set_busid = drm_pci_set_busid,
+
     .name = "nvidia-drm",
     .desc = "NVIDIA DRM driver",
     .date = "20130102",

