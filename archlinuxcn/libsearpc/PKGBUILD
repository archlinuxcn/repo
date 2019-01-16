# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=libsearpc
epoch=1
pkgver=3.1.0
pkgrel=2
pkgdesc="A simple C language RPC framework (including both server side & client side)"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/libsearpc"
license=('Apache')
depends=("glib2>=2.26.0" "jansson>=2.2.1" "python2-gobject2>=2.26.0" 'python2-simplejson')
source=("libsearpc-${pkgver}.tar.gz::${url}/archive/v${pkgver}.zip"
        "libsearpc.pc.patch")
sha256sums=('894917227243a6961bebac908c82898ed35dd3b5bf85acaa6f9c8e2d0b063326'
            'aec39a303aaebc0777a22d8c53367f52f619654d63f62b362d75c1c599e632f4')

prepare () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    patch -p1 -i "${srcdir}"/libsearpc.pc.patch
}

build () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    ./autogen.sh
    ./configure --prefix=/usr PYTHON=/usr/bin/python2
    make
}

check () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make check
}

package () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
