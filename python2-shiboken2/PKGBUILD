# Maintainer:  Gabriel Souza Franco <Z2FicmllbGZyYW5jb3NvdXphQGdtYWlsLmNvbQ==>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=python2-shiboken2
_qtver=5.11.2
pkgver=${_qtver/-/}
pkgrel=1
arch=(x86_64)
url='http://qt-project.org/'
license=(GPL2 LGPL)
pkgdesc='Generates bindings for C++ libraries using CPython source code'
depends=(python2)
makedepends=(clang llvm cmake libxslt qt5-xmlpatterns)
_pkgfqn=pyside-setup-everywhere-src-${_qtver}
source=("http://download.qt.io/official_releases/QtForPython/pyside2/PySide2-$pkgver-src/${_pkgfqn}.tar.xz")
sha256sums=('18f572f1f832e476083d30fccabab167450f2a8cbe5cd9c6e6e4fa078ccb86c2')

build() {
    mkdir -p build
    cd build
    cmake ../${_pkgfqn}/sources/shiboken2 \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_TESTS=OFF \
        -DUSE_PYTHON_VERSION=2
    make
}

package_python2-shiboken2() {
    cd build
    make DESTDIR="$pkgdir" install
    # Provided in shiboken
    rm -r "$pkgdir"/usr/{bin,include,lib/{cmake/*/Shiboken2Config{,Version}.cmake,pkgconfig},share}
}
