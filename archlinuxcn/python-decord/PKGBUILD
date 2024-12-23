# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=decord
pkgname=('python-decord' 'python-decord-cuda')
pkgver=0.6.0
pkgrel=9
pkgdesc="An efficient video loader for deep learning with smart shuffling that's super easy to digest"
arch=('x86_64')
url='https://github.com/dmlc/decord'
license=('Apache-2.0')
depends=(
  ffmpeg6.1
  glibc
  gcc-libs
  python-numpy
)
makedepends=(
  chrpath
  cmake
  cuda
  cython
  git
  nvidia-utils
  python-build
  python-installer
  python-setuptools
  python-wheel
  chrpath
)
source=("${_pkgname}-${pkgver}::git+https://github.com/dmlc/decord.git#tag=v${pkgver}"
        "0002-fix-building-with-ffmpeg.patch"
)
sha512sums=('f91944e7931f18576cdedd69edc9f651189db2dbc63e7f211cb894cea71bc9df0f4f83ef27f2449da4c9cf13517c310ed0ef6bdd01d01f48258e0f7bf3efa027'
            'b5d01e3666ce961276100eeea779333ab440a169f0de23c4382e88436a362a1c732eb5e99137701f689cbbde13a14fec9118195e22a58253c3a8bc595aab54af')

prepare() {
  cd "${_pkgname}-${pkgver}"
  git submodule update --init --recursive
  # fix building with ffmpeg 6
  patch -p1 -i ${srcdir}/0002-fix-building-with-ffmpeg.patch
  cp -a "${srcdir}/${_pkgname}-${pkgver}" "${srcdir}/${_pkgname}-cuda-${pkgver}"
}

build() {
  # building without CUDA
  cmake \
    -B "${srcdir}/${_pkgname}-${pkgver}/build" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DFFMPEG_INCLUDE_DIR=/usr/include/ffmpeg6.1 \
    -DFFMPEG_LIBRARIES="/usr/lib/ffmpeg6.1/libavformat.so;/usr/lib/ffmpeg6.1/libavfilter.so;/usr/lib/ffmpeg6.1/libavcodec.so;/usr/lib/ffmpeg6.1/libavutil.so;/usr/lib/ffmpeg6.1/libavdevice.so;/usr/lib/ffmpeg6.1/libswresample.so" \
    -DUSE_CUDA=OFF \
    -S "${srcdir}/${_pkgname}-${pkgver}"
  make -C "${srcdir}/${_pkgname}-${pkgver}/build" VERBOSE=1
  cd "${srcdir}/${_pkgname}-${pkgver}/python"
  python -m build --wheel --no-isolation

  # building with CUDA
  cmake \
    -B "${srcdir}/${_pkgname}-cuda-${pkgver}/build" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DFFMPEG_INCLUDE_DIR=/usr/include/ffmpeg6.1 \
    -DFFMPEG_LIBRARIES="/usr/lib/ffmpeg6.1/libavformat.so;/usr/lib/ffmpeg6.1/libavfilter.so;/usr/lib/ffmpeg6.1/libavcodec.so;/usr/lib/ffmpeg6.1/libavutil.so;/usr/lib/ffmpeg6.1/libavdevice.so;/usr/lib/ffmpeg6.1/libswresample.so" \
    -DUSE_CUDA=ON \
    -S "${srcdir}/${_pkgname}-cuda-${pkgver}"
  make -C "${srcdir}/${_pkgname}-cuda-${pkgver}/build" VERBOSE=1
  cd "${srcdir}/${_pkgname}-cuda-${pkgver}/python"
  python -m build --wheel --no-isolation
}

package_python-decord() {
  cd "${srcdir}/${_pkgname}-${pkgver}/python"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-decord-cuda() {
  pkgdesc="${pkgdesc} (with CUDA)"
  depends+=(
    cuda
    libcudart.so
    nvidia-utils
  )
  provides=(python-decord=${pkgver})
  conflicts=(python-decord)

  cd "${srcdir}/${_pkgname}-cuda-${pkgver}/python"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  find ${pkgdir} -type f -name "*.so" -exec chrpath --delete {} \;
}
# vim:set ts=2 sw=2 et:
