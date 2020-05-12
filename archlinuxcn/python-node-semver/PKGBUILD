# Maintainer: Tomislav Ivek <tomislav.ivek@gmail.com>

pkgname=('python-node-semver')
pkgver=0.8.0
pkgrel=1
pkgdesc="python version of node-semver"
arch=('any')
url="https://github.com/podhmo/python-semver"
license=('MIT')
depends=()
makedepends=('python-setuptools' 'fakeroot')
source=(https://github.com/podhmo/python-semver/archive/$pkgver.tar.gz)
sha512sums=('665ae0dbced16e0f05306614b1577464aa1bdac666b35cf2e7ad4b8844a6814dc7e8672f0dff3043c7bd048aa455d671efd268052ac59166293b91d1dff17784')

build() {
  cd "$srcdir/python-semver-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/python-semver-$pkgver"
  python setup.py install --optimize=1 --root=${pkgdir}
  # install -m755 -d "${pkgdir}/usr/share/licenses/$pkgname"
  # install -m644 LICENSE "${pkgdir}/usr/share/licenses/$pkgname/"
}
