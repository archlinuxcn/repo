#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2015.12.4.3
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(python3 pyalpm)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.12.4.3.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.12.4.3.tar.xz.sig
)
sha512sums=(
  da1a00f3c5d46612b30b2e86b70b48ac72a396e8031a7fc6e6234d5f42cd3c28e7f4ab31185ee55f8e82b7e7668f567b32d2481287b3be969c59488dd63235c3
  15d67bee90392419a5d64ad94550e56dedd4b8c055e4d33dfd335a036c372a79118832c306be980ff1f1cd1678ce763750381d9145d0b69ed3c5ce9deedd4d07
)
md5sums=(
  c46dbcf619cacd221b7ed0b1685701d9
  7e001bfb6c84f3a6cca16824b28cfdef
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
