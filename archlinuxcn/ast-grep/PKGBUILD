# Maintainer: KokaKiwi <kokakiwi+aur [at] kokakiwi dot com>
# Contributor: Mike Yuan <me@yhndnzj.com>

pkgbase=ast-grep
pkgname=(ast-grep python-ast-grep)
pkgver=0.36.0
pkgrel=1
pkgdesc='A fast and polyglot tool for code structural search, lint, rewriting at large scale'
arch=('x86_64')
url='https://ast-grep.github.io/'
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo' 'python-build' 'python-installer' 'python-wheel' 'python-maturin')
checkdepends=('python')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ast-grep/ast-grep/archive/$pkgver.tar.gz")
sha256sums=('aa8c1199d191859d61f4b407ad8ad34aa46a5a57575110b6605a1bf74f7f2363')
b2sums=('6b548be059b639318af891f12a602dbdbaa1f01d46da5c27dcccd49762d79be2ff70747cee2e5da7c71f06e0e19c54d5474089000486bc314a2fab1277151abf')
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
