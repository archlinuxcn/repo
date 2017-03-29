#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-memoizedb
pkgver=2017.3.29
pkgrel=1
pkgdesc='Generic data retrieval memoizer that uses an sqlite database to cache data.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-memoizedb"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2017.3.29.tar.xz
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2017.3.29.tar.xz.sig
)
sha512sums=(
  4a3385751b39dff34e4023ec937dd137f652469fb90c90054432eef7c0eae06380a5c5df0c1c87702c6b82eab623d5f0ebdcee6f996bdb8800964dcc1b9af2a3
  d2ad11a38a27aa256c90aae8999cc30dcc96c651433ae89a06e5ed2b63d1f54f43878f140d5405cb38a70df75ca5573967438362f80865b18f7c79c63e3c0348
)
md5sums=(
  6a086768fd32de7cb21b414b8167c1b6
  ff224f9402bdd5ac0f7fb8aae9825917
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
