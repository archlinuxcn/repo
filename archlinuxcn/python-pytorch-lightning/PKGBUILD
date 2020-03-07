# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_name=${pkgname#python-}
_pkgname=pytorch-lightning
pkgver=0.7.1
pkgrel=1
pkgdesc="Rapid research framework for PyTorch. The researcher's version of Keras"
arch=('any')
url='https://github.com/williamFalcon/pytorch-lightning'
license=('Apache')
depends=(
  'python-pandas'
  'python-numpy'
  'python-scikit-learn'
  'python-pytorch'
  'python-torchvision'
  'python-twine'
  'python-tqdm'
)
optdepends=(
  'python-apex: mixed precision support'    
)
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('6778121d4bbc6eaa5686197128194bf1c5a236586d9c4f18d5a133b2f4c225c86833badca2056e5b6493ad440397d49dd2df6fdd1fcfbc1451613f218a6a8009')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
