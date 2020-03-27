# Maintainer: Butui Hu <hot123tea123@gmail.com>

#_cudaarch="3.7;5.0;5.2;5.2+PTX;5.3;5.3+PTX;6.0;6.0+PTX;6.1;6.1+PTX;6.2;6.2+PTX;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX"
_cudaarch="6.0;6.1;7.0;7.5"
_pkgname=mxnet
pkgname=('mxnet-git' 'mxnet-cuda-git')
_pkgver=2.0.0
pkgver=2.0.0.r10821.9a355ebc1d
pkgrel=1
pkgdesc='A flexible and efficient library for deep learning'
arch=('x86_64')
url="http://mxnet.io/"
license=('Apache')
depends=(
  'curl'
  'double-conversion'
  'hdf5'
  'intel-mkl'
  'intel-tbb'
  'protobuf'
  'python-graphviz'
  'python-numpy'
  'python-requests'
  'zeromq'
)
makedepends=(
  'cmake'
  'cuda'
  'cudnn'
  'cython'
  'git'
  'gtk3'
  'nccl'
  'opencv'
  'qt5-base'
)
provides=(mxnet=${pkgver})
conflicts=(mxnet)
source=("${_pkgname}::git+https://github.com/apache/incubator-mxnet.git")
sha512sums=('SKIP')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

pkgver() {
  cd "${srcdir}/${_pkgname}"
  ver=$(printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)")
  echo "${_pkgver}.${ver}"
}

prepare() {
  cd "${srcdir}/${_pkgname}"
  git submodule update --init --recursive

  # do not use 3rd party openmp
  rm -rfv "${srcdir}/${_pkgname}/3rdparty/openmp"
  # the latest cmake set OpenMP_FOUND instead of OPENMP_FOUND
  sed -i 's/OPENMP_FOUND/OpenMP_FOUND/g' "${srcdir}/${_pkgname}/CMakeLists.txt"

  rm -rf "${srcdir}/${_pkgname}/build"
  mkdir "${srcdir}/${_pkgname}/build"
  cp -a "${srcdir}/${_pkgname}" "${srcdir}/mxnet-git"
  cp -a "${srcdir}/${_pkgname}" "${srcdir}/mxnet-cuda-git"
}

build() {
  cmake_opts=(
    -DBUILD_CPP_EXAMPLES:BOOL=OFF
    -DBUILD_TESTING:BOOL=OFF
    -DCMAKE_INSTALL_LIBDIR:PATH=lib
    -DCMAKE_INSTALL_PREFIX:PATH=/usr
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
    -DINSTALL_DOCUMENTATION:BOOL=OFF
    -DMKL_USE_SINGLE_DYNAMIC_LIBRARY:BOOL=ON
    -DUSE_BLAS=mkl
    -DUSE_CPP_PACKAGE:BOOL=ON
    -DUSE_CXX14_IF_AVAILABLE:BOOL=ON
    -DUSE_DIST_KVSTORE:BOOL=ON
    -DUSE_GPERFTOOLS:BOOL=OFF
    -DUSE_JEMALLOC:BOOL=OFF
    -DUSE_LAPACK:BOOL=ON
    -DUSE_MKLDNN:BOOL=ON
    -DUSE_MKL_IF_AVAILABLE:BOOL=ON
    -DUSE_OPENMP:BOOL=ON
    -DUSE_S3:BOOL=ON
)

  # use gcc version compatible with CUDA
  export CC=/opt/cuda/bin/gcc
  export CXX=/opt/cuda/bin/g++

  # building with CUDA
  cd "${srcdir}/mxnet-cuda-git/build"
  cmake \
    ${cmake_opts[@]} \
    -DMXNET_CUDA_ARCH=${_cudaarch} \
    -DUSE_CUDA:BOOL=ON \
    -DUSE_CUDNN:BOOL=ON \
    -DUSE_NCCL:BOOL=ON \
    -DUSE_OPENCV:BOOL=OFF \
    ..
  make
  cd ../python
  python setup.py build --with-cython
  
  export CC=gcc
  export CXX=g++

  # building without CUDA
  cd "${srcdir}/mxnet-git/build"
  cmake \
    ${cmake_opts[@]} \
    -DUSE_CUDA:BOOL=OFF \
    -DUSE_CUDNN:BOOL=OFF \
    -DUSE_NCCL:BOOL=OFF \
    -DUSE_OPENCV:BOOL=ON \
    ..
  make
  cd ../python
  python setup.py build --with-cython
}

_package() {
  cd "${srcdir}/${pkgname}/build"

  # install mxnet core component
  make DESTDIR="${pkgdir}" install

  if [ -f "${srcdir}/${pkgname}/build/im2rec" ]; then
    install -Dm755 "${srcdir}/${pkgname}/build/im2rec" "${pkgdir}/usr/bin/im2rec"
  fi

  # install python binding
  cd "${srcdir}/${pkgname}/python"
  python setup.py install --root="${pkgdir}" --optimize=1 --with-cython --skip-build
  install -Dm644 "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # create neccesarry soft links
  ln -sf '/usr/lib/libmxnet.so' "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/mxnet/libmxnet.so"
  ln -s "/usr/include" "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/mxnet/include"

  # remove unwantted files
  rm -rfv "${pkgdir}/usr/mxnet"
  rm -rfv "${pkgdir}/usr/lib/cmake" "${pkgdir}/usr/share/doc"
  find "${pkgdir}" -type f -name '*dnn*' -delete
  find "${pkgdir}" -name '*.a' -delete
  find "${pkgdir}" -type d -empty -delete
}


package_mxnet-git() {
  depends+=(opencv)

  export CC=gcc
  export CXX=g++
  _package
}

package_mxnet-cuda-git() {
  pkgdesc="${pkgdesc} (with CUDA)"
  depends+=(cuda cudnn nccl)
  provides+=(mxnet-cuda=${pkgver})
  conflicts+=(mxnet-cuda=${pkgver})

  export CC=/opt/cuda/bin/gcc
  export CXX=/opt/cuda/bin/g++
  _package
}

# vim:set ts=2 sw=2 et:

