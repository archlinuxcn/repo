# Maintainer: Maxqia contrib@maxqia.com

pkgname=keepassx-http
_gitname=keepassx_http
pkgver=2.0.2.r165.gcbb1269
pkgrel=1
pkgdesc="KeepassX, with the proposed keepasshttp support."
arch=('i686' 'x86_64')
url="https://github.com/keepassx/keepassx/pull/111"
license=('GPL2')
depends=('libxtst' 'shared-mime-info' 'qt5-x11extras' 'hicolor-icon-theme' 'desktop-file-utils' 'libmicrohttpd')
install=keepassx.install
makedepends=('git' 'intltool' 'cmake' 'qt5-base' 'qt5-tools' 'zlib' 'libgcrypt')
conflicts=('keepassx-svn' 'keepassx' 'keepassx-git' 'keepassx2' 'keepassx2-git' 'keepassx2-yubikey-git')
options=(!emptydirs)
source=(git+https://github.com/droidmonkey/keepassx_http.git#commit=cbb1269)
md5sums=('SKIP')

pkgver() {
    cd "${_gitname}"
    git describe --long | sed 's/^FOO-//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
    cd ${_gitname}
    mkdir -p build
}

build() {
    cd "${_gitname}/build"
    cmake -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_BINDIR=/usr/bin \
        -DCMAKE_INSTALL_LIBDIR=/usr/lib \
        -DCMAKE_VERBOSE_MAKEFILE=OFF \
        -DWITH_GUI_TESTS=ON \
        -DCMAKE_BUILD_TYPE=Release ..
    make
}

#check() {
#    cd "${_gitname}/build"
#    make test
#}

package() {
    cd "${_gitname}/build"
    make DESTDIR="${pkgdir}" install
}

