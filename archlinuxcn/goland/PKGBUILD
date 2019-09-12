# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>

pkgbase=goland
pkgname=(goland goland-jre)
pkgver=2019.2.2
pkgrel=1
pkgdesc='Capable and Ergonomic Go IDE'
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/go/'
license=('Commercial')
makedepends=('rsync')
options=('!strip')
source=(https://download.jetbrains.com/go/${pkgbase}-${pkgver}.tar.gz
        jetbrains-goland.desktop)
sha512sums=('0a114c6cd707efcfcbb8c62bc879509922cae0df20c2013d77fb1df0c12aaf3e90131a26a470ced614e2b867dd626aebfb01f7e6d968b65cd485dd7e091bcba5'
            '930a0f1269b7f49f7a08fd5fbfff178628114dee01f4e4e8426c643d7c442b77f178b5188325caf0ace5503c5f873a419cd3f7128b63d7c3c9baf8065b0065aa')

package_goland() {
  optdepends=('goland-jre: JetBrains custom Java Runtime (Recommended)'
              'java-runtime: JRE - Required if goland-jre is not installed')
  conflicts=('gogland')
  replaces=('gogland')

  install -d -m 755 "${pkgdir}/opt/"
  install -d -m 755 "${pkgdir}/usr/bin/"
  install -d -m 755 "${pkgdir}/usr/share/applications/"
  install -d -m 755 "${pkgdir}/usr/share/pixmaps/"

  rsync -rtl "${srcdir}/GoLand-${pkgver}/" "${pkgdir}/opt/${pkgbase}" --exclude=/jbr

  ln -s "/opt/${pkgbase}/bin/${pkgbase}.sh" "${pkgdir}/usr/bin/${pkgbase}"
  install -D -m 644 "${srcdir}/jetbrains-${pkgbase}.desktop" "${pkgdir}/usr/share/applications/"
  install -D -m 644 "${pkgdir}/opt/${pkgbase}/bin/${pkgbase}.png" "${pkgdir}/usr/share/pixmaps/${pkgbase}.png"
}

package_goland-jre() {
  conflicts=('gogland-jre')
  replaces=('gogland-jre')

  install -d -m 755 "${pkgdir}/opt/${pkgbase}"
  rsync -rtl "${srcdir}/GoLand-${pkgver}/jbr" "${pkgdir}/opt/${pkgbase}"
}
