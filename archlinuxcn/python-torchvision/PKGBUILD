# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Jean Lucas <jean@4ray.co>
# Based on python-torchvision-git; original contributors:
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>

pkgname=python-torchvision
_pkgname=vision
pkgver=0.3.0
pkgrel=2
pkgdesc='Datasets, transforms, and models specific to computer vision'
arch=('x86_64')
url=https://github.com/pytorch/vision
license=(BSD)
depends=(python-numpy python-pillow python-pytorch python-scipy python-six python-tqdm)
makedepends=(python-setuptools)
checkdepends=(python-pytest python-scipy)
source=("https://github.com/pytorch/vision/archive/v${pkgver}.tar.gz")
sha512sums=('a402221827319c9792e7ff8edb8218737e09b8dade186a3b7adeb7501f2f60d030e0cc22e5b78163368056370daea4682da0748c72a736df0f4ee4443a8150fe')

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
