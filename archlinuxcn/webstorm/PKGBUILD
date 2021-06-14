# Maintainer: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgbase=webstorm
pkgname=(webstorm webstorm-jre)
pkgver=2021.1.2b211.7442.26
pkgrel=1
pkgdesc='JavaScript IDE and HTML editor'
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/webstorm/'
license=('custom:jetbrains')
depends=('glib2')
options=('!strip')
source=("https://download.jetbrains.com/webstorm/WebStorm-${pkgver%b*}.tar.gz"
        jetbrains-webstorm.desktop
        LICENSE)
b2sums=('93de8d368c89892c587418acd23f8a6edd7f0a7614007a78a5617f956018055a2f27485b150c06a7ae133aecbfb3342db66a65b764ca7adde39c4b86a9a4126d'
        '0d4e900eb8c78abf7acbbcc86400065d63d9cd3fec77299d7d6abf540a9bf589f879b274f9bb23573f6ef78592b8987414816a56397b9d8d80d6bad29ad4440d'
        'dadaf0e67b598aa7a7a4bf8644943a7ee8ebf4412abb17cd307f5989e36caf9d0db529a0e717a9df5d9537b10c4b13e814b955ada6f0d445913c812b63804e77')

package_webstorm() {
  optdepends=('webstorm-jre: JetBrains custom Java Runtime (Recommended)'
              'java-runtime: JRE - Required if webstorm-jre is not installed'
              'gnome-keyring: save login/deployment credentials safely')

  install -dm755 "${pkgdir}"/opt/
  install -dm755 "${pkgdir}"/usr/bin/
  install -dm755 "${pkgdir}"/usr/share/applications/
  install -dm755 "${pkgdir}"/usr/share/pixmaps/

  cp -a "${srcdir}"/WebStorm-${pkgver#*b}/ "${pkgdir}"/opt/${pkgbase}
  rm -rf "${pkgdir}"/opt/${pkgbase}/jbr

  ln -s /opt/${pkgbase}/bin/${pkgbase}.sh "${pkgdir}"/usr/bin/${pkgbase}
  install -m644 "${srcdir}"/jetbrains-${pkgbase}.desktop "${pkgdir}"/usr/share/applications/
  install -m644 "${pkgdir}"/opt/${pkgbase}/bin/${pkgbase}.svg "${pkgdir}"/usr/share/pixmaps/${pkgbase}.svg
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE.txt
}

package_webstorm-jre() {
  pkgdesc='JBR (JetBrains Runtime) for WebStorm - a patched JRE'
  url='https://confluence.jetbrains.com/display/JBR/JetBrains+Runtime'

  install -dm755 "${pkgdir}"/opt/${pkgbase}
  cp -a "${srcdir}"/WebStorm-${pkgver#*b}/jbr "${pkgdir}"/opt/${pkgbase}
}
