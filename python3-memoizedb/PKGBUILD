#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-memoizedb
pkgver=2016.5
pkgrel=1
pkgdesc='Generic data retrieval memoizer that uses an sqlite database to cache data.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-memoizedb"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2016.5.tar.xz
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2016.5.tar.xz.sig
)
sha512sums=(
  70ccffa3cd1e8ba860d5bba454e0cdc14fef37e70acdd5206bfb779451511d538c212ac2673c406506e1b96e13b9b1e5399b9035944915ffa8adb57b588a32a6
  0224e5d07c63e9b5d792cf9cf8a98a1fb4279d6a9ea9264995d3d243d3267d9f6b48da15225d36e8a962f7aec8f4a9fe2b1fd40f8fda5c6f070ed9a1b6987e5b
)
md5sums=(
  0b75602e730773588686b6ec749b069d
  36c0984f24839b5276883c511907dc49
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
