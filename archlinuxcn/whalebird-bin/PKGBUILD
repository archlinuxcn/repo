# Maintainer: Mélanie Chauvel (ariasuni) <perso@hack-libre.org>

_appname=whalebird
pkgname="$_appname-bin"
pkgver=3.0.1
pkgrel=1
pkgdesc='An Electron based Mastodon client for Windows, Mac and Linux'
arch=(x86_64)
url='https://whalebird.org/'
license=(MIT)
depends=(alsa-lib gconf gtk2 libxss libxtst nss)
source=("https://github.com/h3poteto/whalebird-desktop/releases/download/$pkgver/Whalebird-$pkgver-linux-x64.rpm")
sha256sums=('ffa2d96a0ebe1f73729e45b86f5b7cbaa282923a1e032305b47cef3d005e682d')

package() {
  cp -R opt/ usr/ "$pkgdir"
  mkdir "$pkgdir/usr/bin"
  ln -s /opt/Whalebird/whalebird "$pkgdir/usr/bin/whalebird"
}
