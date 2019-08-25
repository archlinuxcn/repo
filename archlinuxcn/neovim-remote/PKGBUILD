# Maintainer: Hexchain Tong <i at hexchain dot org>
pkgname=neovim-remote
pkgver=2.2.0
pkgrel=1
pkgdesc="Support --remote and friends for Neovim"
arch=(any)
url="https://github.com/mhinz/neovim-remote"
license=('MIT')
depends=('python-neovim' 'python-psutil')
makedepends=('git' 'python-setuptools')
source=("https://github.com/mhinz/neovim-remote/archive/v$pkgver.tar.gz")
sha256sums=('e9b0075e882bab750643f0066fe70dd7720b7b44db180a1626b6ab73bc9e79a0')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install -O1 --root="$pkgdir/"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}

# vim:set ts=2 sw=2 et:
