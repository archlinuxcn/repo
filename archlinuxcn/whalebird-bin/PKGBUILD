# Maintainer: Mélanie Chauvel (ariasuni) <perso@hack-libre.org>

_appname=whalebird
pkgname="$_appname-bin"
pkgver=3.0.3
pkgrel=1
pkgdesc='An Electron based Mastodon client for Windows, Mac and Linux'
arch=(x86_64)
url='https://whalebird.org/'
license=(MIT)
depends=(c-ares ffmpeg gtk3 http-parser libevent libvpx libxslt libxss minizip nss re2 snappy libnotify libappindicator-gtk3)
source=("https://github.com/h3poteto/whalebird-desktop/releases/download/$pkgver/Whalebird-$pkgver-linux-x64.rpm")
sha256sums=('cab4c85b9760f16bdd88d98a359538894a50e71119d0eda45c0a564072495da8')

package() {
  cp -R opt/ usr/ "$pkgdir"
  mkdir "$pkgdir/usr/bin"
  ln -s /opt/Whalebird/whalebird "$pkgdir/usr/bin/whalebird"
}
