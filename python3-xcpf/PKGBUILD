#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2015.11
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(python3 pyalpm)
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.11.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.11.tar.xz.sig
)
sha512sums=(
  3165c36a9b1c343250e979a1ae50aff8755df1b1b3aed518cf6b07b6c7ffbba9c76c98dbd339988c5dc6f91f0c6ebb6cb72ab5bc118147cf4088aeefef380719
  840e27dfc583e6701ebd4f7de42449272e0f955e3579958197e8238b160a2d1d00abd7b9ab66f0a4734de83d4c79c57aa49f5714fae772412d639337945b4299
)
md5sums=(
  487bfb371aed8e6e8d8147c060c27d16
  d52f9c335a07d3385108243dc729b96c
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
