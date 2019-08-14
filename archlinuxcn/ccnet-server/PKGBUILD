# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=ccnet-server
pkgver=7.0.3
pkgrel=1
pkgdesc="Internal communication framework and user/group management for seafile server"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('GPL2')
depends=('libevent' 'libsearpc' 'libldap' 'mariadb-libs' 'postgresql-libs')
makedepends=('vala')
conflicts=('ccnet')
provides=('ccnet')
source=("$pkgname-v$pkgver-server.tar.gz::$url/archive/v$pkgver-server.tar.gz")
sha256sums=('b7dd311645be3813c7fdeefb328c5a6948e3130d347dc6a71480ebe9e0f1027b')

prepare() {
    cd "$srcdir/$pkgname-$pkgver-server"
    sed -i "s|(DESTDIR)@prefix@|@prefix@|" "./libccnet.pc.in"
}

build() {
    cd "$srcdir/$pkgname-$pkgver-server"
    ./autogen.sh
    ./configure \
        --enable-ldap \
        --enable-python \
        --enable-console \
        --prefix=/usr \
        PYTHON='/usr/bin/python2'
    make
}

package() {
    cd "$srcdir/$pkgname-$pkgver-server"
    make DESTDIR="$pkgdir" install
}
