# Maintainer:  KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Bumsik Kim <k.bumsik@gmail.com>

pkgname=nushell
pkgver=0.25.0
pkgrel=1
pkgdesc="A new type of shell."
url="https://www.nushell.sh"
license=('MIT')
depends=('openssl' 'libxcb' 'libgit2' 'zlib' 'libx11')
makedepends=('rust' 'python')
arch=('x86_64' 'i686')
source=("https://github.com/nushell/nushell/archive/${pkgver}.tar.gz")
install=nushell.install
sha256sums=('31e8a121d38cf6386090cea7e96ac72b22ed41ceca2bdf0e7eb65f7741ab67b3')
b2sums=('e2c0b406e348ddb7fb445a5956127f3880858e9177a67a44005114c8fc36001c14f6e4c4a1b3cb4901c70f5b0e5ecbd0e9f63706a9405200e64e5057a64e6bb9')

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
