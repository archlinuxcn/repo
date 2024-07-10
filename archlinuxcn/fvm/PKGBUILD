# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=fvm
pkgver=3.1.7
pkgrel=1
pkgdesc="Flutter Version Management: A simple CLI to manage Flutter SDK versions."
arch=('x86_64')
url="https://fvm.app"
license=('MIT')
depends=('git' 'unzip')
makedepends=('dart')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::https://github.com/leoafarias/fvm/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('a479b54c4ade1df99dee975adbf61b56c6dff224915e44d4914925e4dfce8b4c')

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
