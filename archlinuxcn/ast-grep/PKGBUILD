# Maintainer: KokaKiwi <kokakiwi+aur [at] kokakiwi dot com>
# Contributor: Mike Yuan <me@yhndnzj.com>

pkgbase=ast-grep
pkgname=(ast-grep python-ast-grep)
pkgver=0.38.0
pkgrel=1
pkgdesc='A fast and polyglot tool for code structural search, lint, rewriting at large scale'
arch=('x86_64')
url='https://ast-grep.github.io/'
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo' 'python-build' 'python-installer' 'python-wheel' 'python-maturin')
checkdepends=('python')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ast-grep/ast-grep/archive/$pkgver.tar.gz")
sha256sums=('1377cfcaaf0d42c9cb757ab92a91b2fd84404944b194030fda7b4d5180d6fb68')
b2sums=('2dc701e3ea883add36123ac68579c289ceadaaae0a2249c3bdb39814c3591beab9c31905a5cc0672c7d43d41ad1376ffb3d1e881721ca64471a9bd39a18ccf1b')
options=('!lto')

export RUSTUP_TOOLCHAIN=${RUSTUP_TOOLCHAIN:-stable}

prepare() {
  cd "$pkgbase-$pkgver"

  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "$pkgbase-$pkgver"

  CARGO_TARGET_DIR=target \
  cargo build --frozen --release --all-features --package ast-grep --bin ast-grep

  cd crates/pyo3
  python -m build --wheel --no-isolation
}

check() {
  cd "$pkgbase-$pkgver"

  RUSTFLAGS="$RUSTFLAGS -C debug-assertions" cargo test --frozen --all-features
}

package_ast-grep() {
  cd "$pkgbase-$pkgver"

  install -Dm0755 -t "$pkgdir/usr/bin" \
    target/release/ast-grep
  ln -sf ast-grep "$pkgdir/usr/bin/asg"

  install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    LICENSE
}

package_python-ast-grep() {
  depends=('python')

  cd "$pkgbase-$pkgver"

  install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    LICENSE

  cd crates/pyo3
  python -m installer --destdir="$pkgdir" dist/*.whl
}
