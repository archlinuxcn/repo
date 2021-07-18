# Maintainer:  KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Bumsik Kim <k.bumsik@gmail.com>

pkgname=nushell
pkgver=0.34.0
pkgrel=2
pkgdesc="A new type of shell."
url="https://www.nushell.sh"
license=('MIT')
depends=('openssl' 'libxcb' 'libgit2' 'zlib' 'libx11')
makedepends=('rust' 'python')
arch=('x86_64' 'i686' 'aarch64')
install=nushell.install
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/nushell/nushell/archive/${pkgver}.tar.gz")
cksums=('1554336555')
sha256sums=('9571c7fbf0f0fdabb055727b63b6a5c3561f04357336289106591fc6afcff7a3')
b2sums=('a83ca65512c90641714c969e17e6b1c3b79e1f52a26d2fd3c960a10e9b947185f0679f6ff03512e5c94268f8d5df475fe8b0598b3f20fc96eadfdcfc1fe5e4ca')

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
