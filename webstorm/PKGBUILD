# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgbase=webstorm
pkgname=(webstorm webstorm-jre)
pkgver=2017.1
_pkgver=171.3780.79
pkgrel=1
pkgdesc='JavaScript IDE and HTML editor.'
arch=('x86_64' 'i686')
license=('Commercial')
url='https://www.jetbrains.com/webstorm/'
options=('!strip')
makedepends=('rsync')
source=(https://download.jetbrains.com/webstorm/WebStorm-${pkgver}.tar.gz
        jetbrains-webstorm.desktop)
sha512sums=('7f62239a20121f647b917bdf8dba7adc87c9dcfc0eb85dce81f53b8de59030043cc6ba9fd5b38c6eb7e079bdfad960e9723ffbd2421503af06dc1e951420d96d'
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
