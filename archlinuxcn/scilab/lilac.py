from lilaclib import *

libxml_extern_C_patch = b"""
diff --git a/modules/functions_manager/src/cpp/dynamic_modules.cpp b/modules/functions_manager/src/cpp/dynamic_modules.cpp
index 4c2859b..ca44abc 100644
--- a/modules/functions_manager/src/cpp/dynamic_modules.cpp
+++ b/modules/functions_manager/src/cpp/dynamic_modules.cpp
@@ -22,13 +22,13 @@ extern "C"
 {
 #include "loadOnUseClassPath.h"
 #include "Scierror.h"
+}
 
     //XML API
 #include <libxml/xpath.h>
 #include <libxml/xmlreader.h>
 #include "sci_malloc.h"
 #include "configvariable_interface.h"
-}
 
 vectGateway loadGatewaysName(const std::wstring& _wstModuleName)
 {
diff --git a/modules/io/src/cpp/loadlib.cpp b/modules/io/src/cpp/loadlib.cpp
index 25ca60b..2887bf6 100644
--- a/modules/io/src/cpp/loadlib.cpp
+++ b/modules/io/src/cpp/loadlib.cpp
@@ -26,9 +26,9 @@ extern "C"
 #include "fullpath.h"
 #include "PATH_MAX.h"
 #include "pathconvert.h"
+}
 #include <libxml/xpath.h>
 #include <libxml/xmlreader.h>
-}
 
 #define DEFAULT_ENCODING "UTF-8"
 
diff --git a/modules/xml/src/cpp/XMLDocument.hxx b/modules/xml/src/cpp/XMLDocument.hxx
index 51f5208..7df26d3 100644
--- a/modules/xml/src/cpp/XMLDocument.hxx
+++ b/modules/xml/src/cpp/XMLDocument.hxx
@@ -23,13 +23,10 @@
 
 #include "dynlib_xml_scilab.h"
 
-extern "C"
-{
 #include "xml.h"
 #ifndef XML_XPATH_CHECKNS
 #define XML_XPATH_CHECKNS
 #endif
-}
 
 #include "XMLObject.hxx"
 
diff --git a/modules/scicos/includes/XMIResource.hxx b/modules/scicos/includes/XMIResource.hxx
index 5c115b9..00891b7 100644
--- a/modules/scicos/includes/XMIResource.hxx
+++ b/modules/scicos/includes/XMIResource.hxx
@@ -22,10 +22,8 @@
 #include <string>
 #include <vector>
 
-extern "C" {
 #include <libxml/xmlwriter.h>
 #include <libxml/xmlreader.h>
-}
 
 namespace org_scilab_modules_scicos
 {

"""

pkgbuild_patch=b"""
diff --git a/tmp/scilab/PKGBUILD b/PKGBUILD
index 73359f527e..2473c0da55 100644
--- a/tmp/scilab/PKGBUILD
+++ b/PKGBUILD
@@ -4,7 +4,7 @@
 
 pkgname=scilab
 pkgver=6.0.2
-pkgrel=1
+pkgrel=2.1
 pkgdesc='A scientific software package for numerical computations.'
 arch=('i686' 'x86_64')
 url='https://www.scilab.org'
@@ -20,7 +20,7 @@ depends=('suitesparse>=4.4.1' 'arpack' 'fftw' 'eigen'
          'java-skinlf' 'java-testng' 'xalan-java' 'docbook-xsl'
          'jogl>=2.3.2' 'apache-lucene>=7'
          'java-batik>=1.8' 'java-xmlgraphics-commons>=2.0.1')
-makedepends=('java-environment=8' 'ant>=1.9.0'
+makedepends=('jdk8-openjdk' 'ant>=1.9.0'
              'ocaml-findlib' 'ocaml-num' 'gcc-fortran'
              'time')
 source=("${url}/download/${pkgver}/${pkgname}-${pkgver}-src.tar.gz"
@@ -29,6 +29,7 @@ source=("${url}/download/${pkgver}/${pkgname}-${pkgver}-src.tar.gz"
         "${pkgname}-strict-jar.patch"
         "${pkgname}-LD_LIBRARY_PATH.patch"
         "${pkgname}-0004-Fix-build-with-ocaml-4.0.4.patch"
+	"libxml_extern_C.patch"
         "${pkgname}-num.patch")
 sha256sums=('880f4b614143e9f43c41416304874875df6ebc1a1b0e4400e69384851f6216b0'
             'f19f173e989f72bd55bda35e271b3c180ecef4e29da964df3f230fce8b1330fc'
@@ -36,6 +37,7 @@ sha256sums=('880f4b614143e9f43c41416304874875df6ebc1a1b0e4400e69384851f6216b0'
             '38aa094951338fa1d267dc6f397552e175213b0f8ba7b35727c178607861f6dd'
             'a39277cb8cfc3d7929c73ce6d707dc24e3df4b8d8f2d587f075efebda79ff4db'
             '6712c6db2f3ba365d150e1feb1c71bf691f8aa3b45d5a872b05a42f0daf23392'
+            'a424c453041c5f7e225763e1be2149a30f3d6b8c0718a6c112d6555db3a8cbaa'
             '31e757bdb2086e08e2477118fceddcdd50f3c2fcad5c86cf5de8ec06009f34ed')
 
 prepare(){
@@ -53,12 +55,14 @@ prepare(){
   # OCaml
   patch -p0 < "${srcdir}"/${pkgname}-0004-Fix-build-with-ocaml-4.0.4.patch
   patch -p0 < "${srcdir}"/${pkgname}-num.patch
+  # fix builds
+  patch -p1 < "${srcdir}"/libxml_extern_C.patch
 }
 
 build() {
   cd "${srcdir}/${pkgname}-${pkgver}"
 
-  ./configure \
+  ./configure --with-jdk=/usr/lib/jvm/java-8-openjdk/ \
     --prefix=/usr \
     --with-gcc \
     --with-gfortran \
"""

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build()
    with open('libxml_extern_C.patch', 'wb') as f:
        f.write(libxml_extern_C_patch)
    apply_patch('PKGBUILD', pkgbuild_patch)
    run_cmd(['updpkgsums'])

def post_build():
    aur_post_build()
    with open('libxml_extern_C.patch', 'wb') as f:
        f.write(libxml_extern_C_patch)
    run_cmd(['updpkgsums'])
    git_add(['PKGBUILD', 'libxml_extern_C.patch'])

if __name__ == '__main__':
   single_main()
