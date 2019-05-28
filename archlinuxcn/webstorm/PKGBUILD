# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgbase=webstorm
pkgname=(webstorm webstorm-jre)
pkgver=2019.1.3
_pkgver=191.7479.14
pkgrel=1
pkgdesc='JavaScript IDE and HTML editor.'
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/webstorm/'
license=('Commercial')
makedepends=('rsync')
options=('!strip')
source=(https://download.jetbrains.com/webstorm/WebStorm-${pkgver}.tar.gz
        jetbrains-webstorm.desktop)
sha512sums=('bb54b97f36fa4c0bcb36ca21b05b2eddcbfe607690ff736c8b50da57c1c637e303494e37ea01165899db2bc01c155c664b2a62cc6a9cf36e11690dc1df16e00c'
            'e261eb9b7fe61518d3399874492c94b642cb8268861c246692887ef3027380af06b7e692d6733340deebb629a3c8d095364cb6def4071cd5af31cfbfe9ec6b68')

package_webstorm() {
  optdepends=('webstorm-jre: JetBrains custom Java Runtime (Recommended)'
              'java-runtime: JRE - Required if webstorm-jre is not installed'
              'gnome-keyring: save login/deployment credentials safely')

  install -d -m 755 "${pkgdir}/opt/"
  install -d -m 755 "${pkgdir}/usr/bin/"
  install -d -m 755 "${pkgdir}/usr/share/applications/"
  install -d -m 755 "${pkgdir}/usr/share/pixmaps/"

  rsync -rtl "${srcdir}/WebStorm-${_pkgver}/" "${pkgdir}/opt/${pkgbase}" --exclude=/jre64

  ln -s "/opt/${pkgbase}/bin/${pkgbase}.sh" "${pkgdir}/usr/bin/${pkgbase}"
  install -D -m 644 "${srcdir}/jetbrains-${pkgbase}.desktop" "${pkgdir}/usr/share/applications/"
  install -D -m 644 "${pkgdir}/opt/${pkgbase}/bin/${pkgbase}.svg" "${pkgdir}/usr/share/pixmaps/${pkgbase}.svg"
}

package_webstorm-jre() {
  install -d -m 755 "${pkgdir}/opt/${pkgbase}"
  rsync -rtl "${srcdir}/WebStorm-${_pkgver}/jre64" "${pkgdir}/opt/${pkgbase}"
}
