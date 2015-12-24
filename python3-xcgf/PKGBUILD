#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2015.12.23
pkgrel=1
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcgf"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2015.12.23.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2015.12.23.tar.xz.sig
)
sha512sums=(
  740a1f2b5be32ad9ab6ad6a0985c87aa4d59765bc9502ed22c0efcd17fe3dc73aa883456b79c1807d82addc612076b653f8c53c052b9f6d269fbf3dec4522855
  658507c2c0eae596c605877eb73c40bd088e3885f1dae92dad78ada520a62ce548f5a3e11b84e848f99ae0137a38325f3d087b78cdfc1aea6ba50e814da3be90
)
md5sums=(
  b25af661bd235373373bdfe7349bfcd9
  ab549099ea40544d04de2c10227bce3b
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
