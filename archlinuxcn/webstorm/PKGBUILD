# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgbase=webstorm
pkgname=(webstorm webstorm-jre)
pkgver=2019.3.1b193.5662.54
pkgrel=1
pkgdesc='JavaScript IDE and HTML editor.'
arch=('x86_64' 'i686')
url='https://www.jetbrains.com/webstorm/'
license=('commercial')
depends=('glib2')
options=('!strip')
source=("https://download.jetbrains.com/webstorm/WebStorm-${pkgver%b*}.tar.gz"
        jetbrains-webstorm.desktop
        LICENSE)
sha512sums=('d14d627e91154606e190e26006a357998b2882400d1e42f72f4b9f0fcd881fe7e9f7af104e33204cc18e60f02b27f4b7e36dab9fb15e8efd70d216563e50d489'
            '3635b8b6787aae583742e95de7d26d0f80b857f48143898e5963f219d1d4ec8b4cb8e37ce3f058324bb5a253b883c2610be848e883576896c67030e9a36be7e6'
            'e2aaaa75571f368f85bcc4baef27cc502781ce382bf04737763b07244716918fc2f0eb0b78b02631e242c9a5c246b27d720bb28556fc64bbde213403b7bf57f6')

pkgver() {
  echo "${pkgver%b*}b$(find ${srcdir} -maxdepth 1 -type d -printf "%P" | cut -d "-" -f2)"
}

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
