# Maintainer: Metal A-wing <1 at 233 dot email>

pkgname=deno
pkgver=0.37.1
pkgrel=1
pkgdesc="A secure JavaScript/TypeScript runtime built with V8, Rust, and Tokio"
arch=('i686' 'x86_64')
url="https://github.com/denoland/deno"
license=('MIT')
depends=('gcc-libs')
makedepends=('git' 'python2' 'cargo' 'nodejs')
source=("${pkgname}-${pkgver}::git+https://github.com/denoland/deno#tag=v${pkgver}")
sha512sums=('SKIP')

prepare() {
  cd ${pkgname}-${pkgver}
  git submodule update --init --recursive
  mkdir -p "${srcdir}"/python2-path
  ln -sf /usr/bin/python2 "${srcdir}/python2-path/python"
  PATH="${srcdir}/python2-path:${PATH}"
}

build() {
  cd ${pkgname}-${pkgver}
  cargo build --release --locked
}

check() {
  cd ${pkgname}-${pkgver}
  ./target/release/deno run cli/tests/002_hello.ts
}

package() {
  cd ${pkgname}-${pkgver}
  install -Dm755 target/release/deno "${pkgdir}"/usr/bin/deno
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}

