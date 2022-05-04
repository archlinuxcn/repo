# Maintainer: Hexchain Tong <i at hexchain dot org>
pkgname=neovim-remote
pkgver=2.4.2
pkgrel=1
pkgdesc="Support --remote and friends for Neovim"
arch=(any)
url="https://github.com/mhinz/neovim-remote"
license=('MIT')
depends=('python-pynvim' 'python-psutil')
makedepends=('git' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/mhinz/neovim-remote/archive/v$pkgver.tar.gz")
sha256sums=('4bad60d5cc34dc18ef51494faa6afa9c390cb82042d4cc80ff62681a045a6481')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --optimize=1 --root="$pkgdir/" --prefix=/usr --skip-build
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 contrib/completion.bash "$pkgdir/usr/share/bash-completion/completions/neovim-remote"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname/"
}

# vim:set ts=2 sw=2 et:
