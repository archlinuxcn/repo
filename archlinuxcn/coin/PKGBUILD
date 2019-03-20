# Maintainer:  Gabriel Souza Franco <Z2FicmllbGZyYW5jb3NvdXphQGdtYWlsLmNvbQ==>
# Contributor: Florian Pritz
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: mickele
# Contributor: marcus fritzsch <fritschy@googlemail.com>

pkgbase=coin
pkgname=(coin coin-docs)
_count=11927
_rev=e74da184f75b
pkgver=4.0.0a+$_count+m$_rev
pkgrel=1
pkgdesc='A high-level 3D graphics toolkit on top of OpenGL'
url='https://bitbucket.org/Coin3D/coin'
license=('GPL')
arch=('i686' 'x86_64')
depends=('libgl')
makedepends=('mercurial' 'cmake' 'doxygen' 'glu')
optdepends=('openal: sound/dynamic linking support'
            'fontconfig: dynamic linking support'
            'zlib: dynamic linking support'
            'freetype2: dynamic linking support')
source=("coin::hg+https://bitbucket.org/Coin3D/coin#revision=$_rev"
        "generalmsvcgeneration::hg+https://bitbucket.org/Coin3D/generalmsvcgeneration"
        "boost-header-libs-full::hg+https://bitbucket.org/Coin3D/boost-header-libs-full")
sha256sums=('SKIP' 'SKIP' 'SKIP')

build() {
    mkdir -p build
    cd build

    cmake ../coin \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCOIN_THREADSAFE=ON \
        -DCOIN_BUILD_DOCUMENTATION_CHM=ON \
        -DCOIN_BUILD_DOCUMENTATION_MAN=ON \
        -DUSE_EXTERNAL_EXPAT=ON

    make
}

package_coin() {
    optdepends+=('coin-docs: Coin documentation')

    cd build

    make DESTDIR="$pkgdir" install

    # final adjustments
    rm -rf "$pkgdir/usr/share/doc"
    for _FILE in threads errors events; do
        mv "$pkgdir/usr/share/man/man3/$_FILE.3" "$pkgdir/usr/share/man/man3/coin-$_FILE.3"
    done
}

package_coin-docs() {
    pkgdesc='A high-level 3D graphics toolkit on top of OpenGL (docs)'
    arch=(any)
    depends=()

    cd build/src/doc

    make DESTDIR="$pkgdir" install
    rm -rf "$pkgdir/usr/share/man"
}
