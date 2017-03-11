#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-memoizedb
pkgver=2017.3
pkgrel=1
pkgdesc='Generic data retrieval memoizer that uses an sqlite database to cache data.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-memoizedb"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2017.3.tar.xz
  http://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2017.3.tar.xz.sig
)
sha512sums=(
  906e0eed26cda5cafc302a577bdd2e2c56e4353b663be4012163122e2ffbd94918646b903a74c587aea97707eb17544198bf93ef701bc9df229bf9efca1e0d24
  8c807a9489931b72879c05d2e6275620ad2619d2f64c11d8aa1107e0baaff9301518e3f87421516e46b2a79ad608ad015b2d37f2bf1bc6afaafdd35f47e74e6f
)
md5sums=(
  dd86dcf32da6e32715771c214980ec80
  b0f87314d3aec6a7bf054b84e54dd19e
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
