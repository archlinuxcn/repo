# Maintainer :  Kr1ss $(echo \<kr1ss+x-yandex+com\>|sed s/\+/./g\;s/\-/@/)
# Contributor : Mélanie Chauvel (ariasuni) <perso@hack-libre.org>


pkgname=whalebird-bin

pkgver=4.2.0
pkgrel=2

pkgdesc='Electron based multi-platform client for Mastodon, Misskey & Pleroma'
arch=('x86_64')
url="https://${pkgname%-bin}.org"
license=('MIT')

provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")

depends=('c-ares' 'ffmpeg' 'gtk3' 'http-parser' 'libevent' 'libvpx' 'libxslt' 'libxss' 'minizip' 'nss' 're2' 'snappy' 'libnotify' 'libappindicator-gtk3')

source=("https://github.com/h3poteto/${pkgname%-bin}-desktop/releases/download/$pkgver/Whalebird-$pkgver-linux-x64.rpm")
sha256sums=('ce3eb29d052d5db37bd13cecb9dee338f61d15d0e00fe6d8a131a50142637f80')


package() {
  install -Dm644 opt/Whalebird/LICENSE* -t"$pkgdir/usr/share/licenses/${pkgname%-bin}/"
  cp -R usr/share/* "$pkgdir/usr/share/"
  cp -R opt "$pkgdir/"
  install -dm755 "$pkgdir/usr/bin"
  ln -s "/opt/Whalebird/${pkgname%-bin}" "$pkgdir/usr/bin/"
}


# vim: ts=2 sw=2 et ft=PKGBUILD:
