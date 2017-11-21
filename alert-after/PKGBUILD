# Maintainer: Vlad M. <vlad@archlinux.net>

pkgname=alert-after
pkgver=1.4.1
pkgrel=1
pkgdesc="Get a desktop notification after a command finishes executing"
arch=('i686' 'x86_64')
url="https://github.com/frewsxcv/alert-after"
license=('MIT' 'Apache')
depends=('dbus')
makedepends=('cargo')
source=("$url/archive/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('c6ef20ed97d114b2bde8442e214847b3ed878ef0b3add903c2486f2cd7732333')

build() {
  cd "$pkgname-$pkgver"
  cargo build --release
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 "target/release/aa" "$pkgdir/usr/bin/aa"
}
