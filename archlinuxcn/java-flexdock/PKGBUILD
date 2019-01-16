# Maintainer: Victor Dmitriyev <mrvviter@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Sergej Pupykin <pupykin.s+arch at gmail dot com>
# Contributor: Simon Lipp <sloonz+aur at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>

pkgname=java-flexdock
pkgver=1.2.4
pkgrel=1
pkgdesc="Docking framework for Swing"
arch=('any')
url="http://forge.scilab.org/index.php/p/flexdock/"
license=('MIT')
depends=('java-runtime')
privides=('flexdock')
conflicts=('flexdock')
source=("license.txt"
  "http://forge.scilab.org/index.php/p/flexdock/downloads/get/flexdock-${pkgver}.jar")
md5sums=('ed8e56d9c9e4a4a32251592d0f778866'
'a6790943645aa7204ca12c190cb6e08b')
noextract=("flexdock-${pkgver}.jar")

package() {
  cd "${srcdir}"
  install -Dm644 "flexdock-${pkgver}.jar" \
    "${pkgdir}/usr/share/java/flexdock/flexdock.jar"
  install -Dm644 "license.txt" "${pkgdir}/usr/share/licenses/${pkgname}/license.txt"
}
# vim:set ts=2 sw=2 et:
