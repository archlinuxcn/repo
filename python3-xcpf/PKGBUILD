#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2017.2.10
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.2.10.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.2.10.tar.xz.sig
)
sha512sums=(
  a36095bbdc96bc371c33ae4cb4bd20e27b82c73a6a3e906e9aa449baf295f34823632823510f8319055e5763d2e09c4a5c2fb9f50439bf22992e3c5de52d6763
  0bcdaf3f33bcb66cc3f2cef3f67397e708138787232c64d01752ef8edeccd6e639f49526b54ab330a9bfea19cba8bf0bea777b0f6c4f2ff9e673e88d8a7d9d99
)
md5sums=(
  2be39ee167f2432f25fba6e884bfca63
  b9bb4719743701da856dbb6dfc3670f2
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
