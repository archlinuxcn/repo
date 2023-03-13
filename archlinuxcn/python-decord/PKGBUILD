# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=decord
pkgname=('python-decord' 'python-decord-cuda')
pkgver=0.6.0
pkgrel=4
pkgdesc="An efficient video loader for deep learning with smart shuffling that's super easy to digest"
arch=('x86_64')
url='https://github.com/dmlc/decord'
license=('Apache')
depends=(
  ffmpeg
  libavcodec.so
  libavfilter.so
  libavformat.so
  libavutil.so
  libswresample.so
  python-numpy
)
makedepends=(
  chrpath
  cmake
  cuda
  cython
  git
  python-setuptools
)
source=("${_pkgname}-${pkgver}::git+https://github.com/dmlc/decord.git#tag=v${pkgver}")
sha512sums=('SKIP')

prepare() {
  cd "${_pkgname}-${pkgver}"
  git submodule update --init --recursive
  # fix building with ffmpeg
  sed -i "21i#include <libavcodec/bsf.h>" "src/video/ffmpeg/ffmpeg_common.h"
  # fix const pointer convert issue
  sed -i "s,AVCodec \*dec,const AVCodec \*dec," "src/video/video_reader.cc"
  sed -i "165s,fmt_ctx_,(AVInputFormat\*)fmt_ctx_," "src/video/video_reader.cc"
  cp -a "${srcdir}/${_pkgname}-${pkgver}" "${srcdir}/${_pkgname}-cuda-${pkgver}"
}

build() {
  # building without CUDA
  cmake -B "${srcdir}/${_pkgname}-${pkgver}/build" -S "${srcdir}/${_pkgname}-${pkgver}" \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DUSE_CUDA:BOOL=OFF
  make -C "${srcdir}/${_pkgname}-${pkgver}/build"
  cd "${srcdir}/${_pkgname}-${pkgver}/python"
  python setup.py build

  # building with CUDA
  cmake -B "${srcdir}/${_pkgname}-cuda-${pkgver}/build" -S "${srcdir}/${_pkgname}-cuda-${pkgver}" \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DUSE_CUDA:BOOL=ON
  make -C "${srcdir}/${_pkgname}-cuda-${pkgver}/build"
  cd "${srcdir}/${_pkgname}-cuda-${pkgver}/python"
  python setup.py build
}

package_python-decord() {
  cd "${srcdir}/${_pkgname}-${pkgver}/python"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  mv -vf "${pkgdir}/usr/${_pkgname}/libdecord.so" "${pkgdir}/usr/lib"
  rm -rf "${pkgdir}/usr/${_pkgname}"
}

package_python-decord-cuda() {
  pkgdesc="${pkgdesc} (with CUDA)"
  depends+=(cuda libcudart.so)
  provides=(python-decord=${pkgver})
  conflicts=(python-decord)

  cd "${srcdir}/${_pkgname}-cuda-${pkgver}/python"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  mv -vf "${pkgdir}/usr/${_pkgname}/libdecord.so" "${pkgdir}/usr/lib"
  chrpath --delete "${pkgdir}/usr/lib/libdecord.so"
  rm -rf "${pkgdir}/usr/${_pkgname}"
}
# vim:set ts=2 sw=2 et:
