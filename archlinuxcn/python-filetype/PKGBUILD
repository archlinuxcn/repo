# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=python-filetype
pkgver=1.2.0
pkgrel=3
pkgdesc="Infer file type and MIME type of any file/buffer"
url="https://github.com/h2non/filetype.py"
license=('MIT')
arch=('any')
depends=('python')
makedepends=('python-setuptools')
source=("https://github.com/h2non/filetype.py/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
sha512sums=('e6116dd5505c01803c29016a8e85ce3f126c998f882eb1cfa8ff67990f560fee486d06b27dc64dbd74490f5d0f0327a9af0074e9cf1e16d3d55e71eeb2575c75')

build() {
  cd filetype.py-$pkgver
  python setup.py build
}

check() {
  cd filetype.py-$pkgver
  python -m unittest discover
}

package() {
  cd filetype.py-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
