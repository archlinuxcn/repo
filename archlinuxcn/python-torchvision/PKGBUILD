# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Jean Lucas <jean@4ray.co>
# Based on python-torchvision-git; original contributors:
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX;8.0;8.0+PTX;8.6;8.6+PTX"
pkgname=('python-torchvision' 'python-torchvision-cuda')
_pkgname=vision
pkgver=0.8.2
pkgrel=1
pkgdesc='Datasets, transforms, and models specific to computer vision'
arch=('x86_64')
url='https://github.com/pytorch/vision'
license=('BSD')
depends=(
  'python-numpy'
  'python-pillow'
  'python-scipy'
  'python-six'
  'python-tqdm'
)
optdepends=(
  'ffmpeg: video reader backend (the recommended one with better performance)'
  'python-av: video reader backend (the default one)'
  'python-pycocotools: support for MS-COCO dataset'
)
makedepends=(
  'cuda'
  'ffmpeg'
  'python-av'
  'python-pytorch-cuda'
  'python-setuptools'
  'qt5-base'
)
checkdepends=(
  'python-mock'
  'python-pytest'
  'python-scipy'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/pytorch/vision/archive/v${pkgver}.tar.gz")
sha512sums=('81f7a6c90eab77fddbaef49506c1323e1d2e18e3b61612d21881c1684c35ebccc0bcad6480f9ebf4a57861d984ff3bf2598bdb4cf9c3128637875d4edb27d904')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

prepare() {
  cp -a "${srcdir}/${_pkgname}-${pkgver}" "${srcdir}/${_pkgname}-cuda-${pkgver}"
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
  
  cd "${srcdir}/${_pkgname}-cuda-${pkgver}"
  FORCE_CUDA=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py build
}

check() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-$(get_pyver)" pytest -v
  
  cd "${srcdir}/${_pkgname}-cuda-${pkgver}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-$(get_pyver)" pytest -v
}

package_python-torchvision() {
  depends+=(python-pytorch)

  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_python-torchvision-cuda() {
  pkgdesc='Datasets, transforms, and models specific to computer vision (with GPU support)'
  depends+=(python-pytorch-cuda)
  provides+=(python-torchvision=${pkgver})
  conflicts+=(python-torchvision=${pkgver})
  
  cd "${srcdir}/${_pkgname}-cuda-${pkgver}"
  FORCE_CUDA=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
