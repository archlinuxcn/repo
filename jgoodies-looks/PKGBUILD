# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: David Hajek <dante4d at gmail dot com>
# Contributor: Geoffroy Carrier <geoffroy dot carrier at koon dot fr>
# Contributor: Otto Allmendinger <otto.allmendinger@gmail.com>

pkgname=jgoodies-looks
pkgver=2.8.0
pkgrel=3
pkgdesc="A Java Swing look and feel library"
arch=('any')
url="http://www.jgoodies.com/"
license=('BSD')
groups=('jgoodies')
depends=('java-runtime')
#source=("http://www.jgoodies.com/download/libraries/looks/jgoodies-looks-${pkgver//./_}-20150402.zip")
source=("jgoodies-looks-2_8_0-20150402.zip::https://www.dropbox.com/s/88cjnlxecs9qsf1/jgoodies-looks-2_8_0-20150402.zip?dl=1")
md5sums=('89a28c43d742142869077e3ebeb109c9')

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -Dm644 "LICENSE.txt" \
    "${pkgdir}/usr/share/licenses/${pkgname}/license.txt"
  install -Dm644 "${pkgname}-${pkgver}.jar" \
    "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}

# vim:set ts=2 sw=2 et:
