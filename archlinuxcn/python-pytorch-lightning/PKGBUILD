# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=0.5.1.3
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
sha512sums=('d037953a343f914273ec136ef08c75a02890275034a07d57da4ef14ee28c3efbeb7c10f686e4bca2cb34860a59dcf5cf7687f541a2ab29c2004a475eaa251e00')

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
