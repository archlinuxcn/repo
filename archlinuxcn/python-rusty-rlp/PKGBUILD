# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=rusty-rlp
pkgname=python-$_name
pkgver=0.4.0
pkgrel=1
pkgdesc='Python bindings for rust rlp'
arch=(x86_64)
url=https://github.com/cburgdorf/$_name
license=(MIT)
depends=(gcc-libs glibc python)
makedepends=(cargo git maturin python-installer)
source=("git+$url.git#tag=$pkgver")
sha512sums=('da7b2153ab89287c03f727c0ed1f3fd5d1d2e535ddc1f51ff38b1b75da0f9907aec67573479e28e1cf8bdd716dd08fe0b8ba3d734c43f461653c782a175f4a79')

prepare() {
  cd $_name
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd $_name
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  maturin build --locked --release --target "$(rustc -vV | sed -n 's/host: //p')" --strip
}

check() {
  cd $_name
  export RUSTUP_TOOLCHAIN=stable
  cargo test --frozen
}

package() {
  cd $_name
  python -m installer -d "$pkgdir" target/wheels/*.whl
  install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
  install -Dm0644 -t "$pkgdir/usr/share/doc/$pkgname/" README.md
}
