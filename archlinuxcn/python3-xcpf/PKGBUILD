#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2019.11
pkgrel=3
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2019.11.tar.xz
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2019.11.tar.xz.sig
)
sha512sums=(
  fd317f86d07f4832647a8bc4556e168b821dcdd99f516dc0f7f5dd8ab1e8988cc262dc1937d0d2e99500557840e9125bf62b5116e572c2742b14bb82d1c1d7fa
  0c2fc177c0be71653d804a83b508fb7e2cce651a4ad75a3ed623fe969faa7c2d6758dafb9803e6c6c6e4e16e5ee080d3c85b95f70033cccab2d065de6d1639aa
)
md5sums=(
  a949d2b16b0373990d09d529afdc8565
  52a458bc72a5b9b9189430017a8d793e
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
