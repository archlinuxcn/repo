# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=fvm
pkgver=3.2.1
pkgrel=2
pkgdesc="Flutter Version Management: A simple CLI to manage Flutter SDK versions."
arch=('x86_64')
url="https://fvm.app"
license=('MIT')
depends=('git' 'glibc' 'unzip')
makedepends=('dart')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::https://github.com/leoafarias/fvm/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('d4d524a5e1d7c5160b17ee9c3b2dd4482224d2e1c27c8d494fa0290ae818cd41')

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
