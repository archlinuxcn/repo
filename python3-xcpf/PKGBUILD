#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2016.11
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2016.11.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2016.11.tar.xz.sig
)
sha512sums=(
  648e78cef6022c959f45089175948ba5f26585b54dd6639a361478cf3c973530bd9c3295dba7f8b18de17a706aac82968b8f68185df3f5f80e64b51b9a67c145
  4e01f8e8a7c27cd5273598bf0e5420f6db363d1f8dc748f7da35a2e2f351e6f833182e1736f8a98a2112d60ac00039df488c9fe405c3ba3a33817b445e5d0ddd
)
md5sums=(
  de1b5ef68b37e4145a7d030ada219538
  96c43fb14277f27db2513b64459a5b3d
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
