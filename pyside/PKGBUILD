# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Contributor: Matthias Maennich <arch@maennich.net>
# Contributor: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
# Contributor: Jan-Erik Meyer-Luetgens <nyan at meyer-luetgens dot de>
pkgbase=pyside
pkgname=pyside
true && pkgname=(pyside-common pyside-python2 pyside-python3)
_pkgrealname=pyside
pkgver=1.2.1
pkgrel=4
pkgdesc="Provides LGPL Qt bindings for Python and related tools for binding generation. Will build for both Python 2 and 3 versions."
arch=('i686' 'x86_64')
license=('LGPL')
url="http://qt-project.org/wiki/PySide"
_qtver=4.8
makedepends=('cmake' 'automoc4' 'qtwebkit' 'python' 'python2')
optdepends=('qtwebkit: for PySide.QtWebKit')
source=("http://download.qt-project.org/official_releases/pyside/${_pkgrealname}-qt${_qtver}+$pkgver.tar.bz2")
md5sums=('34b05faa7cc44d3c24d5ccadd894bd3c')

depends=('python' 'python2' "qt4>=${_qtver}" 'phonon' "shiboken>=$pkgver")
provides=("python-pyside=$pkgver" "python2-pyside=$pkgver")
conflicts=('python-pyside' 'python2-pyside')
replaces=('python-pyside' 'python2-pyside')

build(){
    cd $srcdir/${_pkgrealname}-qt${_qtver}+$pkgver
    mkdir -p build_py3 && cd build_py3
    _pyverflags=$(python -c 'import sysconfig; print(sysconfig.get_config_var("SOABI"))')
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF \
      -DQT_PHONON_INCLUDE_DIR=/usr/include/qt4/phonon -DQT_QMAKE_EXECUTABLE=qmake-qt4 \
      -DPYTHON_SUFFIX=.${_pyverflags}
    make

    cd $srcdir/${_pkgrealname}-qt${_qtver}+$pkgver
    mkdir -p build_py2 && cd build_py2
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF \
      -DQT_PHONON_INCLUDE_DIR=/usr/include/qt4/phonon -DQT_QMAKE_EXECUTABLE=qmake-qt4
    make
}

package_pyside-common(){
    true && depends=("qt4>=${_qtver}" 'phonon' "shiboken>=$pkgver")
    true && pkgdesc="Provides LGPL Qt bindings for Python and related tools for binding generation. Common Files."
    true && provides=()
    true && conflicts=()
    true && replaces=()
    # cmake will use Python 3 version by default
    cd $srcdir/${_pkgrealname}-qt${_qtver}+$pkgver/build_py3
    make DESTDIR=$pkgdir install

    rm -rf "$pkgdir"/usr/lib/python* "$pkgdir"/usr/lib/libpyside.* \
      "$pkgdir"/usr/lib/cmake/PySide-1.2.1/PySideConfig*python*.cmake \
      "$pkgdir"/usr/lib/pkgconfig/pyside.pc
}

package_pyside-python3(){
    true && depends=('python' "qt4>=${_qtver}" 'phonon' "shiboken>=$pkgver" "pyside-common=$pkgver")
    true && pkgdesc="Provides LGPL Qt bindings for Python and related tools for binding generation. Python 3 version."
    true && provides=("python-pyside=$pkgver")
    true && conflicts=('python-pyside')
    true && replaces=('python-pyside')

    cd $srcdir/${_pkgrealname}-qt${_qtver}+$pkgver/build_py3
    make DESTDIR=$pkgdir install
    mv "$pkgdir"/usr/lib/pkgconfig/pyside.pc \
      "$pkgdir"/usr/lib/pkgconfig/pyside-py3.pc
    rm -rf "$pkgdir"/usr/include \
      "$pkgdir"/usr/lib/cmake/PySide-$pkgver/PySideConfig.cmake \
      "$pkgdir"/usr/lib/cmake/PySide-$pkgver/PySideConfigVersion.cmake \
      "$pkgdir"/usr/share
}

package_pyside-python2(){
    true && depends=('python' "qt4>=${_qtver}" 'phonon' "shiboken>=$pkgver" "pyside-common=$pkgver")
    true && pkgdesc="Provides LGPL Qt bindings for Python and related tools for binding generation. Python 2 version."
    true && provides=("python2-pyside=$pkgver")
    true && conflicts=('python2-pyside')
    true && replaces=('python2-pyside')

    cd $srcdir/${_pkgrealname}-qt${_qtver}+$pkgver/build_py2
    make DESTDIR=$pkgdir install
    mv "$pkgdir"/usr/lib/pkgconfig/pyside.pc \
      "$pkgdir"/usr/lib/pkgconfig/pyside-py2.pc
    rm -rf "$pkgdir"/usr/include \
      "$pkgdir"/usr/lib/cmake/PySide-$pkgver/PySideConfig.cmake \
      "$pkgdir"/usr/lib/cmake/PySide-$pkgver/PySideConfigVersion.cmake \
      "$pkgdir"/usr/share
}
