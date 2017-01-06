#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-memoizedb
pkgver=2017
pkgrel=1
pkgdesc='Generic data retrieval memoizer that uses an sqlite database to cache data.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-memoizedb"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2017.tar.xz
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2017.tar.xz.sig
)
sha512sums=(
  886f49866a1754c4d62801ec21f9b3683e24173f14370d0038f4de0a862d43cb11c953c5413b5c75a5c2d805d52dab606b68531f0c07fba722447c4a7172bc9b
  e8b52c00303d54fe21d846230ce925751e0e0c1f542d0831ba51dfc336401fbb9e5c0e4fa8cff5c421edfb14b257efce86d6e8536314c97c3219b4469b810ad8
)
md5sums=(
  7eaed62ffd68d0bfc86ac17410f13d2a
  1c6d6f1afae3c238cc116213c078b7fa
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
