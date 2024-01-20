# Maintainer: Paul-Louis Ageneau <paul-louis at ageneau dot org>

pkgname=libjuice
pkgver=1.3.4
pkgrel=1
pkgdesc="UDP Interactive Connectivity Establishment (ICE) library"
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url="https://github.com/paullouisageneau/$pkgname"
license=('MPL2')
makedepends=('git' 'cmake')
depends=('glibc')
provides=('libjuice.so')
conflicts=()
source=("git+https://github.com/paullouisageneau/$pkgname.git#tag=v$pkgver")
md5sums=('SKIP')

build() {
    cd $pkgname
    rm -rf build
    cmake -B build -Wno-dev \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DNO_TESTS=1

    cmake --build build
}

package() {
    cd $pkgname
    DESTDIR="$pkgdir/" cmake --install build
}
