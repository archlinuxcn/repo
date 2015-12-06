#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2015.12.6
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python3)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.12.6.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.12.6.tar.xz.sig
)
sha512sums=(
  34fb2d53c32c3b59c137054b4077c25ca6b83d6cab4f183a255f512d08290ce1cc825cb951b421a9ee59cf7eed3e47a32b629e151dbc5e5b2b0dd4bf4fa8b770
  4604f3807f13efde560c0ecaa507ffdc44070359ceeac23ff8dc1c32f56bc4fc23560a7e68bf94fcd58ecb0364f641227cf5231959cec73079803c2f562d5179
)
md5sums=(
  67818b9e3f7a1b989861a2ee89688fbb
  2d4316b644048e69bfce073cb5e36f17
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
