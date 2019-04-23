# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>

pkgname=wasmer
pkgver=0.4.0
pkgrel=1
pkgdesc="Universal Binaries Powered by WebAssembly"
arch=('x86_64')
url="https://github.com/wasmerio/wasmer"
license=(MIT)
makedepends=(cargo cmake python)
source=(https://github.com/wasmerio/wasmer/archive/${pkgver}.tar.gz)
sha512sums=('eed84cd314c14448b7eceb11778c4695ebdd665c3cdad66c3dd4b4abee415d7da7e388ebe4d149de15df9992ac93c4131b88a7f85be4d519dde07c8f8853ec33')

build() {
  cd "$srcdir/$pkgname-$pkgver"

  cargo build --release --locked
}

check() {
  cd "$srcdir/$pkgname-$pkgver"

  # Currently broken
  # make test
}

package() {
  cd "$srcdir/$pkgname-$pkgver"

  install -Dm755 target/release/wasmer "$pkgdir"/usr/bin/wasmer
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
