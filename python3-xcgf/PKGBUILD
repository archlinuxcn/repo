#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2016.4.26
pkgrel=1
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcgf"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2016.4.26.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2016.4.26.tar.xz.sig
)
sha512sums=(
  272c78ad24f00b6f3b42059b06488e34f78d438c307a17b6ff0293e5257f3c1f35eb08f414aa4ac5facd958ee090535d817beea0e3c46258c0a194c4ea51e6e3
  acb915ec5d3ec7a12f4ad7ad8d8858d1cde3de8e22ce616b8953fe33ba3390b59eebae04f401f2d06078c0531ba3df349acd0ca03dcbc8a2837f08772d020763
)
md5sums=(
  a7867d3651ba09812286915a1a5425d1
  44939d706905a54d2fff35d8efcc9efc
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
