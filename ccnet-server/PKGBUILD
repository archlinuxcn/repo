# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname='ccnet-server'
pkgver='6.3.2'
pkgrel=1
pkgdesc="Internal communication framework and user/group management for seafile server"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('GPL2')
depends=('libevent' 'libsearpc' 'libldap' 'libmariadbclient' 'postgresql-libs')
makedepends=('vala')
conflicts=('ccnet')
source=("$pkgname-v$pkgver-server.tar.gz::$url/archive/v$pkgver-server.tar.gz")
sha256sums=('ea33cc13f08c8fd9162e7c0e0f9bd37716f637bfad60f43b7037748c794d421d')

prepare () {
    cd "$srcdir/$pkgname-$pkgver-server"
    sed -i "s|(DESTDIR)@prefix@|@prefix@|" "./libccnet.pc.in"
}

build () {
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

package () {
    cd "$srcdir/$pkgname-$pkgver-server"
    make DESTDIR="$pkgdir" install
}
