# Maintainer: Hexchain Tong <i at hexchain dot org>
pkgname=neovim-remote
pkgver=2.4.0
pkgrel=2
pkgdesc="Support --remote and friends for Neovim"
arch=(any)
url="https://github.com/mhinz/neovim-remote"
license=('MIT')
depends=('python-pynvim' 'python-psutil')
makedepends=('git' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/mhinz/neovim-remote/archive/v$pkgver.tar.gz")
sha256sums=('4213b6eaad638aa20d8687362764843beb626e6e1a03bc3c8b3399bbfc11fbf7')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --optimize=1 --root="$pkgdir/" --prefix=/usr --skip-build
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}

# vim:set ts=2 sw=2 et:
