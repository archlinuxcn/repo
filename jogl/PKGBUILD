# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alexander Rødseth <rodseth@gmail.com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Simon Lipp <sloonz+aur@gmail.com>

pkgname=jogl
pkgver=2.3.2
pkgrel=2
pkgdesc='OpenGL bindings for Java'
arch=('x86_64' 'i686')
url="http://jogamp.org/"
license=('BSD')
depends=('java-runtime' 'libgl')
source=("jogl.LICENSE.txt"
  "gluegen.LICENSE.txt"
	"jogl-all-v${pkgver}.jar::http://jogamp.org/deployment/v${pkgver}/jar/orig/jogl-all.jar"
	"gluegen-rt-v${pkgver}.jar::http://jogamp.org/deployment/v${pkgver}/jar/orig/gluegen-rt.jar")
source_i686=("jogl-all-natives-linux-i586-v${pkgver}.jar::http://jogamp.org/deployment/v${pkgver}/jar/orig/jogl-all-natives-linux-i586.jar"
	"gluegen-rt-natives-linux-i586-v${pkgver}.jar::http://jogamp.org/deployment/v${pkgver}/jar/orig/gluegen-rt-natives-linux-i586.jar")
source_x86_64=("jogl-all-natives-linux-amd64-v${pkgver}.jar::http://jogamp.org/deployment/v${pkgver}/jar/orig/jogl-all-natives-linux-amd64.jar"
	"gluegen-rt-natives-linux-amd64-v${pkgver}.jar::http://jogamp.org/deployment/v${pkgver}/jar/orig/gluegen-rt-natives-linux-amd64.jar")

md5sums=('e77015f08f0c8c3b39b9b7d379d57183'
         '3809542dae46666cb50b9cb7c6d5ac5f'
         'ce831cf96129a663433861a7eda55595'
         '14e746f9328bc33a9b01cf9e16427f4d')
md5sums_x86_64=('0ff2870c4f8da227b05e79b352133c3e'
                '5ea60ff86650e3fc3ed77a417ef2fb95')
md5sums_i686=('79b946d0e6fff33a82a2e0d90133796a'
              'd67501bb4c973ca06140c34e8fb97461')

noextract=("jogl-all-v${pkgver}.jar" "gluegen-rt-v${pkgver}.jar")

package() {
  # *.so files
  install -Ddm755 "${pkgdir}/usr/lib/${pkgname}"
  find "${srcdir}/natives" -type f -print0 | xargs -0 mv -t "${pkgdir}/usr/lib/${pkgname}"

  cd "${srcdir}"
  install -Dm644 "jogl-all-v${pkgver}.jar" "${pkgdir}/usr/share/java/${pkgname}/jogl-all.jar"
  install -Dm644 "gluegen-rt-v${pkgver}.jar" "${pkgdir}/usr/share/java/${pkgname}/gluegen-rt.jar"
  install -Dm644 "jogl.LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/jogl.LICENSE.txt"
  install -Dm644 "gluegen.LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/gluegen.LICENSE.txt"

  cd "${pkgdir}/usr/share/java/${pkgname}"
  ln -s "jogl-all.jar" "jogl2.jar"
  ln -s "gluegen-rt.jar" "gluegen2-rt.jar"

  cd "${pkgdir}/usr/lib"
  ln -s "jogl" "jogl2"
  ln -s "jogl" "gluegen2"
  ln -s "libgluegen-rt.so" "jogl/libgluegen2-rt.so"
}

# vim:set ts=2 sw=2 et:
