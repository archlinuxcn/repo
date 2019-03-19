# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>

pkgname=wasmer
pkgver=0.2.1
pkgrel=1
pkgdesc="Universal Binaries Powered by WebAssembly"
arch=('x86_64')
url="https://github.com/wasmerio/wasmer"
license=(MIT)
makedepends=(cargo cmake python)
source=(https://github.com/wasmerio/wasmer/archive/${pkgver}.tar.gz)
sha512sums=('f949a686cb5b5dc63d361e93d5ef73f11a2f3450dd6af8d2be9553ceabdff24ccfaa64067862bed091e8090c9fcbac359d83106892ba354d72729f675f42e0c0')

build() {
  cd "$srcdir/$pkgname-$pkgver"

  cargo build --release --locked
}

check() {
  cd "$srcdir/$pkgname-$pkgver"

  make test
}

package() {
  cd "$srcdir/$pkgname-$pkgver"

  install -Dm755 target/release/wasmer "$pkgdir"/usr/bin/wasmer
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
