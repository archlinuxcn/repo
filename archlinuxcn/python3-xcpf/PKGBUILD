#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2019
pkgrel=2
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2019.tar.xz
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2019.tar.xz.sig
)
sha512sums=(
  e6ead2b1c516f4734d9de6678b2455f81ef7c4f978707609c906eb18ad8d3341e4119e2c0ec980bbb0a301be4e5cc55b39d9e222c7c753bc26727967d03ab1f9
  cdab61ed652d805d915ffba5d7fb88e4ab4be2efd2f03c0f8ec0c7fd5c38caec98e193e61e6963068ef2015481527ede077620464a541f2530430ba42087b89b
)
md5sums=(
  973f4a0701ffc466f744c3335f55e0a0
  c93be8c5b7899b8d40038f1c310afbd5
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
