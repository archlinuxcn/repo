# Maintainer:  KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Bumsik Kim <k.bumsik@gmail.com>

pkgname=nushell
pkgver=0.30.0
pkgrel=1
pkgdesc="A new type of shell."
url="https://www.nushell.sh"
license=('MIT')
depends=('openssl' 'libxcb' 'libgit2' 'zlib' 'libx11')
makedepends=('rust' 'python')
arch=('x86_64' 'i686' 'aarch64')
install=nushell.install
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/nushell/nushell/archive/${pkgver}.tar.gz")
sha256sums=('a36cd3d93c69aab83c874fe0c8b653ce9fe188da9f527d3bb28492ba213e579a')
b2sums=('efcf5c73c0467d0972329ac9c00b064d5288d57a8925c6deada60aba87d06fed2f80c69dd5a37cf121e23ec7c176fdd32cbb6b163d55ad5feefa231715bcf24c')

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
