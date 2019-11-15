#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-memoizedb
pkgver=2017.3.30
pkgrel=4
pkgdesc='Generic data retrieval memoizer that uses an sqlite database to cache data.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-memoizedb"
depends=(python3)
source=(
  https://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2017.3.30.tar.xz
  https://xyne.archlinux.ca/projects/python3-memoizedb/src/python3-memoizedb-2017.3.30.tar.xz.sig
)
sha512sums=(
  fb3df141b381842494ca9692e2eb57c58f75c5f075be618e33064da30b4fc800ef8aad97a184cbc26a1f79ce08e5b116f7e70251296ed93a4ec90a77f79ef48f
  18e68b86ec64634a3085c5a2e4686a63f9026b1484085b1172b8efca6dc6bd94ae5174d74b3c38872ba93f0a48f77f40a29cf4080b811be91e8d842637872c65
)
md5sums=(
  22be1c358596a97a372c17f8a23c705a
  59a528054ab250cc431b1b9332ce3874
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
