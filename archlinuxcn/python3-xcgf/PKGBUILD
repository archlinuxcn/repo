#Maintainer: Xyne <gro xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2021
pkgrel=2
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.dev/projects/python3-xcgf"
depends=(python3)
source=(
  https://xyne.dev/projects/python3-xcgf/src/python3-xcgf-2021.tar.xz
  https://xyne.dev/projects/python3-xcgf/src/python3-xcgf-2021.tar.xz.sig
)
sha512sums=(
  a42a45cdfcb5b65a866be13c0bad06b2f6b251d5bfe9353f045e8eed87850129a949708aec6ae470117a22dbd290552f4d046ecbfa960f8f9f56fbbad38bc081
  3f26e6d2b6bdab2af8315e998ed2beab682f4d0373f2da884fb255017ef6eec278fdee96079b9a228319db5019cb30f5982d5502afbcc716a4ed13be8a9eb4cf
)
md5sums=(
  61ff53d3820358dfbadb3e146024636a
  b9985f601fca6a93ce928e7bb464e9eb
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
