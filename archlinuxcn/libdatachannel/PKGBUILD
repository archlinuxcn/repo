# Maintainer: Jay Schmidek <jschmidek at gmail dot com>
# Maintainer: Paul-Louis Ageneau <paul-louis at ageneau dot org>

pkgname=libdatachannel
pkgver=0.19.0
pkgrel=1
pkgdesc="C/C++ WebRTC network library featuring Data Channels, Media Transport, and WebSockets"
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url="https://github.com/paullouisageneau/$pkgname"
license=('MPL2')
makedepends=('git' 'cmake')
depends=('openssl' 'libjuice' 'libsrtp')
provides=("$pkgname")
conflicts=("$pkgname")
source=("git+https://github.com/paullouisageneau/$pkgname.git#tag=v$pkgver")
md5sums=('SKIP')

prepare() {
    cd $pkgname
    git submodule update --init --recursive "$srcdir"/"$pkgname"/deps/{usrsctp,plog}
}

build() {
    cd $pkgname
    rm -rf build
    cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DUSE_GNUTLS=0 -DUSE_NICE=0 -DUSE_SYSTEM_JUICE=1 -DUSE_SYSTEM_SRTP=1 -DNO_TESTS=1 -DNO_EXAMPLES=1
    cd build
    make
}

package() {
    cd $pkgname
    cd build
    make DESTDIR="$pkgdir/" install
}

