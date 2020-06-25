# Maintainer :  Kr1ss $(echo \<kr1ss+x-yandex+com\>|sed s/\+/./g\;s/\-/@/)
# Contributor : Mélanie Chauvel (ariasuni) <perso@hack-libre.org>


pkgname=whalebird-bin

pkgver=4.1.3
pkgrel=2

pkgdesc='Electron based Mastodon client for Windows, Mac and Linux'
arch=('x86_64')
url="https://${pkgname%-bin}.org"
license=('MIT')

depends=('c-ares' 'ffmpeg' 'gtk3' 'http-parser' 'libevent' 'libvpx' 'libxslt' 'libxss' 'minizip' 'nss' 're2' 'snappy' 'libnotify' 'libappindicator-gtk3')

source=("https://github.com/h3poteto/${pkgname%-bin}-desktop/releases/download/$pkgver/Whalebird-$pkgver-linux-x64.rpm")
sha256sums=('a661273879bbdded3b33e7d29dcc97b1eac87eaa8be72a372eb2128f7b69db40')


package() {
  install -Dm644 opt/Whalebird/LICENSE* -t"$pkgdir/usr/share/licenses/${pkgname%-bin}/"
  cp -R usr/share/* "$pkgdir/usr/share/"
  cp -R opt "$pkgdir/"
  install -dm755 "$pkgdir/usr/bin"
  ln -s "/opt/Whalebird/${pkgname%-bin}" "$pkgdir/usr/bin/"
}


# vim: ts=2 sw=2 et ft=PKGBUILD:
