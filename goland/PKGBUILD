# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>

pkgbase=goland
pkgname=(goland goland-jre)
pkgver=2018.3.2
pkgrel=1
pkgdesc='Capable and Ergonomic Go IDE'
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/go/'
license=('Commercial')
makedepends=('rsync')
options=('!strip')
source=(https://download.jetbrains.com/go/${pkgbase}-${pkgver}.tar.gz
        jetbrains-goland.desktop)
sha512sums=('fea01b988e668f461026a741cdc5b054e1a6c93b3ea6d9ae6127f69b4460df9ad2b18a41032c49b5073e8c491594467d6cf8c38f658a23c345a9134a7e384871'
            '391167246a98cc82305ffa7d475960b3f58f78d36dee5cda3f318351e5ddf07d3457688713c1fcc2c20f548aeed387e5a9f16c97423bd37bb43bc502082f61eb')

package_goland() {
  optdepends=('goland-jre: JetBrains custom Java Runtime (Recommended)'
              'java-runtime: JRE - Required if goland-jre is not installed')
  conflicts=('gogland')
  replaces=('gogland')

  install -d -m 755 "${pkgdir}/opt/"
  install -d -m 755 "${pkgdir}/usr/bin/"
  install -d -m 755 "${pkgdir}/usr/share/applications/"
  install -d -m 755 "${pkgdir}/usr/share/pixmaps/"

  rsync -rtl "${srcdir}/GoLand-${pkgver}/" "${pkgdir}/opt/${pkgbase}" --exclude=/jre64

  ln -s "/opt/${pkgbase}/bin/${pkgbase}.sh" "${pkgdir}/usr/bin/${pkgbase}"
  install -D -m 644 "${srcdir}/jetbrains-${pkgbase}.desktop" "${pkgdir}/usr/share/applications/"
  install -D -m 644 "${pkgdir}/opt/${pkgbase}/bin/${pkgbase}.png" "${pkgdir}/usr/share/pixmaps/${pkgbase}.png"
}

package_goland-jre() {
  conflicts=('gogland-jre')
  replaces=('gogland-jre')

  install -d -m 755 "${pkgdir}/opt/${pkgbase}"
  rsync -rtl "${srcdir}/GoLand-${pkgver}/jre64" "${pkgdir}/opt/${pkgbase}"
}
