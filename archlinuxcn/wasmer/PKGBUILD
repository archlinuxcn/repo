# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>

pkgname=wasmer
pkgver=0.5.6
pkgrel=1
pkgdesc="Universal Binaries Powered by WebAssembly"
arch=('x86_64')
url="https://github.com/wasmerio/wasmer"
license=(MIT)
makedepends=(cargo cmake python git)
source=("git+https://github.com/wasmerio/wasmer.git#tag=0.4.2")
sha512sums=('SKIP')

build() {
  cd "$srcdir/$pkgname"

  git submodule update --init --recursive
  cargo build --release --locked
}

check() {
  cd "$srcdir/$pkgname"

  # Currently broken
  # make test
}

package() {
  cd "$srcdir/$pkgname"

  cargo install --root "$pkgdir"/usr --path .
  rm "$pkgdir"/usr/.crates.toml
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
