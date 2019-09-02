# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=0.4.8
pkgrel=3
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
sha512sums=('98ddff3fe06d31ecc98277efbdcb5dfaf1d6162cc06896e79fdbe0be7806c45f0af20cc30417e3f703584048412f210f2d7e0ff4f9ac8acdbc274a6eb800414e')

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
