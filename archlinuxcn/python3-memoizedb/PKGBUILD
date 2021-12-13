#Maintainer: Xyne <gro xunilhcra enyx, backwards>
pkgname=python3-memoizedb
pkgver=2021
pkgrel=2
pkgdesc='Generic data retrieval memoizer that uses an sqlite database to cache data.'
arch=(any)
license=(GPL)
url="https://xyne.dev/projects/python3-memoizedb"
depends=(python3)
source=(
  https://xyne.dev/projects/python3-memoizedb/src/python3-memoizedb-2021.tar.xz
  https://xyne.dev/projects/python3-memoizedb/src/python3-memoizedb-2021.tar.xz.sig
)
sha512sums=(
  33667aa062742bcc42410048b8c397031103aac144e863ad074d60e8169611d849a589e331407c26c49d9de4ebd9281978ef2d8b0ee058b4df1db8458f1c6aaf
  76e4b0e3a1c0653790368c3b387fa14fc2013283aebe0cabf1776f469f89a14661ac974ef324a2162ea16fc973ccd721ba2b9cc726c956eb1600b7b8ebfd5115
)
md5sums=(
  6c522e5b6aea2360a5e3cf4fe1dd05b6
  741ca0316c97fd44d200e3ce0707958d
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
