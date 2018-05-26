# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>

pkgbase=goland
pkgname=(goland goland-jre)
pkgver=2018.1.4
pkgrel=1
pkgdesc='Capable and Ergonomic Go IDE'
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/go/'
license=('Commercial')
makedepends=('rsync')
options=('!strip')
source=(https://download.jetbrains.com/go/${pkgbase}-${pkgver}.tar.gz
        jetbrains-goland.desktop)
sha512sums=('972c15d6636728e214b355ce4ce7174d08e0e842c6ca4e4385fbc4330930a2fae3a964b1b3753c38fe77ac2b8073fd7366fd0085d00fcf05b832c985d6243325'
            '391167246a98cc82305ffa7d475960b3f58f78d36dee5cda3f318351e5ddf07d3457688713c1fcc2c20f548aeed387e5a9f16c97423bd37bb43bc502082f61eb')

package_goland() {
  optdepends=('goland-jre: JetBrains custom Java Runtime (Recommended)'
              'java-runtime>=8: JRE - Required if goland-jre is not installed')
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
