# Maintainer:  Gabriel Souza Franco <Z2FicmllbGZyYW5jb3NvdXphQGdtYWlsLmNvbQ==>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=python2-pyside2
_qtver=5.12.0
pkgver=${_qtver/-/}
pkgrel=1
arch=(x86_64)
url='http://qt-project.org/'
license=(LGPL)
pkgdesc='Enables the use of Qt5 APIs in Python applications'
depends=(python2-shiboken2 qt5-base)
optdepends=('qt5-svg: QtSvg bindings'
            'qt5-script: QtScript bindings'
            'qt5-speech: QtTextToSpeech bindings'
            'qt5-websockets: QtWebSockets bindings'
            'qt5-webengine: QtWebEngine bindings'
            'qt5-datavis3d: QtDataVisualization bindings'
            'qt5-scxml: QtScxml bindings'
            'qt5-sensors: QtSensors bindings'
            'qt5-3d: Qt3D bindings'
            'qt5-x11extras: QtX11Extras bindings'
            'qt5-charts: QtCharts bindings'
            'qt5-tools: QtHelp bindings')
makedepends=(shiboken2 python2-shiboken2 cmake
             qt5-multimedia qt5-tools qt5-sensors qt5-charts qt5-webengine qt5-datavis3d
             qt5-websockets qt5-speech qt5-3d qt5-svg qt5-script qt5-scxml qt5-x11extras)
groups=(qt qt5)
_pkgfqn=pyside-setup-everywhere-src-${_qtver}
source=("http://download.qt.io/official_releases/QtForPython/pyside2/PySide2-$pkgver-src/${_pkgfqn}.tar.xz")
sha256sums=('890149628a6c722343d6498a9f7e1906ce3c10edcaef0cc53cd682c1798bef51')

build() {
    mkdir -p build
    cd build

    cmake ../${_pkgfqn}/sources/pyside2 \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_TESTS=OFF \
        -DUSE_PYTHON_VERSION=2
    make
}

package() {
    cd build
    make DESTDIR="$pkgdir" install

    # Provided in pyside2
    rm -r "$pkgdir"/usr/{include,share,lib/{pkgconfig,cmake/*/PySide2Config{.cmake,Version.cmake}}}
}

