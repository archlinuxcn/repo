# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>

pkgbase=goland
pkgname=(goland goland-jre)
pkgver=2019.3.2
pkgrel=1
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/go/'
license=('commercial')
depends=('glib2')
options=('!strip')
source=("https://download.jetbrains.com/go/${pkgbase}-${pkgver}.tar.gz"
        jetbrains-goland.desktop
        LICENSE)
sha512sums=('9741675570ee4d17251ce5a7661e8ff052d3b5753de9c297f847631c99e74ab22793450b6738cb222a587063ae26d4fda0e4c5a1f69573282d8b03bc3578736c'
            '930a0f1269b7f49f7a08fd5fbfff178628114dee01f4e4e8426c643d7c442b77f178b5188325caf0ace5503c5f873a419cd3f7128b63d7c3c9baf8065b0065aa'
            'e2aaaa75571f368f85bcc4baef27cc502781ce382bf04737763b07244716918fc2f0eb0b78b02631e242c9a5c246b27d720bb28556fc64bbde213403b7bf57f6')

package_goland() {
  pkgdesc='Capable and Ergonomic Go IDE'
  optdepends=('goland-jre: JetBrains custom Java Runtime (Recommended)'
              'java-runtime: JRE - Required if goland-jre is not installed')
  conflicts=('gogland')
  replaces=('gogland')

  install -dm755 "${pkgdir}"/opt/
  install -dm755 "${pkgdir}"/usr/bin/
  install -dm755 "${pkgdir}"/usr/share/applications/
  install -dm755 "${pkgdir}"/usr/share/pixmaps/

  cp -a "${srcdir}"/GoLand-${pkgver}/ "${pkgdir}"/opt/${pkgbase}
  rm -rf "${pkgdir}"/opt/${pkgbase}/jbr

  ln -s /opt/${pkgbase}/bin/${pkgbase}.sh "${pkgdir}"/usr/bin/${pkgbase}
  install -m644 "${srcdir}"/jetbrains-${pkgbase}.desktop "${pkgdir}"/usr/share/applications/
  install -m644 "${pkgdir}"/opt/${pkgbase}/bin/${pkgbase}.png "${pkgdir}"/usr/share/pixmaps/${pkgbase}.png
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE.txt
}

package_goland-jre() {
  pkgdesc='JBR (JetBrains Runtime) for Goland - a patched JRE'
  url='https://confluence.jetbrains.com/display/JBR/JetBrains+Runtime'
  conflicts=('gogland-jre')
  replaces=('gogland-jre')

  install -dm755 "${pkgdir}"/opt/${pkgbase}
  cp -a "${srcdir}"/GoLand-${pkgver}/jbr "${pkgdir}"/opt/${pkgbase}
}
