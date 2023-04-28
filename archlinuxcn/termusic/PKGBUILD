# Maintainer: orhun <orhunparmaksiz@gmail.com>
# https://github.com/orhun/pkgbuilds

pkgname=termusic
pkgver=0.7.10
pkgrel=1
pkgdesc="Music Player TUI written in Rust"
arch=('x86_64')
url="https://github.com/tramhao/termusic"
license=('MIT' 'GPL3')
depends=('gstreamer' 'gst-plugins-base' 'gst-plugins-good' 'gst-plugins-bad' 'gst-plugins-ugly' 'gst-libav' 'dbus' 'ueberzug')
optdepends=('yt-dlp: download mp3'
            'ffmpeg: download mp3')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha512sums=('f98d0248746b756fc09d022f40412c07e042194edca9997c49484f6464b0be44922581802057192f5e7eb95639f0e697dc3713dde8b7d04bbd6d5ac0ccba7887')
options=('!lto')

prepare() {
  cd "$pkgname-$pkgver"
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgname-$pkgver"
  cargo build --features mpris,cover,discord --release --frozen
}

check() {
  cd "$pkgname-$pkgver"
  cargo test --frozen
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm 755 "target/release/$pkgname" -t "$pkgdir/usr/bin"
  install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm 644 LICENSE_MIT -t "$pkgdir/usr/share/licenses/$pkgname"
}
