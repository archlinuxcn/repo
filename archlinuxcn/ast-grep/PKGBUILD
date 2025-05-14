# Maintainer: KokaKiwi <kokakiwi+aur [at] kokakiwi dot com>
# Contributor: Mike Yuan <me@yhndnzj.com>

pkgbase=ast-grep
pkgname=(ast-grep python-ast-grep)
pkgver=0.38.1
pkgrel=1
pkgdesc='A fast and polyglot tool for code structural search, lint, rewriting at large scale'
arch=('x86_64')
url='https://ast-grep.github.io/'
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo' 'python-build' 'python-installer' 'python-wheel' 'python-maturin')
checkdepends=('python')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ast-grep/ast-grep/archive/$pkgver.tar.gz")
sha256sums=('e1378aef969fbedd450f52eb85bf56a0389acdfd09316c130b28ade920a59cb3')
b2sums=('4d663a1d57da2fceb2c653edbef7481a9c067841c15224ac2c657af7bcad0553d10b8c7e91cd58a205b4f450f7fac9c1d2b1fc5b2541039ffae7c7d458b64fe0')
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
