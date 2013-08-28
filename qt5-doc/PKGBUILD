# Maintainer: Michael Hansen <zrax0111 gmail com>

pkgname=qt5-doc
_srcpkg=qt5
pkgdesc='Documentation package for qt5'
pkgver=5.1.0
_qtver=5.1
pkgrel=4
arch=('any')
url='http://qt-project.org/'
license=('LGPL')
makedepends=('python' 'python2' 'ruby' 'gperf' 'qt5-tools')
depends=()

_pkgfqn="qt-everywhere-opensource-src-${pkgver}"
source=("http://download.qt-project.org/official_releases/qt/${_qtver}/${pkgver}/single/${_pkgfqn}.tar.xz"
        "qtwebkit-use-python2.patch" "bison3.patch")
md5sums=('44a507beebef73eb364b5a2ec7bbe090'
         '9f5fbd8497e379f60192a92d3ae0e280'
         '23c9b8824c1ea8eec917bf52a519414a')

build() {
    cd ${_pkgfqn}

    # build with python2 (thanks to ascarpino for pointing out the patch at
    # https://projects.archlinux.org/svntogit/packages.git/plain/trunk/use-python2.patch?h=packages/qtwebkit
    patch -uNp1 -i ../qtwebkit-use-python2.patch

    # Fix for Bison 3.0 bug in ANGLE's glslang.y lexer
    cd qtwebkit
    patch -uNp1 -i ../../bison3.patch
    cd ..

    ./configure --prefix=/usr \
        -release \
        -opensource \
        --confirm-license \
        -nomake libs \
        -nomake tools \
        -nomake demos \
        -nomake tests \
        -nomake examples \
        -make docs \
        -opengl desktop \
        -no-egl \
        -no-eglfs \
        -no-rpath \
        -docdir /usr/share/doc/qt

    make && make docs
}

package() {
    cd ${_pkgfqn}

    # Despite telling Qt not to build the libs, it builds the libs...
    # And even then, make install doesn't install the docs!  So although
    # "make install_*_docs" seems like a hack, it's necessary until Qt
    # fixes their build/install process :(
    make INSTALL_ROOT="${pkgdir}" install_qch_docs
    make INSTALL_ROOT="${pkgdir}" install_html_docs
}
