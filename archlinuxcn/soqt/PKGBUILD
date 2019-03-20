# Maintainer:  Gabriel Souza Franco <Z2FicmllbGZyYW5jb3NvdXphQGdtYWlsLmNvbQ==>
# Contributor: Florian Pritz
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: mickele
# Contributor: marcus fritzsch <fritschy@googlemail.com>

pkgname=soqt
_count=2014
_rev=872b87e73dfb
pkgver=1.6.0a+$_count+m$_rev
pkgrel=1
pkgdesc='A library which provides the glue between Coin and Qt'
arch=('i686' 'x86_64')
url='http://www.coin3d.org/lib/soqt/'
license=('GPL')
depends=('coin>=4.0.0a' 'qt5-base')
makedepends=('mercurial' 'cmake' 'doxygen')
source=("soqt::hg+https://bitbucket.org/Coin3D/soqt#revision=$_rev"
        "generalmsvcgeneration::hg+https://bitbucket.org/Coin3D/generalmsvcgeneration"
        "soanydata::hg+https://bitbucket.org/Coin3D/soanydata"
        "sogui::hg+https://bitbucket.org/Coin3D/sogui")
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')

build() {
    mkdir -p build
    cd build

    cmake ../soqt \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DSOQT_BUILD_DOC_MAN=ON \
        -DSOQT_BUILD_DOC_CHM=OFF

    make
}

package() {
    cd build

    make DESTDIR="$pkgdir" install

    # remove html help pages
    rm -rf "$pkgdir/usr/share/doc"
}

