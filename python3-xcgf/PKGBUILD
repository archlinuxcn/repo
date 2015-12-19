#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2015.12.19
pkgrel=1
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcgf"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2015.12.19.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2015.12.19.tar.xz.sig
)
sha512sums=(
  9e78da6fdc4b2781a790f0587679e77ffb20a0ed7210d5f6384a00b636ae2d146e15707b93cb3c81aaeaa515abf80a68df6162b51881a770b9fba460d8a1c911
  2f88e5fe4bee230dcd291e67aaddfb19507ab704198cddb98612fcb0c96e9e2d2d748a512c3f76a233b3dc715d8c8a08da003a41a3956d1dbf6b80ca148a3cb0
)
md5sums=(
  69e427bbff70b3630aaa8afed644bdd8
  b6b8b144356639b0f6bd5ed7baf5466d
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
