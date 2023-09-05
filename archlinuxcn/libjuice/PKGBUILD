# Maintainer: Paul-Louis Ageneau <paul-louis at ageneau dot org>

pkgname=libjuice
pkgver=1.3.1
pkgrel=1
pkgdesc="UDP Interactive Connectivity Establishment (ICE) library"
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url="https://github.com/paullouisageneau/$pkgname"
license=('MPL2')
makedepends=('git' 'cmake')
depends=()
provides=("$pkgname")
conflicts=("$pkgname")
source=("git+https://github.com/paullouisageneau/$pkgname.git#tag=v$pkgver")
md5sums=('SKIP')

build() {
    cd $pkgname
    rm -rf build
    cmake -B build -Wno-dev -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DNO_TESTS=1
    cd build
    make
}

package() {
    cd $pkgname
    cd build
    make DESTDIR="$pkgdir/" install
}
