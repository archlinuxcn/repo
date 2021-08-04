# Maintainer:  KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Bumsik Kim <k.bumsik@gmail.com>

pkgname=nushell
pkgver=0.35.0
pkgrel=1
pkgdesc="A new type of shell."
url="https://www.nushell.sh"
license=('MIT')
depends=('openssl' 'libxcb' 'libgit2' 'zlib' 'libx11')
makedepends=('rust' 'python')
arch=('x86_64' 'i686' 'aarch64')
install=nushell.install
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/nushell/nushell/archive/${pkgver}.tar.gz")
cksums=('1290491688')
sha256sums=('2e93366a2f089bdbe0ae52eafcda5390119642c66e541b26e8eeb1ab4bc13823')
b2sums=('1a179cfa8e4a6bb5f7543e7a22ef2de596b5f03cb0c401e1751d525cbf7e3466704495b815a84e609cc67d99fe18f9be2b840dd5b380afd2c05667418ca9431b')

build() {
  cd "${pkgname}-${pkgver}"

  RUSTUP_TOOLCHAIN=stable cargo build --release --locked --all-features --target-dir=target
}

package() {
  cd "${pkgname}-${pkgver}"

  install -Dm0755 -t "${pkgdir}/usr/bin" \
    target/release/nu $(find target/release -maxdepth 1 -type f -executable -name 'nu_plugin_*')

  install -Dm0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
