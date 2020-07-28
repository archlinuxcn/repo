# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-fastprogress
_pkgname=fastprogress
pkgver=0.2.4
pkgrel=1
pkgdesc='Simple and flexible progress bar for Jupyter Notebook and console'
arch=('any')
url='https://github.com/fastai/fastprogress'
license=('Apache')
makedepends=(
  'python-setuptools'
)
source=("${pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('97e6ccc49b9c8360738b77259f2900eb105eadcce1ff2b1bc82d5f06d96901f93a70e274f002bfaefd245e41db497d992a1e4112ea5b8f55d81b6271305a7cd3')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
