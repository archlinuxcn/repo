# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Maintainer: Hugo Osvaldo Barrera <hugo@osvaldobarrera.com.ar>
# Contributor: Matthias Maennich <arch@maennich.net>
# Contributor: Jan-Erik Meyer-Luetgens <nyan at meyer-luetgens dot de>
pkgname=python-shiboken
pkgver=1.2.1
pkgrel=1
_pyver=3.3
_py2ver=2.7
pkgdesc="Python 2 & 3 bindings generator for Qt C++ libraries"
arch=('i686' 'x86_64')
license=('LGPL')
url="http://qt-project.org/wiki/PySide"
depends=("qt4>=4.8" 'openssl' 'libxslt')
optdepends=(
    "python-sphinx: Documentation"
    "python=${_pyver}: Python 3 support"
    "python2=${_py2ver}: Python 2 support"
)
makedepends=('cmake' 'automoc4' 'generatorrunner>=0.6.16' "python" "python2")
conflicts=("libshiboken")
provides=("libshiboken" "shiboken=$pkgver")
replaces=('shiboken')
source=("http://download.qt-project.org/official_releases/pyside/shiboken-$pkgver.tar.bz2" "FindPython3Libs.cmake.patch")
md5sums=('06100e2c91ab4433dbf15c26f5bb6c17' 'e21f354434c2c43b8ebdcf582d512de5')

build(){
    patch $srcdir/shiboken-$pkgver/cmake/Modules/FindPython3Libs.cmake FindPython3Libs.cmake.patch
    cd $srcdir/shiboken-$pkgver
    mkdir -p build_3 && cd build_3
    cmake ../ -DCMAKE_INSTALL_PREFIX=/usr     \
              -DCMAKE_BUILD_TYPE=Release      \
              -DBUILD_TESTS=OFF               \
	      -DQT_QMAKE_EXECUTABLE=qmake-qt4 \
              -DUSE_PYTHON3=yes
    make
    cd ..

    mkdir -p build_2 && cd build_2
    cmake ../ -DCMAKE_INSTALL_PREFIX=/usr     \
              -DCMAKE_BUILD_TYPE=Release      \
              -DBUILD_TESTS=OFF               \
	      -DQT_QMAKE_EXECUTABLE=qmake-qt4 \
              -DPYTHON_EXECUTABLE=/usr/bin/python${_py2ver} \
              -DPYTHON_LIBRARY=/usr/lib/libpython${_py2ver}.so \
              -DPYTHON_INCLUDE_DIR=/usr/include/python${_py2ver}
    make
}

package(){
    cd $srcdir/shiboken-$pkgver/build_3
    make DESTDIR=$pkgdir install

    cd generator
    _pyverflags=$(python3 -c 'import sysconfig; print(sysconfig.get_config_var("SOABI"))')
    install -D -m 755 ../data/ShibokenConfig.cmake $pkgdir/usr/lib/cmake/Shiboken-$pkgver/
    install -D -m 755 ../data/ShibokenConfigVersion.cmake $pkgdir/usr/lib/cmake/Shiboken-$pkgver/
    install -D -m 755 ../data/ShibokenConfig.${_pyverflags}.cmake $pkgdir/usr/lib/cmake/Shiboken-$pkgver/
    install -D -m 755 ../data/shiboken.pc $pkgdir/usr/lib/pkgconfig/

    cd $srcdir/shiboken-$pkgver/build_2
    make DESTDIR=$pkgdir install
    cd generator
    install -D -m 755 ../data/ShibokenConfig-python${_py2ver}.cmake $pkgdir/usr/lib/cmake/Shiboken-$pkgver/
}

