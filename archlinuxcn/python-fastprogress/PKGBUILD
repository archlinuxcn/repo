# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-fastprogress
_pkgname=fastprogress
pkgver=0.2.3
pkgrel=2
pkgdesc='Simple and flexible progress bar for Jupyter Notebook and console'
arch=('any')
url='https://github.com/fastai/fastprogress'
license=('Apache')
makedepends=(
  'python-setuptools'
)
source=("${pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('cc518bc8670f7a68fb06456a17adff8b244d77af9549cbdec6cc9dd71e595a29b51f8efca23d46ca6429e20a4ef74bdc5cbf27820ab4bbc7f6c90c8c9c959c5e')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
