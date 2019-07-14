# Maintainer: Hexchain Tong <i at hexchain dot org>
pkgname=neovim-remote
pkgver=2.1.9
pkgrel=1
pkgdesc="Support --remote and friends for Neovim"
arch=(any)
url="https://github.com/mhinz/neovim-remote"
license=('MIT')
depends=('python-neovim' 'python-psutil')
makedepends=('git' 'python-setuptools')
source=("https://github.com/mhinz/neovim-remote/archive/v$pkgver.tar.gz")
sha256sums=('25d9fe4f4c90a9b68d507d1c9f81411e00342c95517d19051c5dba3a42b703aa')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install -O1 --root="$pkgdir/"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}

# vim:set ts=2 sw=2 et:
