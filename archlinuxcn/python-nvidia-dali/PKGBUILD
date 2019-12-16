# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-nvidia-dali
_pkgname=dali
pkgver=0.16.0
pkgrel=2
pkgdesc='A library containing both highly optimized building blocks and an execution engine for data pre-processing in deep learning applications'
arch=('x86_64')
url='https://github.com/NVIDIA/DALI'
license=('Apache')
depends=(
  'cuda'
  'lmdb'
  'opencv'
  'protobuf'
  'python'
)
makedepends=(
  'cmake'
  'git'
  'python-setuptools'
)
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
  mkdir "${srcdir}/${pkgname}/build"
  cd "${srcdir}/${pkgname}/build"
  cmake \
    -DBUILD_LMDB:BOOL=ON \
    -DCMAKE_BUILD_TYPE:String=Release \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DProtobuf_USE_STATIC_LIBS:BOOL=OFF \
    ..
  make
  cd 'dali/python'
  python setup.py build
}

package() {
  cd "${srcdir}/${pkgname}/build"
  make DESTDIR="${pkgdir}" install
  cd 'dali/python'
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  # create softlink for libdali.so
  ln -s "/usr/lib/python$(get_pyver)/site-packages/nvidia/dali/libdali.so" "${pkgdir}/usr/lib/libdali.so"
}
# vim:set ts=2 sw=2 et:

