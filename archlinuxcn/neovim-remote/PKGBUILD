# Maintainer: Hexchain Tong <i at hexchain dot org>
pkgname=neovim-remote
pkgver=2.3.4
pkgrel=1
pkgdesc="Support --remote and friends for Neovim"
arch=(any)
url="https://github.com/mhinz/neovim-remote"
license=('MIT')
depends=('python-pynvim' 'python-psutil')
makedepends=('git' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/mhinz/neovim-remote/archive/v$pkgver.tar.gz")
sha256sums=('697f7c86efef102d7df582b55e918c129852aeea42939e9872b9f22d6185b010')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install -O1 --root="$pkgdir/"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}

# vim:set ts=2 sw=2 et:
