# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=python-dict2xml
pkgver=1.7.5
pkgrel=2
pkgdesc="Small utility to convert a python dictionary into an XML string"
arch=('any')
url="https://github.com/delfick/python-dict2xml"
license=('MIT')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-hatchling')
checkdepends=('python-pytest' 'python-noseofyeti')
source=("https://github.com/delfick/python-dict2xml/archive/release-$pkgver/$pkgname-$pkgver.tar.gz")
sha512sums=('17b022e12dd50171eb06f1300c01ccde3b8017f156cf7bc4f0a8dabfa54e36c015daec7301019c480925666518d100bef43fff27b41a3539613f8922ee6c99bd')

build() {
  cd python-dict2xml-release-$pkgver
  python -m build -nw
}

check() {
  cd python-dict2xml-release-$pkgver
  pytest
}

package() {
  cd python-dict2xml-release-$pkgver
  python -m installer -d "$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
