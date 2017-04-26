# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=ccnet
pkgver=6.0.4
pkgrel=2
pkgdesc="A framework for writing networked applications in C."
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/${pkgname}"
license=('GPL2')
depends=('ccnet-server')
makedepends=('vala' 'libmariadbclient' )
source=("${pkgname}-v${pkgver}-server.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "libccnet.pc.patch"
        "openssl-1.0.patch")
sha256sums=('2156787fc9ae1e4293493f0ce398aa8b97d84b9f0201d2fd6986b736bd249b04'
            '66c3b02c3981db6a80819e0ae103bedadf8dfdf81405a7f75a9cba714acf973f'
            'ea7a80195436ba61b45bd2a1ee23b31975c841034189542ea3faf30ca9107f02')

prepare () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    patch -p1 -i "${srcdir}"/libccnet.pc.patch
    patch -p1 -i "${srcdir}"/openssl-1.0.patch
}

build () {
    cd "${srcdir}/${pkgname}-${pkgver}"
    export PKG_CONFIG_PATH=/usr/lib/openssl-1.0/pkgconfig
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
