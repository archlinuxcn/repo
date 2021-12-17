# Maintainer: Tomislav Ivek <tomislav.ivek@gmail.com>

pkgname=('python-node-semver')
pkgver=0.8.0
pkgrel=6
pkgdesc="python version of node-semver"
arch=('any')
url="https://github.com/podhmo/python-node-semver"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source=(python-node-semver.tar.gz::https://github.com/podhmo/python-node-semver/archive/$pkgver.tar.gz)
sha512sums=('ef6e7cac219a3170676d33af70b7f3d17798285ceea495345746489261987f0e41cfcd3d05ebc333477813404fd0b2028c037d71270fd01142d448bec672643b')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --optimize=1 --root=${pkgdir}
  install -D -m644 "$srcdir/$pkgname-$pkgver/LICENSE" "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
