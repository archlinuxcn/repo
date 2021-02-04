# Maintainer:  KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Bumsik Kim <k.bumsik@gmail.com>

pkgname=nushell
pkgver=0.26.0
pkgrel=2
pkgdesc="A new type of shell."
url="https://www.nushell.sh"
license=('MIT')
depends=('openssl' 'libxcb' 'libgit2' 'zlib' 'libx11')
makedepends=('rust' 'python')
arch=('x86_64' 'i686')
install=nushell.install
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/nushell/nushell/archive/${pkgver}.tar.gz")
sha256sums=('66fbfe1297997a3f6b2181cd723816150ad2453527c7cab6c83a9c67b9af2478')
b2sums=('d7b06a13f17a03203411df5045557c6cd4689edd69b18500cf29da0b1649423bdb80aebfa1cec3e4d9d2069b1d985da0c8641e27c13e02a9b3ec5c1c9755673b')

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
