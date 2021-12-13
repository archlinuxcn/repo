#Maintainer: Xyne <gro xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2021.11
pkgrel=2
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.dev/projects/python3-xcpf"
depends=(pyalpm python-pyxdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.dev/projects/python3-xcpf/src/python3-xcpf-2021.11.tar.xz
  https://xyne.dev/projects/python3-xcpf/src/python3-xcpf-2021.11.tar.xz.sig
)
sha512sums=(
  a70158e18afc70e4e9adee7a26eada3e32a55f76de315a03657fd5336b739a29d709ca14569080f1efb7f177ab0071c288af8b5d686c2873ec8fd807ebf32dd0
  31e78f080c4788504b465bf75c99a81501310d0b2e45628e1c53c731b86a1757ebb7e83e393a3b5728eefdf7dd418b0fe5e3334d8f37bcfc91724cd8fd0a83c5
)
md5sums=(
  bcc4b951ac6e15dee7070c031421d571
  fc14c5e7c2e5e3885a9d6022eee3d9c2
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
