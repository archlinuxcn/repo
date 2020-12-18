# Maintainer:  KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Bumsik Kim <k.bumsik@gmail.com>

pkgname=nushell
pkgver=0.24.1
pkgrel=1
pkgdesc="A new type of shell."
url="https://www.nushell.sh"
license=('MIT')
depends=('openssl' 'libxcb' 'libgit2' 'zlib' 'libx11')
makedepends=('rust' 'python')
arch=('x86_64' 'i686')
source=("https://github.com/nushell/nushell/archive/${pkgver}.tar.gz")
install=nushell.install
sha256sums=('6048137c092c90c77d55717d477669374115e77d08c77c3e85734086084a32b3')
b2sums=('6034948e59932c92b85bc1b6ca03ac755baa6476da979ab4064e2e6fe78a7b8fada1e8869944592199f3606902cb213d29601ec702b105979cd11c65e7f8643a')

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
