# Maintainer:  Gabriel Souza Franco <Z2FicmllbGZyYW5jb3NvdXphQGdtYWlsLmNvbQ==>
# Contributor: Florian Pritz
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: mickele
# Contributor: marcus fritzsch <fritschy@googlemail.com>

pkgbase=coin
pkgname=(coin coin-docs)
pkgver=4.0.0
pkgrel=1
pkgdesc='A high-level 3D graphics toolkit on top of OpenGL'
url='https://github.com/coin3d/coin'
license=('GPL')
arch=('i686' 'x86_64')
depends=('libgl')
makedepends=('cmake' 'doxygen' 'glu' 'boost')
optdepends=('openal: sound/dynamic linking support'
            'fontconfig: dynamic linking support'
            'zlib: dynamic linking support'
            'freetype2: dynamic linking support')
source=("https://github.com/coin3d/coin/archive/Coin-$pkgver.tar.gz"
        "coin-remove-cpack.patch::https://github.com/coin3d/coin/commit/be8e3d5.patch")
sha256sums=('b00d2a8e9d962397cf9bf0d9baa81bcecfbd16eef675a98c792f5cf49eb6e805'
            'c77a6bbcaef4d65b45eac7711d3be713d4d23699d63a38f57030febb4b16e24d')

prepare() {
    cd coin-Coin-$pkgver

    patch -Np1 -i ../coin-remove-cpack.patch
}

build() {
    mkdir -p build
    cd build

    cmake ../coin-Coin-$pkgver \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCOIN_THREADSAFE=ON \
        -DCOIN_BUILD_DOCUMENTATION=ON \
        -DCOIN_BUILD_DOCUMENTATION_CHM=OFF \
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
