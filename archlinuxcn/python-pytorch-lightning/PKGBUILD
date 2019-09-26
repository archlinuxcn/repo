# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=0.5.0
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
source=("https://github.com/williamFalcon/pytorch-lightning/archive/${pkgver}.tar.gz")
sha512sums=('df76b72bb2443ac793286854c70ce26eaacfb125fe6f711ab2bd43f7bba062ae881e84be4976e8b9049edfb8dcbd4ccd2d404a97de5bfedcfbbab607a2c125ec')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
# remove conflict tests folder
  rm -rfv "${pkgdir}/usr/lib/python3.7/site-packages/tests"
}
# vim:set ts=2 sw=2 et:
