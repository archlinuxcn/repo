# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=libsearpc
epoch=1
pkgver=3.0.8
_commit=12a01268825e9c7e17794c58c367e3b4db912ad9
pkgrel=2
pkgdesc="A simple and easy-to-use C language RPC framework (including both server side & client side) based on GObject System."
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
url="https://github.com/haiwen/libsearpc"
license=('Apache')
depends=("glib2>=2.26.0" "jansson>=2.2.1" "python2-gobject2>=2.26.0" 'python2-simplejson')
source=("libsearpc-v${pkgver}.tar.gz::${url}/archive/${_commit}.zip"
        "libsearpc.pc.patch")
sha256sums=('7dc664c4f9f66c7fe79bae4707291c2dfdbb356865bb7c2cebf4c55f605e3238'
            'aec39a303aaebc0777a22d8c53367f52f619654d63f62b362d75c1c599e632f4')

prepare () {
    cd "${srcdir}/${pkgname}-${_commit}"
    patch -p1 -i "${srcdir}"/libsearpc.pc.patch
}

build () {
    cd "${srcdir}/${pkgname}-${_commit}"
    ./autogen.sh
    ./configure --prefix=/usr PYTHON=/usr/bin/python2
    make
}

check () {
    cd "${srcdir}/${pkgname}-${_commit}"
    make check
}

package () {
    cd "${srcdir}/${pkgname}-${_commit}"
    make DESTDIR="${pkgdir}" install
}
