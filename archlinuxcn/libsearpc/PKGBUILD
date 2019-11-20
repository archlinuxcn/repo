# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=libsearpc
epoch=2
pkgver=3.2.0
pkgrel=2
pkgdesc="A simple C language RPC framework (including both server side & client side)"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/libsearpc"
license=('Apache')
depends=("glib2>=2.26.0" "jansson>=2.2.1" "python2-gobject2>=2.26.0" 'python2-simplejson')

source=("libsearpc-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "libsearpc.pc.patch"
        "fix_python_future_builtins_object.patch")
sha256sums=('c479d85e405674c3450eac040abe143af5a9fafe7f1b74926e2a05280ab5420e'
            'aec39a303aaebc0777a22d8c53367f52f619654d63f62b362d75c1c599e632f4'
            'f7f8a43bca73e05ce234fb13cae0663c0c7b095d4500200e3479b8eea5fc1497')

prepare () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    patch -p1 -i "${srcdir}"/libsearpc.pc.patch
    patch -p1 -i "${srcdir}"/fix_python_future_builtins_object.patch
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
