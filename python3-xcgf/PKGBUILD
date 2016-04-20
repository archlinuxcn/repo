#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2016.4.5
pkgrel=1
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcgf"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2016.4.5.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2016.4.5.tar.xz.sig
)
sha512sums=(
  bee42dc93632258fc5793544e927677dd8cc0cc58fd610aad73206f8f2cd62fb9879d8e1dc518994c114e9c8409b3444d5a77a0bb0885cbbe615fd33e8f61c72
  b5914b81b706a3a2b8516dc56da0d74e78f24d3a4c66059975c4e2d6a3c6b8e4e6a7c766102f472c296fec3880a77bab9ed8c437318b5354c2c09df0523da9b4
)
md5sums=(
  95e66ccdd3216adc51f84e7f1c43fcd1
  0ba3825192898462bf9136db4b37372a
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
