# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgbase=webstorm
pkgname=(webstorm webstorm-jre)
pkgver=2016.3.4
_pkgver=163.13906.20
pkgrel=1
pkgdesc='JavaScript IDE and HTML editor.'
arch=('x86_64' 'i686')
license=('Commercial')
url='https://www.jetbrains.com/webstorm/'
options=('!strip')
makedepends=('rsync')
source=(https://download.jetbrains.com/webstorm/WebStorm-${pkgver}.tar.gz
        jetbrains-webstorm.desktop)
sha512sums=('ae1111746073412578891c1477bade8110436c57904522df6a4bc4d9221cc2d1a14ff0185b0a84236ffc0fac957c6fa480043d805d669a84d8896b636e387142'
            'e261eb9b7fe61518d3399874492c94b642cb8268861c246692887ef3027380af06b7e692d6733340deebb629a3c8d095364cb6def4071cd5af31cfbfe9ec6b68')

package_webstorm() {
  optdepends=('webstorm-jre: JetBrains custom Java Runtime (Recommended)'
              'java-runtime>=8: JRE - Required if webstorm-jre is not installed')

  install -d -m 755 ${pkgdir}/opt/
  install -d -m 755 ${pkgdir}/usr/bin/
  install -d -m 755 ${pkgdir}/usr/share/applications/
  install -d -m 755 ${pkgdir}/usr/share/pixmaps/

  rsync -rtl ${srcdir}/WebStorm-${_pkgver}/ ${pkgdir}/opt/${pkgbase} --exclude=/jre

  ln -s /opt/${pkgbase}/bin/${pkgbase}.sh ${pkgdir}/usr/bin/${pkgbase}
  install -D -m 644 ${srcdir}/jetbrains-${pkgbase}.desktop ${pkgdir}/usr/share/applications/
  install -D -m 644 ${pkgdir}/opt/${pkgbase}/bin/${pkgbase}.svg ${pkgdir}/usr/share/pixmaps/${pkgbase}.svg
}

package_webstorm-jre() {
  install -d -m 755 ${pkgdir}/opt/${pkgbase}
  rsync -rtl ${srcdir}/WebStorm-${_pkgver}/jre ${pkgdir}/opt/${pkgbase}
}
