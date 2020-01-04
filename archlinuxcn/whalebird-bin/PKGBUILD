# Maintainer: Mélanie Chauvel (ariasuni) <perso@hack-libre.org>

_appname=whalebird
pkgname="$_appname-bin"
pkgver=3.0.2
pkgrel=1
pkgdesc='An Electron based Mastodon client for Windows, Mac and Linux'
arch=(x86_64)
url='https://whalebird.org/'
license=(MIT)
depends=(c-ares ffmpeg gtk3 http-parser libevent libvpx libxslt libxss minizip nss re2 snappy libnotify libappindicator-gtk3)
source=("https://github.com/h3poteto/whalebird-desktop/releases/download/$pkgver/Whalebird-$pkgver-linux-x64.rpm")
sha256sums=('4662d78cddc864c4792cf31bb340bbc774f55f27022d2b839d030efec7fa7fd7')

package() {
  cp -R opt/ usr/ "$pkgdir"
  mkdir "$pkgdir/usr/bin"
  ln -s /opt/Whalebird/whalebird "$pkgdir/usr/bin/whalebird"
}
