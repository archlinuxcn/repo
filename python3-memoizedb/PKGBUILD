#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-memoizedb
pkgver=2015.12
pkgrel=1
pkgdesc='Generic data retrieval memoizer that uses an sqlite database to cache data.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-memoizedb"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2015.12.tar.xz
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2015.12.tar.xz.sig
)
sha512sums=(
  b8668f825b3da693d36e9ad88a8848954da8348c34e9562673ab0b3a5cac7cf79b9b0e5cb8b8f61b97f23460a93b20f60992d60d9158994d9337369c58d61ea3
  f755ebb88dc9ff23d918dd9db75858b43f4f966ffba2ac00cec39fb53c7c67ba256ea20ac0b8aeb5b26ea4092e67e61362afa609b8b6be3318528c58a8d812b6
)
md5sums=(
  51357b6bccb8edcd8fb089ec9447c879
  91efa9fcd6e04e9154fb03552cbd0d20
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
