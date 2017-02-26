# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgbase=webstorm
pkgname=(webstorm webstorm-jre)
pkgver=2016.3.3
_pkgver=163.12024.17
pkgrel=2
pkgdesc='JavaScript IDE and HTML editor.'
arch=('x86_64' 'i686')
license=('Commercial')
url='https://www.jetbrains.com/webstorm/'
options=('!strip')
makedepends=('rsync')
source=(https://download.jetbrains.com/webstorm/WebStorm-${pkgver}.tar.gz
        jetbrains-webstorm.desktop)
sha512sums=('5b48d63f81dcfda947c5208bf16a3114a2100bce3028790e9048099e9b056535b7277eea3fbc1eb64f168c1776bc96147e3f712d4c0f88b65f5f8dc87dbe5ee3'
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
