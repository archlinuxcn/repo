#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2015.12.7.1
pkgrel=1
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcgf"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2015.12.7.1.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2015.12.7.1.tar.xz.sig
)
sha512sums=(
  6782211c31980acafe847ac73511c3d54d45da687b98c4afb7cfecbf094df86947027b10c31347374de43b3c0feefbbd42c828e82f890cfd51c2e99f80f6d47c
  df25bef597712b6fa9a7b4a81d086a235c67d85b4d23e0fb27cec8573f3162094dc87cdd01fffa12b775b9fd58e4a678029d7ea65a175b914d19e1c8d199a12b
)
md5sums=(
  3a0fb9c095fe45ac33a734b9e05a9901
  b37a16c22a8e1ec0af83390a7f202c8a
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
