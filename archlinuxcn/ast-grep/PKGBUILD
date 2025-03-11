# Maintainer: KokaKiwi <kokakiwi+aur [at] kokakiwi dot com>
# Contributor: Mike Yuan <me@yhndnzj.com>

pkgbase=ast-grep
pkgname=(ast-grep python-ast-grep)
pkgver=0.36.1
pkgrel=1
pkgdesc='A fast and polyglot tool for code structural search, lint, rewriting at large scale'
arch=('x86_64')
url='https://ast-grep.github.io/'
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo' 'python-build' 'python-installer' 'python-wheel' 'python-maturin')
checkdepends=('python')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ast-grep/ast-grep/archive/$pkgver.tar.gz")
sha256sums=('3f0b06c29220eda817a652475f5e73356398550f2f9bf0c134fa0340a17e60cf')
b2sums=('04a220e26511f56cb710255da4e1bdaf6d37ce9d2195a59224b4933f45c6be41c3559e9e9332b815c5f31fd59c09cbe13a04fa26da348bd77620c7ff662bd2af')
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
