# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-tangled-up-in-unicode
_pkgname=tangled-up-in-unicode
pkgver=0.0.6
pkgrel=1
pkgdesc='Access to the Unicode Character Database (UCD)'
arch=('any')
url='https://github.com/dylan-profiler/tangled-up-in-unicode'
license=('BSD')
depends=(
  python
)
makedepends=(python-setuptools)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/dylan-profiler/tangled-up-in-unicode/archive/v${pkgver}.tar.gz")
sha512sums=('1e6e2251184ab02bf257c988bb499f2de59c451b41b1244454888bdab8d84e4379a07527c10be3421de9588632405da27e81adbbd4cd677ced3e272bf289ddd5')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
