# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=fvm
pkgver=3.2.0
pkgrel=2
pkgdesc="Flutter Version Management: A simple CLI to manage Flutter SDK versions."
arch=('x86_64')
url="https://fvm.app"
license=('MIT')
depends=('glibc')
makedepends=('dart')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::https://github.com/leoafarias/fvm/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('50aed46957c4149f88682e9ac062c8aeb44a8da0b023a49aa8e3eb4cd570d72e')

prepare() {
  cd "$pkgname-$pkgver"

  # disable analytics
  dart --disable-analytics

  # download dependencies
  dart pub get
}

build() {
  cd "$pkgname-$pkgver"
  dart compile exe -o bin/fvm bin/main.dart
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 "bin/$pkgname" -t "$pkgdir/usr/bin/"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
