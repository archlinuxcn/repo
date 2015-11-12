#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2015.11.12
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(python3 pyalpm)
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.11.12.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.11.12.tar.xz.sig
)
sha512sums=(
  1c09f7b4e12ecf013998d3f1e438768ebbbfccf45c96e3769d323992060790bf6abd26e8d4260bbe44b975b5b63501e917675c627484ddabd59fd10fdc670687
  ee873ea8b0ffa5d55510814a0e1e70237e590391acf185d0a76b11cda8fba741a483637d69bd08a64142eea2e86d7e55540c31b7697dd55e945629a82dba2ea0
)
md5sums=(
  515ecea0cf1715c8c75b42ccc03e4642
  835dbd24252da19a72b3036c3315fe29
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
