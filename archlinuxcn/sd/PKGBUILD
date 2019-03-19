# Maintainer: Wesley Moore <wes@wezm.net>
pkgname=sd
pkgver=0.5.0
pkgrel=1
pkgdesc='Intuitive find & replace'
arch=('i686' 'x86_64')
url="https://github.com/chmln/sd"
license=('MIT')
depends=()
conflicts=('sd-git')
makedepends=('rust' 'cargo' 'git')
source=("$pkgver.tar.gz::$url/archive/sd-$pkgver.tar.gz")
sha256sums=('167940e76ce0dd0129832e1cc1302eef9318f9003d27d968fbcba912ce23bb1c')

build() {
  cd "$pkgname-$pkgname-$pkgver"
  /usr/bin/cargo build --release
}

package() {
    install -Dm755 "$srcdir/$pkgname-$pkgname-$pkgver/target/release/$pkgname" "$pkgdir/usr/bin/$pkgname"
}
