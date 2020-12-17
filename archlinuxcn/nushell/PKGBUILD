# Maintainer:  KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Bumsik Kim <k.bumsik@gmail.com>

pkgname=nushell
pkgver=0.24.0
pkgrel=1
pkgdesc="A new type of shell."
url="https://www.nushell.sh"
license=('MIT')
depends=('openssl' 'libxcb' 'libgit2' 'zlib' 'libx11')
makedepends=('rust' 'python')
arch=('x86_64' 'i686')
source=("https://github.com/nushell/nushell/archive/${pkgver}.tar.gz")
install=nushell.install
sha256sums=('02edabab67947cc3907d71010778248b5836e04998c32f7e4957feaf669b54a9')
b2sums=('e688a6d5ca8450c76b5e772a4a3b4ce3603c84fae8ab2663cf3b24aa444ef29e48aa0776fb89bc4fe91cb071ae6c50e49d21f2616249aa421337a3cf52731988')

build() {
  cd "${pkgname}-${pkgver}"

  cargo build --release --locked --features extra
}

package() {
  cd "${pkgname}-${pkgver}"

  install -Dm0755 -t "${pkgdir}/usr/bin" \
    target/release/nu $(find target/release -maxdepth 1 -type f -executable -name 'nu_plugin_*')

  install -Dm0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
