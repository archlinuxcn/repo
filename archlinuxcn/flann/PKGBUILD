# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Tim Rakowski <tim.rakowski@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Javier Fuentes <0xffaa.rm@gmail.com>
# Contributor: Figo.zhang <figo1802@gmail.com>
# Contributor: hauptmech

pkgname=flann
pkgver=1.9.1
pkgrel=6
pkgdesc="FLANN is a library for performing fast approximate nearest neighbor searches in high dimensional spaces"
arch=('i686' 'x86_64')
url='https://github.com/mariusmuja/flann'
license=('BSD')
depends=('lz4' 'hdf5')
makedepends=('cmake' 'python' 'texlive-core')
optdepends=('python: python bindings'
            'cuda: cuda support')
source=("https://github.com/mariusmuja/flann/archive/${pkgver}.tar.gz")
md5sums=('73adef1c7bf8e8b978987e7860926ea6')

prepare() {
  cd "$srcdir/flann-${pkgver}"

  sed -i "s|setup\.py install|setup.py install --root=$pkgdir --optimize=1|" src/python/CMakeLists.txt

  touch src/cpp/empty.cpp
  sed -i -e 's/flann_cpp SHARED \"\"/flann_cpp SHARED \"empty\.cpp\"/g' src/cpp/CMakeLists.txt
  sed -i -e 's/flann SHARED \"\"/flann SHARED \"empty\.cpp\"/g' src/cpp/CMakeLists.txt
}

build() {
  cd "$srcdir/flann-${pkgver}"

  #[[ -d build ]] && rm -r build
  mkdir -p build && cd build
  cmake .. \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DBUILD_MATLAB_BINDINGS=OFF \
      -DBUILD_PYTHON_BINDINGS=ON \
      -DPYTHON_EXECUTABLE=/usr/bin/python2 \
      -DBUILD_TESTS=OFF \
      -DBUILD_EXAMPLES=OFF
  make
  make doc
}

package() {
  cd "$srcdir/flann-${pkgver}"

  cd build
  make DESTDIR="$pkgdir" install

  #install license file
  install -D -m644 ../COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

