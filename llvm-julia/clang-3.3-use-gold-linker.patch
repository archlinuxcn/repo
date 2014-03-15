diff -upr cfe.src.orig/lib/Driver/ToolChains.cpp cfe.src/lib/Driver/ToolChains.cpp
--- cfe.src.orig/lib/Driver/ToolChains.cpp	2013-06-08 16:17:19.000000000 +0300
+++ cfe.src/lib/Driver/ToolChains.cpp	2013-06-08 16:17:33.000000000 +0300
@@ -2220,7 +2220,7 @@ Linux::Linux(const Driver &D, const llvm
   PPaths.push_back(Twine(GCCInstallation.getParentLibPath() + "/../" +
                          GCCInstallation.getTriple().str() + "/bin").str());
 
-  Linker = GetProgramPath("ld");
+  Linker = GetProgramPath("ld.gold");
 
   Distro Distro = DetectDistro(Arch);
 
