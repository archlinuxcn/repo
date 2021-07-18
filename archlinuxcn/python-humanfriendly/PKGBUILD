# Maintainer: Maikel Wever <maikelwever@gmail.com>
# Maintainer: Matthew Gamble <git@matthewgamble.net>

pkgname=python-humanfriendly
pkgver=9.2
pkgrel=1
pkgdesc="Human friendly input/output in Python"
arch=('any')
url="https://github.com/xolox/python-humanfriendly"
license=('MIT')
depends=('python')
makedepends=('python-setuptools' 'python-sphinx')
source=("https://github.com/xolox/python-humanfriendly/archive/${pkgver}.tar.gz")
sha256sums=('63b6ae2ca33e7e8f5c3ae80b2a86d4bdf4d80e113afe02f4f1bd38031144f649')

build() {
  cd "python-humanfriendly-${pkgver}"

  python setup.py build

  cd docs
  sphinx-build -nb html -d build/doctrees . build/html
}

package() {
  cd "python-humanfriendly-${pkgver}"

  PYTHONHASHSEED=0 python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-humanfriendly/LICENSE.txt"
  install -Dm644 CHANGELOG.rst "${pkgdir}/usr/share/doc/python-humanfriendly/CHANGELOG.rst"
  cp -r docs/build/html "${pkgdir}/usr/share/doc/python-humanfriendly/html"
}

# vim:set ts=2 sw=2 et:
