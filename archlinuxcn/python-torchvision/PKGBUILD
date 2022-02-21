# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Jean Lucas <jean@4ray.co>
# Based on python-torchvision-git; original contributors:
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.2;7.5;8.0;8.6;8.6+PTX"
pkgname=('python-torchvision' 'python-torchvision-cuda')
_pkgname=vision
pkgver=0.11.3
pkgrel=3
pkgdesc='Datasets, transforms, and models specific to computer vision'
arch=('x86_64')
url='https://github.com/pytorch/vision'
license=('BSD')
depends=(
  python-numpy
  python-pillow
  python-scipy
  python-six
  python-tqdm
)
optdepends=(
  'ffmpeg4.4: video reader backend (the recommended one with better performance)'
  'python-av: video reader backend (the default one)'
  'python-pycocotools: support for MS-COCO dataset'
)
makedepends=(
  cuda
  ffmpeg4.4
  python-av
  python-pytorch-cuda
  python-setuptools
  qt5-base
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/pytorch/vision/archive/v${pkgver}.tar.gz")
sha512sums=('4b712a52d5b72988277c9e9777b2b962cab1ce68edae0610b0fa44426d719e1ebf6dbdf78d0fda525b9f00f0b6ca8bb6d13fa43dfe6a3b46b29fd4a01606e2a1')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

prepare() {
  # fix building with ffmpeg4.4
  sed -i "s#ffmpeg_include_dir = os.path.join(ffmpeg_root, 'include')#ffmpeg_include_dir = os.path.join(ffmpeg_root, 'include', 'ffmpeg4.4')#" "${srcdir}/${_pkgname}-${pkgver}/setup.py"
  sed -i "s#ffmpeg_library_dir = os.path.join(ffmpeg_root, 'lib')#ffmpeg_library_dir = os.path.join(ffmpeg_root, 'lib', 'ffmpeg4.4')#" "${srcdir}/${_pkgname}-${pkgver}/setup.py"
  cp -a "${srcdir}/${_pkgname}-${pkgver}" "${srcdir}/${_pkgname}-cuda-${pkgver}"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
  
  cd "${srcdir}/${_pkgname}-cuda-${pkgver}"
  FORCE_CUDA=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py build
}

package_python-torchvision() {
  depends+=(python-pytorch)

  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_python-torchvision-cuda() {
  pkgdesc='Datasets, transforms, and models specific to computer vision (with GPU support)'
  depends+=(python-pytorch-cuda)
  provides+=(python-torchvision=${pkgver})
  conflicts+=(python-torchvision=${pkgver})
  
  cd "${_pkgname}-cuda-${pkgver}"
  FORCE_CUDA=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
