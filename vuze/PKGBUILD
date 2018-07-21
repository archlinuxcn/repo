# Maintainer: Det <nimetonmaili gmail a-dot com>
# Contributor: vorbote <palopezv AT gmail DOT com >
# Contributor: td123 <gostrc AT gmail DOT com>
# Contributor: phoenixlzx < phoenixlzx AT phoenixsec DOT org >

pkgname=vuze
pkgver=5.7.6.0
pkgrel=1
_ver=${pkgver//./} 
pkgdesc="A feature-rich Java-based BitTorrent client (previously called 'Azureus')"
arch=('x86_64')
url="http://sourceforge.net/projects/azureus/"
license=('GPL')
depends=('desktop-file-utils' 'java-runtime')
optdepends=('vuze-plugin-countrylocator: Country flags for the "Peers" tab'
            'vuze-plugin-mldht: The alternative Distributed Hash Table implementation (DHT) used by µTorrent'
            'xulrunner192: Needed for the channels GUI')
options=('!strip')
install=$pkgname.install
source=("http://downloads.sourceforge.net/azureus/vuze/Vuze_${_ver}/Vuze_${_ver}_linux.tar.bz2")
md5sums=('0c6cba3f2ef401df5c09e020ce9b1ff3')

package() {
  cd $pkgname

  msg2 "Creating directory structure..."
  install -d "$pkgdir"/opt/$pkgname/
  install -d "$pkgdir"/usr/bin/
  install -d "$pkgdir"/usr/share/applications/
  install -d "$pkgdir"/usr/share/licenses/$pkgname/
  install -d "$pkgdir"/usr/share/pixmaps/

  msg2 "Moving stuff in place..."
  # Launchers
  mv $pkgname "$pkgdir"/usr/bin/$pkgname
  ln -s $pkgname "$pkgdir"/usr/bin/azureus

  # swt.jar
  mv swt/swt64.jar "$pkgdir"/opt/$pkgname/swt.jar

  # Icon and desktop 
  mv $pkgname.png "$pkgdir"/usr/share/pixmaps/
  mv $pkgname.desktop "$pkgdir"/usr/share/applications/

  # Licenses
  for i in GPL.txt GPLv3.txt LICENSES.txt TOS.txt; do
    mv $i "$pkgdir"/usr/share/licenses/$pkgname/
  done

  msg2 "Removing redundancies..."
  rm -r swt/
  rm    azureus
  rm    installer.log
  rm    README.txt
  rm    $pkgname.schemas

  msg2 "Installing to /opt..."
  mv * "$pkgdir"/opt/$pkgname/

  msg2 "Fixing paths..."
  sed -i "s|#PROGRAM_DIR=.*|PROGRAM_DIR=\"/opt/$pkgname\"|" "$pkgdir"/usr/bin/$pkgname

  msg2 "Adding support for magnet links..."
  sed -r -e "s|Exec=$pkgname %f|Exec=$pkgname %U|" \
         -e "s|(x-bittorrent)|\1;x-scheme-handler/magnet;|" \
         -i "$pkgdir"/usr/share/applications/$pkgname.desktop
}
