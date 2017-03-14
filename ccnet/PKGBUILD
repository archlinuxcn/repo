# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=ccnet
pkgver=6.0.3
pkgrel=1
pkgdesc="A framework for writing networked applications in C."
arch=('i686' 'x86_64' 'armv7h' 'armv6h')
url="https://github.com/haiwen/${pkgname}"
license=('GPL2')
depends=('ccnet-server')
makedepends=('vala' 'libmariadbclient' )
source=("${pkgname}-v${pkgver}-server.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "libccnet.pc.patch")
sha256sums=('b766d049e0464f192f509c997e1a76d544c9e8db88957035bcf62f234bfc86a5'
            '66c3b02c3981db6a80819e0ae103bedadf8dfdf81405a7f75a9cba714acf973f')

prepare () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    patch -p1 -i "${srcdir}"/libccnet.pc.patch
}

build () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    ./autogen.sh
    ./configure --prefix=/usr --enable-console PYTHON=/usr/bin/python2
    make
}

package () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make DESTDIR="$pkgdir" install

    # Already provided by ccnet-server
    rm -rf "${pkgdir}/usr/include"
    rm -rf "${pkgdir}/usr/lib"
}
