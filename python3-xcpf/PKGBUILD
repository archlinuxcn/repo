#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2015.10.21
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(python3 pyalpm)
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.10.21.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.10.21.tar.xz.sig
)
sha512sums=(
  735871c8f6821a63af3b87eeaf7a3e3b184172aef66712af8134ed52396cabcd24c140267f00f7474733a6ce2397ab5b66de76a89964c1244297b8e9fce17e54
  702c377629749ba8081fbee21794609bef867db2f7ba18712c0e5af5d403096a9499dba2b3c6c1ef9c6650d773a1aac2c7eab8d56948803d07d2c4eecc0bacd2
)
md5sums=(
  d7b9c51bb6534b6adbd2d57e362431a2
  56102edc1b67552df917c3829557c6d5
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
