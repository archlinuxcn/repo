# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Jean Lucas <jean@4ray.co>
# Based on python-torchvision-git; original contributors:
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>

pkgname=python-torchvision
_pkgname=vision
pkgver=0.4.1
pkgrel=2
pkgdesc='Datasets, transforms, and models specific to computer vision'
arch=('x86_64')
url='https://github.com/pytorch/vision'
license=('BSD')
depends=(
  'python-av'
  'python-numpy'
  'python-pillow'
  'python-pytorch'
  'python-scipy'
  'python-six'
  'python-tqdm'
)
makedepends=(
  'python-setuptools'
  'qt5-base'
)
checkdepends=(
  'python-mock'
  'python-pytest'
  'python-scipy'
)
source=("https://github.com/pytorch/vision/archive/v${pkgver}.tar.gz")
sha512sums=('644087f2f2bfa2436b8485608ce5d9dd002d73352c8d2b333b434f3c835dcbe85fd927667ce641162dad51c5a011faf9aeaddc7a950af2a0b6912b64475cb5a8')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-3.7" pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
