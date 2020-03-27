# Maintainer: Frederik Schwan <freswa at archlinux dot org>

pkgbase=goland
pkgname=(goland goland-jre)
pkgver=2019.3.4
pkgrel=1
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/go/'
license=('commercial')
depends=('glib2')
options=('!strip')
source=("https://download.jetbrains.com/go/${pkgbase}-${pkgver}.tar.gz"
        jetbrains-goland.desktop
        LICENSE)
sha512sums=('4874502bf6a031221419a015993a78d7139afafda7c92d6567e0fc81eb7b15f6766b1b934567a9b7c1f1395c7529bc838d7df3c42dcd5045e1086e8176e5e578'
            'bafd07eebf41fd815d182473041ff1cf6e069a4c66755cb5eeea27d8f5222e7c79a85765d14d7f78e57d29bdf91ba844069946388c80689189ac7f60c9c1cb81'
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
