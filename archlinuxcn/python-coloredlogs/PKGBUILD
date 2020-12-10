# Maintainer: Maikel Wever <maikelwever@gmail.com>
pkgname=python-coloredlogs
pkgver=15.0
pkgrel=1
pkgdesc="Colored terminal output for Python's logging module"
url="https://github.com/xolox/python-coloredlogs"
license=('MIT')
depends=('python' 'python-humanfriendly')
makedepends=('python-setuptools')
source=("https://github.com/xolox/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('1999ab887e0bf410921c85ade47c1317')
arch=('any')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  mkdir -p ${pkgdir}/usr/share/licenses/${pkgname}
  cp LICENSE.txt ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt
}

# vim:set ts=2 sw=2 et:
