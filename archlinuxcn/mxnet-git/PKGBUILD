# Maintainer: Butui Hu <hot123tea123@gmail.com>

_cudaarch=Common
_pkgname=mxnet
pkgname=('mxnet-git' 'mxnet-mkl-git' 'mxnet-cuda-git' 'mxnet-cuda-mkl-git')
_pkgver=1.5.1
pkgver=1.5.1.r10454.3d38dbde74
pkgrel=1
pkgdesc="A flexible and efficient library for deep learning"
arch=('x86_64')
url="http://mxnet.io/"
license=('Apache')
depends=(
  'cblas'
  'curl'
  'double-conversion'
  'hdf5'
  'intel-tbb'
  'lapack'
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

  # find blas automatically
  sed -i 's/find_package(OpenBLAS REQUIRED)/find_package(BLAS REQUIRED)/' "${srcdir}/${_pkgname}/cmake/ChooseBlas.cmake" "${srcdir}/${_pkgname}/3rdparty/mshadow/cmake/mshadow.cmake"
  sed -i 's/OpenBLAS_LIB/BLAS_LIBRARIES/' "${srcdir}/${_pkgname}/cmake/ChooseBlas.cmake" "${srcdir}/${_pkgname}/cmake/ChooseBlas.cmake" "${srcdir}/${_pkgname}/3rdparty/mshadow/cmake/mshadow.cmake"
  sed -i '/OpenBLAS_INCLUDE_DIR/d' "${srcdir}/${_pkgname}/cmake/ChooseBlas.cmake" "${srcdir}/${_pkgname}/3rdparty/mshadow/cmake/mshadow.cmake"

  # compute capability >= 3.7
  sed -i '/APPEND CUDA_COMMON_GPU_ARCHITECTURES/d' "${srcdir}/${_pkgname}/cmake/FirstClassLangCuda.cmake"
  sed -i '/set(CUDA_COMMON_GPU_ARCHITECTURES/c\set(CUDA_COMMON_GPU_ARCHITECTURES "3.7" "5.0" "5.2" "5.2+PTX" "6.0" "6.1" "6.1+PTX" "7.0" "7.5")' "${srcdir}/${_pkgname}/cmake/FirstClassLangCuda.cmake"

  rm -rf "${srcdir}/${_pkgname}/build"
  mkdir "${srcdir}/${_pkgname}/build"
  cp -a "${srcdir}/${_pkgname}" "${srcdir}/mxnet-git"
  cp -a "${srcdir}/${_pkgname}" "${srcdir}/mxnet-mkl-git"
  cp -a "${srcdir}/${_pkgname}" "${srcdir}/mxnet-cuda-git"
  cp -a "${srcdir}/${_pkgname}" "${srcdir}/mxnet-cuda-mkl-git"
}

build() {
  cmake_opts=(
    -DBUILD_CPP_EXAMPLES:BOOL=OFF
    -DBUILD_TESTING:BOOL=OFF
    -DCMAKE_EXE_LINKER_FLAGS="$(pkg-config --libs cblas)"
    -DCMAKE_INSTALL_LIBDIR:PATH=lib
    -DCMAKE_INSTALL_PREFIX:PATH=/usr
    -DCMAKE_SHARED_LINKER_FLAGS="$(pkg-config --libs cblas)"
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
    -DINSTALL_DOCUMENTATION:BOOL=OFF
    -DUSE_BLAS=open
    -DUSE_CPP_PACKAGE:BOOL=ON
    -DUSE_DIST_KVSTORE:BOOL=ON
    -DUSE_GPERFTOOLS:BOOL=OFF
    -DUSE_JEMALLOC:BOOL=OFF
    -DUSE_LAPACK:BOOL=ON
    -DUSE_MKL_IF_AVAILABLE:BOOL=OFF
    -DUSE_OPENMP:BOOL=ON
    -DUSE_S3:BOOL=ON
)

  export CC=gcc
  export CXX=g++

  # building without CUDA and without MKL-DNN
  cd "${srcdir}/mxnet-git/build"
  cmake \
    ${cmake_opts[@]} \
    -DUSE_CUDA:BOOL=OFF \
    -DUSE_CUDNN:BOOL=OFF \
    -DUSE_MKLDNN:BOOL=OFF \
    -DUSE_NCCL:BOOL=OFF \
    -DUSE_OPENCV:BOOL=ON \
    ..
  make
  cd ../python
  python setup.py build --with-cython

  # building without CUDA and with MKL-DNN
  cd "${srcdir}/mxnet-mkl-git/build"
  cmake \
    ${cmake_opts[@]} \
    -DUSE_CUDA:BOOL=OFF \
    -DUSE_CUDNN:BOOL=OFF \
    -DUSE_MKLDNN:BOOL=ON \
    -DUSE_NCCL:BOOL=OFF \
    -DUSE_OPENCV:BOOL=ON \
    ..
  make
  cd ../python
  python setup.py build --with-cython

  # use gcc version compatible with CUDA
  export CC=/opt/cuda/bin/gcc
  export CXX=/opt/cuda/bin/g++

  # building with CUDA and without MKL-DNN
  cd "${srcdir}/mxnet-cuda-git/build"
  cmake \
    ${cmake_opts[@]} \
    -DCUDA_ARCH_LIST=${_cudaarch} \
    -DUSE_CUDA:BOOL=ON \
    -DUSE_CUDNN:BOOL=ON \
    -DUSE_MKLDNN:BOOL=OFF \
    -DUSE_NCCL:BOOL=ON \
    -DUSE_OPENCV:BOOL=OFF \
    ..
  make
  cd ../python
  python setup.py build --with-cython

  # building with CUDA and with MKL-DNN
  cd "${srcdir}/mxnet-cuda-mkl-git/build"
  cmake \
    ${cmake_opts[@]} \
    -DCUDA_ARCH_LIST=${_cudaarch} \
    -DUSE_CUDA:BOOL=ON \
    -DUSE_CUDNN:BOOL=ON \
    -DUSE_MKLDNN:BOOL=ON \
    -DUSE_NCCL:BOOL=ON \
    -DUSE_OPENCV:BOOL=OFF \
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

package_mxnet-mkl-git() {
  pkgdesc="${pkgdesc} (with MKL-DNN)"
  depends+=(opencv)

  export CC=gcc
  export CXX=g++
  _package
}

package_mxnet-cuda-git() {
  pkgdesc="${pkgdesc} (with CUDA)"
  depends+=(cuda cudnn nccl)

  export CC=/opt/cuda/bin/gcc
  export CXX=/opt/cuda/bin/g++
  _package
}

package_mxnet-cuda-mkl-git() {
  pkgdesc="${pkgdesc} (with CUDA and MKL-DNN)"
  depends+=(cuda cudnn nccl)
  provides+=(mxnet-cuda=${pkgver} mxnet-mkl=${pkgver})
  conflicts+=(mxnet-cuda=${pkgver} mxnet-mkl=${pkgver})

  export CC=/opt/cuda/bin/gcc
  export CXX=/opt/cuda/bin/g++
  _package
}
# vim:set ts=2 sw=2 et:

