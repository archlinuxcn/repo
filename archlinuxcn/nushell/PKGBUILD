# Maintainer:  KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Bumsik Kim <k.bumsik@gmail.com>

pkgname=nushell
pkgver=0.33.0
pkgrel=1
pkgdesc="A new type of shell."
url="https://www.nushell.sh"
license=('MIT')
depends=('openssl' 'libxcb' 'libgit2' 'zlib' 'libx11')
makedepends=('rust' 'python')
arch=('x86_64' 'i686' 'aarch64')
install=nushell.install
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/nushell/nushell/archive/${pkgver}.tar.gz")
sha256sums=('13e766ae3de957e322790cf9874ebc1b768abd205228db7181643e66564c6245')
b2sums=('49f903f51c7a61690db50d575f19d5b51b31872fa01e56f621e85b6b57ebe41b98f3284c19d82888a9d21b5510feffb1e345a28c62b5226aa25cf3b6fe53ef89')

build() {
  cd "${pkgname}-${pkgver}"

  cargo build --release --locked --features extra --target-dir=target
}

package() {
  cd "${pkgname}-${pkgver}"

  install -Dm0755 -t "${pkgdir}/usr/bin" \
    target/release/nu $(find target/release -maxdepth 1 -type f -executable -name 'nu_plugin_*')

  install -Dm0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
