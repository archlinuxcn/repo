# Maintainer: Sven-Hendrik Haase <sh@lutzhaase.com>
# Maintainer: Javier Fuentes <0xffaa.rm@gmail.com>
# Contributor: Figo.zhang <figo1802@gmail.com>
# Contributor: hauptmech

pkgname=flann
pkgver=1.8.4
pkgrel=2
pkgdesc="FLANN is a library for performing fast approximate nearest neighbor searches in high dimensional spaces"
arch=('i686' 'x86_64')
url='http://www.cs.ubc.ca/~mariusm/index.php/FLANN/FLANN'
license=('BSD')
depends=('hdf5')
makedepends=('cmake' 'python2')
optdepends=('python2: python bindings'
            'cuda: cuda support')
source=("http://people.cs.ubc.ca/~mariusm/uploads/FLANN/flann-${pkgver}-src.zip")
md5sums=('a0ecd46be2ee11a68d2a7d9c6b4ce701')

build() {
  cd $srcdir/flann-${pkgver}-src

  sed -i 's/lib64/lib/g' cmake/flann_utils.cmake

  sed -i '1 i #undef _GLIBCXX_ATOMIC_BUILTINS' src/cpp/flann/algorithms/kdtree_cuda_3d_index.cu
  sed -i '1 i #undef _GLIBCXX_USE_INT128' src/cpp/flann/algorithms/kdtree_cuda_3d_index.cu

  sed -i 's|#!/usr/bin/env python|#!/usr/bin/python2|' \
      bin/download_checkmd5.py \
      bin/run_test.py \
      src/python/setup.py.tpl \
      test/test_clustering.py \
      test/test_index_save.py \
      test/test_nn_autotune.py \
      test/test_nn_index.py \
      test/test_nn.py

  sed -i 's|#!/usr/bin/python|#!/usr/bin/python2|' \
      test/memusage_clustering.py \
      test/memusage_nn.py

  sed -i "s|setup\.py install|setup.py install --root=$pkgdir --optimize=1|" src/python/CMakeLists.txt

  [[ -d build ]] && rm -r build
  mkdir build && cd build
  cmake .. \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DBUILD_MATLAB_BINDINGS=OFF \
      -DBUILD_PYTHON_BINDINGS=ON \
      -DPYTHON_EXECUTABLE=/usr/bin/python2 \
      -DNVCC_COMPILER_BINDIR=/usr/bin
  make
}

package() {
  cd $srcdir/flann-${pkgver}-src
  
  cd build
  make DESTDIR=$pkgdir install

  #install license file
  install -D -m644 ../COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # FIXME: awful hack, but I got this error without the fix:
  # running install_lib
  # copying build/lib/pyflann/exceptions.py -> /usr/lib/python2.7/site-packages/pyflann
  # error: /usr/lib/python2.7/site-packages/pyflann/exceptions.py: Permission denied
  _python2libpath="`python2 -c "from distutils.sysconfig import get_python_lib; print get_python_lib()" | tr -d '\n'`"
  mkdir -p "${pkgdir}${_python2libpath}"
  cp -pr "${pkgdir}/usr/share/flann/python/pyflann" "${pkgdir}${_python2libpath}/pyflann"

}

