# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="52;53;60;61;62;70;72;75;80;86;89"
pkgname=python-nvidia-dali
_pkgname=dali
pkgver=1.23.0
pkgrel=2
pkgdesc='A library containing both highly optimized building blocks and an execution engine for data pre-processing in deep learning applications'
arch=('x86_64')
url='https://github.com/NVIDIA/DALI'
license=('Apache')
depends=(
  cuda
  ffmpeg
  libcudart.so
  libtar
  lmdb
  opencv
  python
)
makedepends=(
  cfitsio
  clang
  cmake
  git
  python-setuptools
)
optdepends=(
  python-pytorch
  python-tensorflow
)
options=(!emptydirs !lto)
source=("${pkgname}::git+https://github.com/NVIDIA/DALI.git#tag=v${pkgver}"
        "https://github.com/NVIDIA/DALI/pull/4692.patch"
)
sha512sums=('SKIP'
            'b7d515e059406dcddf302e534b6040ea223dcfc1399f248d9af0b40e68013c346f67a7bc1d36f7fc6ea10d81437dc8e70c03454f47f7c2b62916ef0616ac5708')

prepare() {
  cd "${srcdir}/${pkgname}"
  git submodule update --init --recursive
  # quick fix for https://github.com/archlinuxcn/repo/issues/2877
  export CXXFLAGS=${CXXFLAGS/-Wp,-D_GLIBCXX_ASSERTIONS}
  # fix constexpr issue
  patch -p1 -i "${srcdir}/4692.patch"
}

build() {
  cmake \
    -B "${srcdir}/build" \
    -DBUILD_BENCHMARK=OFF \
    -DBUILD_CFITSIO=ON \
    -DBUILD_CUFILE=ON \
    -DBUILD_FFTS=ON \
    -DBUILD_LIBSND=ON \
    -DBUILD_LIBTAR=ON \
    -DBUILD_LIBTIFF=ON \
    -DBUILD_LMDB=ON \
    -DBUILD_NVDEC=ON \
    -DBUILD_NVJPEG2K=OFF \
    -DBUILD_NVJPEG=OFF \
    -DBUILD_NVML=ON \
    -DBUILD_NVOF=ON \
    -DBUILD_NVTX=OFF \
    -DBUILD_PROTOBUF=ON \
    -DBUILD_PYTHON=ON \
    -DBUILD_TEST=OFF \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_RPATH=ON \
    -DCUDA_TARGET_ARCHS=${_CUDA_ARCH_LIST} \
    -DProtobuf_USE_STATIC_LIBS=OFF \
    -DVERBOSE_LOGS=ON \
    -DWITH_DYNAMIC_CUDA_TOOLKIT=ON \
    -S "${srcdir}/${pkgname}"
  make -C "${srcdir}/build"
  cd "${srcdir}/build/dali/python"
  python setup.py build
  # built tf plugin
  cmake -B ${srcdir}/build-tf \
    -DCUDA_VERSION=11.8 \
    -S ${srcdir}/${pkgname}/dali_tf_plugin
  make -C ${srcdir}/build-tf
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  make -C "${srcdir}/build" DESTDIR="${pkgdir}" install
  cd "${srcdir}/build/dali/python"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  # create softlink to save space
  ln -sf "${site_packages}/nvidia/dali/libdali.so" "${pkgdir}/usr/lib/libdali.so"
  ln -sf "${site_packages}/nvidia/dali/libdali_core.so" "${pkgdir}/usr/lib/libdali_core.so"
  ln -sf "${site_packages}/nvidia/dali/libdali_kernels.so" "${pkgdir}/usr/lib/libdali_kernels.so"
  ln -sf "${site_packages}/nvidia/dali/libdali_operators.so" "${pkgdir}/usr/lib/libdali_operators.so"
  # install tf plugin
  make -C ${srcdir}/build-tf
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
