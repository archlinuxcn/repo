# Contributor: Maikel Wever <maikelwever@gmail.com>
# Contributor: Matthew Gamble <git@matthewgamble.net>

pkgname=python-humanfriendly
pkgver=10.0
pkgrel=2
pkgdesc="Human friendly input/output in Python"
arch=('any')
url="https://github.com/xolox/python-humanfriendly"
license=('MIT')
depends=('python')
makedepends=('python-setuptools' 'python-sphinx')
source=("https://github.com/xolox/python-humanfriendly/archive/${pkgver}.tar.gz")
sha256sums=('a7f6ee6aa93933ffdf716a44163a8b1d17e8c95b3badb25efa37d562b2b93393')

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
