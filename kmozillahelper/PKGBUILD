# Maintainer: FadeMind <fademind@gmail.com>
# Contributor: Ramon Buldó <ramon@manjaro.org>
# Contributor: Weng Xuetian <wengxt@gmail.com>
# Contributor: Yegorius <yegorius@domic.us>

pkgname=kmozillahelper
pkgver=0.6.5
pkgrel=1
pkgdesc="Mozilla KDE Integration"
url="https://github.com/openSUSE/$pkgname"
arch=('i686' 'x86_64')
license=('MIT')
depends=('ki18n' 'kio' 'knotifications' 'kwindowsystem')
makedepends=('cmake' 'extra-cmake-modules' 'python')
_gitcommit=83cd08e0c917fda16b30d91f929779304c46d273
source=("$pkgname-$pkgver-$pkgrel.tar.gz::$url/archive/$_gitcommit.tar.gz")
sha256sums=('987b9a5b35e5f6bef36830184bd0ab2f200a7d7525216320a379ed1a1ef24b0f')

prepare() {
    mv $srcdir/$pkgname-$_gitcommit $srcdir/$pkgname
    if [[ -d build ]]; then
        rm -Rf build
    fi
    mkdir -p build
}

build() {
    cd build  
    cmake ../$pkgname \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr
    make
}

package() {
    make -C build DESTDIR="$pkgdir" install
    install -Dm644 $pkgname/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
} 

