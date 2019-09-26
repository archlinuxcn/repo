# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgbase=webstorm
pkgname=(webstorm webstorm-jre)
pkgver=2019.2.3b192.6817.13
pkgrel=1
pkgdesc='JavaScript IDE and HTML editor.'
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/webstorm/'
license=('Commercial')
makedepends=('rsync')
options=('!strip')
source=(https://download.jetbrains.com/webstorm/WebStorm-${pkgver%b*}.tar.gz
        jetbrains-webstorm.desktop)
sha512sums=('06b6a7b5b4282a7571590364ef8eeaaae57f5acfca1af12de02620069ef017cc941de3c1f75d36bebcef7194dc33f19f25bdabbbd0c192ea39c72134aa93315a'
            '3635b8b6787aae583742e95de7d26d0f80b857f48143898e5963f219d1d4ec8b4cb8e37ce3f058324bb5a253b883c2610be848e883576896c67030e9a36be7e6')

pkgver() {
  echo "${pkgver%b*}b$(find ${srcdir} -maxdepth 1 -type d -printf "%P" | cut -d "-" -f2)"
}

package_webstorm() {
  optdepends=('webstorm-jre: JetBrains custom Java Runtime (Recommended)'
              'java-runtime: JRE - Required if webstorm-jre is not installed'
              'gnome-keyring: save login/deployment credentials safely')

  install -d -m 755 "${pkgdir}/opt/"
  install -d -m 755 "${pkgdir}/usr/bin/"
  install -d -m 755 "${pkgdir}/usr/share/applications/"
  install -d -m 755 "${pkgdir}/usr/share/pixmaps/"

  rsync -rtl "${srcdir}/WebStorm-${pkgver#*b}/" "${pkgdir}/opt/${pkgbase}" --exclude=/jbr

  ln -s "/opt/${pkgbase}/bin/${pkgbase}.sh" "${pkgdir}/usr/bin/${pkgbase}"
  install -D -m 644 "${srcdir}/jetbrains-${pkgbase}.desktop" "${pkgdir}/usr/share/applications/"
  install -D -m 644 "${pkgdir}/opt/${pkgbase}/bin/${pkgbase}.svg" "${pkgdir}/usr/share/pixmaps/${pkgbase}.svg"
}

package_webstorm-jre() {
  install -d -m 755 "${pkgdir}/opt/${pkgbase}"
  rsync -rtl "${srcdir}/WebStorm-${pkgver#*b}/jbr" "${pkgdir}/opt/${pkgbase}"
}
