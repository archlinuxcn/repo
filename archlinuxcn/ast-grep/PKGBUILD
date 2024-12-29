# Maintainer: KokaKiwi <kokakiwi+aur [at] kokakiwi dot com>
# Contributor: Mike Yuan <me@yhndnzj.com>

pkgbase=ast-grep
pkgname=(ast-grep python-ast-grep)
pkgver=0.32.2
pkgrel=2
pkgdesc='A fast and polyglot tool for code structural search, lint, rewriting at large scale'
arch=('x86_64')
url='https://ast-grep.github.io/'
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo' 'python-build' 'python-installer' 'python-wheel' 'python-maturin')
checkdepends=('python')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ast-grep/ast-grep/archive/$pkgver.tar.gz")
sha256sums=('ed36c448bdcb538497d17dfd4e1a8826c096662dec020ac99a77f4945793a9ea')
b2sums=('7b019477e997d793c3dbf2867b1f8d9acbfa97cc54ee43f6dddb57439d9992d844a21eb33d63a8f7a5cf68a7bc637e4a59d2413fcabe14e27ca2dcad64c4c038')
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
