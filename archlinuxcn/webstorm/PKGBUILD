# Maintainer: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgbase=webstorm
pkgname=(webstorm webstorm-jre)
pkgver=2022.3.1
pkgrel=1
pkgdesc='JavaScript IDE and HTML editor'
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/webstorm/'
license=('custom:jetbrains')
depends=('glib2')
options=('!strip')
source=("https://download.jetbrains.com/webstorm/WebStorm-${pkgver}.tar.gz"
        jetbrains-webstorm.desktop
        LICENSE)
b2sums=('aa93b0c0cc4e3a91023da1de2080f5b882a46a9bca4259a912db65a7028a7e1d690bc863f69ef3aa701f8642f1fab5776b41044db1269379b93e3cb134e22f79'
        '0d4e900eb8c78abf7acbbcc86400065d63d9cd3fec77299d7d6abf540a9bf589f879b274f9bb23573f6ef78592b8987414816a56397b9d8d80d6bad29ad4440d'
        'dadaf0e67b598aa7a7a4bf8644943a7ee8ebf4412abb17cd307f5989e36caf9d0db529a0e717a9df5d9537b10c4b13e814b955ada6f0d445913c812b63804e77')

package_webstorm() {
  optdepends=('webstorm-jre: JetBrains custom Java Runtime (Recommended)'
              'java-runtime: JRE - Required if webstorm-jre is not installed'
              'gnome-keyring: save login/deployment credentials safely')
  _buildver="$(ls | grep -Eo 'WebStorm-[[:digit:]]+\.[[:digit:]]{2,5}\.[[:digit:]]+' | sort -r | head -1 | sed 's#WebStorm-##')"

  install -dm755 "${pkgdir}"/opt/
  install -dm755 "${pkgdir}"/usr/bin/
  install -dm755 "${pkgdir}"/usr/share/applications/
  install -dm755 "${pkgdir}"/usr/share/pixmaps/

  cp -a WebStorm-${_buildver:?_buildver unset}/ "${pkgdir}"/opt/${pkgbase}
  rm -rf "${pkgdir}"/opt/${pkgbase}/jbr

  ln -s /opt/${pkgbase}/bin/${pkgbase}.sh "${pkgdir}"/usr/bin/${pkgbase}
  install -m644 "${srcdir}"/jetbrains-${pkgbase}.desktop "${pkgdir}"/usr/share/applications/
  install -m644 "${pkgdir}"/opt/${pkgbase}/bin/${pkgbase}.svg "${pkgdir}"/usr/share/pixmaps/${pkgbase}.svg
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE.txt
}

package_webstorm-jre() {
  pkgdesc='JBR (JetBrains Runtime) for WebStorm - a patched JRE'
  url='https://confluence.jetbrains.com/display/JBR/JetBrains+Runtime'
  _buildver="$(ls | grep -Eo 'WebStorm-[[:digit:]]+\.[[:digit:]]{2,5}\.[[:digit:]]+' | sort -r | head -1 | sed 's#WebStorm-##')"

  install -dm755 "${pkgdir}"/opt/${pkgbase}
  cp -a WebStorm-${_buildver:?_buildver unset}/jbr "${pkgdir}"/opt/${pkgbase}
}
