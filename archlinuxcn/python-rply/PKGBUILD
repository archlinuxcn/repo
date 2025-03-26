# Maintainer: DrRac27 <drrac27 at riseup dot net>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=python-rply
pkgver=0.7.8
pkgrel=4
pkgdesc="A pure Python Lex/Yacc that works with RPython"
arch=('any')
license=('BSD')
url="https://rply.readthedocs.org"
makedepends=('python-setuptools' 'python-appdirs')
checkdepends=('python-pytest')
source=(
  "$pkgname-$pkgver.tar.gz::https://github.com/alex/rply/archive/v$pkgver.tar.gz"
  '0001-replace-py-with-pytest.patch'
)
sha512sums=(
  'b43e6425f046561cfca616801d37d7151f015aeb2ea2365abc00f97fd6b41f1a01a17e330aed5a81537065e4b29d49cd0824b5a5cb8b2d11da2ff1f8de952fce'
  'f22b2e300a43f44755668a3984525639968347f3bcb0c220829590af4da7eca4877230ec27b844dab6da27655ab75fe867ce04a8b67822d5a9b3a4c3cafcd537'
)

prepare() {
  cd "$srcdir"
  patch -p1 -d rply-$pkgver < '0001-replace-py-with-pytest.patch'
}

build() {
  cd "$srcdir"/rply-$pkgver
  python setup.py build
}

check() {
  cd "$srcdir"/rply-$pkgver
  pytest
}

package() {
  depends=('python-appdirs')

  cd rply-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1
  install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
