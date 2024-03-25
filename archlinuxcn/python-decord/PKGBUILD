# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=decord
pkgname=('python-decord' 'python-decord-cuda')
pkgver=0.6.0
pkgrel=6
pkgdesc="An efficient video loader for deep learning with smart shuffling that's super easy to digest"
arch=('x86_64')
url='https://github.com/dmlc/decord'
license=('Apache-2.0')
depends=(
  ffmpeg4.4
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
  python-build
  python-installer
  python-setuptools
  python-wheel
  chrpath
)
source=("${_pkgname}-${pkgver}::git+https://github.com/dmlc/decord.git#tag=v${pkgver}"
        "0001-fix-building-with-ffmpeg4.4.patch"
)
sha512sums=('SKIP'
            'e4b8450ee48583b40f99bf9c981e1f37529c16ba002f6781187621fb6b94d3856db34e90c4c1fd88978601deb88d1e0d31f161232882651c6c6cd61dd91da45a')

prepare() {
  cd "${_pkgname}-${pkgver}"
  git submodule update --init --recursive
  # fix building with ffmpeg4.4
  patch -p1 -i ${srcdir}/0001-fix-building-with-ffmpeg4.4.patch
  cp -a "${srcdir}/${_pkgname}-${pkgver}" "${srcdir}/${_pkgname}-cuda-${pkgver}"
}

build() {
  # building without CUDA
  cmake \
    -B "${srcdir}/${_pkgname}-${pkgver}/build" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DFFMPEG_DIR=/usr \
    -DUSE_CUDA=OFF \
    -S "${srcdir}/${_pkgname}-${pkgver}"
  make -C "${srcdir}/${_pkgname}-${pkgver}/build" VERBOSE=1
  cd "${srcdir}/${_pkgname}-${pkgver}/python"
  python -m build --wheel --no-isolation

  # building with CUDA
  cmake \
    -B "${srcdir}/${_pkgname}-cuda-${pkgver}/build" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_CXX_COMPILER=/opt/cuda/bin/g++ \
    -DCMAKE_C_COMPILER=/opt/cuda/bin/gcc \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DFFMPEG_DIR=/usr \
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
