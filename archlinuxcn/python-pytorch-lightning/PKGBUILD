# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_name=${pkgname#python-}
_pkgname=pytorch-lightning
pkgver=0.6.0
pkgrel=2
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
sha512sums=('cffbf44992e283402e2ebdfc2a64c6a6a68573645fd004bd70eb0a4f68f3aa56eb7369e04e3a57aae4192618f9296094cf7600e5addcbb04c96b869e82505d19')

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
