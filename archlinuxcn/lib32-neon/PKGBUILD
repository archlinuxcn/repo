# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

_basename=neon
pkgname=lib32-neon
pkgver=0.31.2
pkgrel=1
pkgdesc="HTTP and WebDAV client library with a C interface (32 bit)"
arch=('x86_64')
url="https://notroj.github.io/neon"
license=('GPL' 'LGPL')
depends=('lib32-krb5' 'lib32-expat' 'ca-certificates' 'neon')
options=('libtool') # FS#16067
source=(https://notroj.github.io/neon/${_basename}-${pkgver}.tar.gz)
sha512sums=('1e402b40a0445f68ed24d2697ee60d21636f61ebc98edcde37ff9e26c54430acabf3969ac22a942d1dd51bddee0f312c04073b423b0af3a3e7c9bf60cd53e48c')
validpgpkeys=('190555472DCC589BEF01609C608A86DF9833CC49') # Joe Orton

build() {
    cd "${_basename}-${pkgver}"

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32 \
        --with-expat \
        --enable-shared \
        --disable-static \
        --with-ssl=openssl \
        --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt

    sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

    make
}

package() {
    cd "${_basename}-${pkgver}"

    make DESTDIR="${pkgdir}" install

    rm -rf "${pkgdir}/usr"/{bin,include,share}
}
