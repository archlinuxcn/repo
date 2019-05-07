# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: lily wilson <hotaru@thinkindifferent.net>

pkgname=libemf
pkgver=1.0.11
pkgrel=1
pkgdesc='Library implementation of ECMA-234 API for the generation of enhanced metafiles'
arch=('i686' 'x86_64')
url='http://libemf.sourceforge.net/'
license=('GPL' 'LGPL')
depends=('gcc-libs')
source=("https://sourceforge.net/projects/libemf/files/libemf/${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('741a611ce1e9636b4f22e1cc4436b6e08c972b1464affa85b46ebd7d9441b6c4')

build() {
    cd "${pkgname}-${pkgver}"
    
    ./configure \
        --prefix='/usr' \
        --enable-static='no' \
        --enable-shared='yes' \
        --enable-threads \
        --enable-editing
        
    make
}

check() {
    cd "${pkgname}-${pkgver}"
    
    make check
}

package() {
    cd "${pkgname}-${pkgver}"
    
    make DESTDIR="$pkgdir" install
}
