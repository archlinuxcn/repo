# Maintainer: Hexchain Tong <i at hexchain dot org>
pkgname=neovim-remote
pkgver=2.1.7
pkgrel=1
pkgdesc="Support --remote and friends for Neovim"
arch=(any)
url="https://github.com/mhinz/neovim-remote"
license=('MIT')
depends=('python-neovim' 'python-psutil')
makedepends=('git' 'python-setuptools')
source=("https://github.com/mhinz/neovim-remote/archive/v$pkgver.tar.gz")
sha256sums=('f709237a84a42e494533d155da02551709056643bf0ca92ea0208f4e2ea7d272')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install -O1 --root="$pkgdir/"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}

# vim:set ts=2 sw=2 et:
