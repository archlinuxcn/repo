# Maintainer: Felix Golatofski <contact@xdfr.de>
# Contributor: Bumsik Kim <k.bumsik@gmail.com>
# Contributor: KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Scripts inspired by nushell-git package

_pkgname=nu
pkgname=${_pkgname}shell
pkgver=0.20.0
pkgrel=1
pkgdesc="A new type of shell."
url="https://www.nushell.sh"
license=('MIT')
makedepends=('rust')
depends=('openssl')
optdepends=('libxcb' 'libx11')
arch=('x86_64' 'i686')
source=("https://github.com/nushell/nushell/archive/$pkgver.tar.gz")
# Use updpkgsums to update the checksum
sha256sums=('ccecbfd49d03ca45f347fe55b789b8732003ceab49a14af110390e723f2fd274')
b2sums=('3d8fcccc0c353ab7c98a4ad5c3485cd74950d96c481cb6b855e8d5f549b3622d28d1e32f087eb6f620f83f1b7160d25efe80255694cad79b23ad5c2585c5678a')

package() {
  install=nushell.install

  cd "$srcdir/$pkgname-$pkgver"

  cargo install \
    --locked \
    --path . \
    --features stable \
    --root "${pkgdir}"/usr

  rm -f "${pkgdir}"/usr/.crate*
}
