# Maintainer: Mélanie Chauvel (ariasuni) <perso@hack-libre.org>

_appname=whalebird
pkgname="$_appname-bin"
pkgver=2.8.4
pkgrel=1
pkgdesc='An Electron based Mastodon client for Windows, Mac and Linux'
arch=(x86_64)
url='https://whalebird.org/'
license=(MIT)
depends=(alsa-lib gconf gtk2 libxss libxtst nss)
source=("https://github.com/h3poteto/whalebird-desktop/releases/download/$pkgver/Whalebird-$pkgver-linux-x64.rpm")
sha256sums=('519246d24274c376293eef7d8bd8cb7beee5333658d684e97730b954a8aee042')

package() {
  cp -R opt/ usr/ $pkgdir
  mkdir $pkgdir/usr/bin
  ln -s "/opt/Whalebird/whalebird" $pkgdir/usr/bin/whalebird
}
