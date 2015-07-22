# Maintainer: josephgbr <rffontenelle AT gmail DOT com>
# Co-maintainer: Det <nimetonmaili gmail a-dot com>
# Contributor: vorbote <palopezv AT gmail DOT com >
# Contributor: td123 <gostrc AT gmail DOT com>
# Contributor: phoenixlzx < phoenixlzx AT phoenixsec DOT org >

pkgname=vuze
pkgver=5.6.1.2
pkgrel=3
_ver=${pkgver//./} 
pkgdesc="A feature-rich Java-based BitTorrent client (previously called 'Azureus')"
arch=('i686' 'x86_64')
url="http://sourceforge.net/projects/azureus/"
license=('GPL')
depends=('desktop-file-utils' 'java-runtime')
optdepends=('vuze-plugin-countrylocator: Country flags for the "Peers" tab'
            'vuze-plugin-mldht: The alternative Distributed Hash Table implementation (DHT) used by µTorrent'
            'xulrunner192: Needed for the channels GUI')
options=('!strip')
install=$pkgname.install
source=("http://downloads.sourceforge.net/azureus/vuze/Vuze_${_ver}/Vuze_${_ver}_linux.tar.bz2")
md5sums=('c20397aa00614ab8b271afef93c877bc')

package() {
  cd vuze

  msg2 "Creating directory structure..."
  install -d "$pkgdir"/opt/vuze/
  install -d "$pkgdir"/usr/bin/
  install -d "$pkgdir"/usr/share/applications/
  install -d "$pkgdir"/usr/share/licenses/vuze/
  install -d "$pkgdir"/usr/share/pixmaps/

  msg2 "Moving stuff in place..."
  # Launchers
  mv vuze "$pkgdir"/usr/bin/vuze
  ln -s vuze "$pkgdir"/usr/bin/azureus

  # swt.jar
  case "$CARCH" in
    i686)   mv swt/swt32.jar "$pkgdir"/opt/vuze/swt.jar ;;
    x86_64) mv swt/swt64.jar "$pkgdir"/opt/vuze/swt.jar ;;
  esac

  # Icon and desktop 
  mv vuze.png "$pkgdir"/usr/share/pixmaps/
  mv vuze.desktop "$pkgdir"/usr/share/applications/

  # Licenses
  mv GPL.txt      "$pkgdir"/usr/share/licenses/vuze/
  mv GPLv3.txt    "$pkgdir"/usr/share/licenses/vuze/
  mv LICENSES.txt "$pkgdir"/usr/share/licenses/vuze/
  mv TOS.txt      "$pkgdir"/usr/share/licenses/vuze/

  msg2 "Removing redundancies..."
  rm -r swt/
  rm    azureus
  rm    installer.log
  rm    README.txt
  rm    vuze.schemas

  msg2 "Installing to /opt..."
  mv * "$pkgdir"/opt/vuze/

  msg2 "Fixing paths"
  sed 's|#PROGRAM_DIR=.*|PROGRAM_DIR="/opt/vuze"|' \
      -i "$pkgdir"/usr/bin/vuze \

  msg2 "Adding support for magnet links..."
  sed -r -e 's|Exec=vuze %f|Exec=vuze %U|' \
         -e 's|(x-bittorrent)|\1;x-scheme-handler/magnet;|' \
      -i "$pkgdir"/usr/share/applications/vuze.desktop
}
