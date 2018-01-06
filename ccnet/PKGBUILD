# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=ccnet
pkgver=6.1.4
pkgrel=1
pkgdesc="A framework for writing networked applications in C."
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/${pkgname}"
license=('GPL2')
depends=('ccnet-server')
makedepends=('vala' 'libmariadbclient' )
source=("${pkgname}-v${pkgver}-server.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "libccnet.pc.patch")
sha256sums=('59a54dcf967d367cd52f0d6297897dc4766db96fc328a40cdc05ac7c38c010e7'
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
    rm -rf "${pkgdir}/usr/bin/ccnet-init"
}
