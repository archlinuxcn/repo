# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=0.4.9
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
sha512sums=('a0da0b32ba9e89e1b0ecf81789f416719180f1f867d5f341af222f63bfdc9d968b13529e200567c4271362373d56f18733e5526bd752f28dbf9a57d5afafea41')

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
