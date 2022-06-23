# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-nvidia-dali
_pkgname=dali
pkgver=1.15.0
pkgrel=1
pkgdesc='A library containing both highly optimized building blocks and an execution engine for data pre-processing in deep learning applications'
arch=('x86_64')
url='https://github.com/NVIDIA/DALI'
license=('Apache')
depends=(
  cuda
  ffmpeg
  libtar
  lmdb
  opencv
  protobuf
  python
)
makedepends=(
  clang
  cmake
  git
  python-setuptools
)
OPTIONS=(!lto)
source=("${pkgname}::git+https://github.com/NVIDIA/DALI.git#tag=v${pkgver}")
sha512sums=('SKIP')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

prepare() {
  cd "${srcdir}/${pkgname}"
  git submodule update --init --recursive
}

build() {
  cmake \
    -B "${srcdir}/build" \
    -DBUILD_LMDB=ON \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_RPATH=ON \
    -DProtobuf_USE_STATIC_LIBS=OFF \
    -S "${srcdir}/${pkgname}"
  make -C "${srcdir}/build"
  cd "${srcdir}/build/dali/python"
  python setup.py build
}

package() {
  make -C "${srcdir}/build" DESTDIR="${pkgdir}" install
  cd "${srcdir}/build/dali/python"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  # create softlink to save space
  ln -sf "/usr/lib/python$(get_pyver)/site-packages/nvidia/dali/libdali.so" "${pkgdir}/usr/lib/libdali.so"
  ln -sf "/usr/lib/python$(get_pyver)/site-packages/nvidia/dali/libdali_core.so" "${pkgdir}/usr/lib/libdali_core.so"
  ln -sf "/usr/lib/python$(get_pyver)/site-packages/nvidia/dali/libdali_kernels.so" "${pkgdir}/usr/lib/libdali_kernels.so"
  ln -sf "/usr/lib/python$(get_pyver)/site-packages/nvidia/dali/libdali_operators.so" "${pkgdir}/usr/lib/libdali_operators.so"
}
# vim:set ts=2 sw=2 et:

