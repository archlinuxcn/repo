#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-memoizedb
pkgver=2016.4.6
pkgrel=1
pkgdesc='Generic data retrieval memoizer that uses an sqlite database to cache data.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-memoizedb"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2016.4.6.tar.xz
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2016.4.6.tar.xz.sig
)
sha512sums=(
  02239b7f9af143fcd7dadea49f9a7fa2f029c8b072500ba0e8ee667a42cb0475af9c2275ea86383b61e5aa15a74f9605f93eb4ebbc5dd344125374d55973d59e
  17d13e6795f47626e6fd2d926412636a99ef0d6371f49dacdcba5ab523ffc5571a4904340ecd945cd621eefa198cc450dad850227f4284dca95e6c1a763bbc8e
)
md5sums=(
  02356d0d80900f290c77c9543a44719c
  6afabb6af7812a01dc44fad760563786
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
