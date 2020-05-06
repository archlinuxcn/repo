# Maintainer: Michael Lass <bevan@bi-co.net>
# Contributor: Sebastian Wolf < sebastian at melonkru dot de >
# Contributor: gost < gostrc at gmail dot com >
# Contributor: Mikolaj Pastuszko <deluminathor@gmail.com>
# Contributor: Stefan Seemayer < mail at semicolonsoftware dot de >
# Contributor: Gordin < 9ordin @t gmail dot com >
# Contributor: David Davis < davisd<a@t>davisd.com >

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=yed
pkgver=3.20
pkgrel=1
epoch=1
pkgdesc='Very powerful graph editor written in java'
arch=('any')
url='http://www.yworks.com/en/products_yed_about.html'
license=('custom')
depends=('java-runtime')
source=("https://www.yworks.com/resources/yed/demo/yEd-${pkgver}.zip"
        'yed.desktop'
        'yed'
        'graphml+xml-mime.xml')
sha256sums=('c362318fa0d3668ce6735b6c22fee5a34cbc2adc74d020e780d38f983643497e'
            '245182a52896bdff3f2c995a066623619d600665630e789910c92d36725a0aca'
            '731b54c6e731704efe9847d78e2df474d59042452ace29d2786d76891295249e'
            'e751b69ed8a25faf46d4e4016ed8f1774abc88679067934a6081348e3d6fc332')

install=yed.install

package() {
  # Install jars
  install -Dm644 ${srcdir}/yed-${pkgver}/yed.jar ${pkgdir}/usr/share/java/yed/yed.jar
  install -dm755 ${pkgdir}/usr/share/java/yed/lib
  install -m644 ${srcdir}/yed-${pkgver}/lib/* ${pkgdir}/usr/share/java/yed/lib/

  # Install license
  install -Dm644 ${srcdir}/yed-${pkgver}/license.html ${pkgdir}/usr/share/licenses/yed/license.html

  # Install icons
  for n in $(ls ${srcdir}/yed-${pkgver}/icons/yed*.png | xargs -n1 basename | sed s/[^0-9]//g); do
      install -Dm644 ${srcdir}/yed-${pkgver}/icons/yed${n}.png ${pkgdir}/usr/share/icons/hicolor/${n}x${n}/apps/yed.png
  done

  # Install mime definition
  install -Dm644 ${srcdir}/graphml+xml-mime.xml ${pkgdir}/usr/share/mime/packages/graphml+xml-mime.xml

  # Install .desktop file
  install -Dm644 ${srcdir}/yed.desktop ${pkgdir}/usr/share/applications/yed.desktop

  # Install run script
  install -Dm755 ${srcdir}/yed ${pkgdir}/usr/bin/yed
}
