# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_name=${pkgname#python-}
_pkgname=pytorch-lightning
pkgver=0.5.3.1
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
sha512sums=('fd7548d9fb2b45b5908f77f05d67173863c9c72c912ffefee2f8d14f42d240b9e3c2d1d60cc1a5211aef8592bc25ffc8aab3f52cfa597e0f551d166b94a425f2')

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
