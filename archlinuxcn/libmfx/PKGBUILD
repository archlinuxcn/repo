# Maintainer: Daniel Bermond < gmail-com: danielbermond >

pkgname=libmfx
_srcname=mfx_dispatch
pkgver=1.25
pkgrel=2
pkgdesc='Intel Media SDK dispatcher library'
arch=('i686' 'x86_64')
url='https://github.com/lu-zero/mfx_dispatch/'
license=('BSD')
depends=('libva')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/lu-zero/mfx_dispatch/archive/${pkgver}.tar.gz")
sha256sums=('853c4555c800a262fedacc580d06c234c520a919e4497b50e555291d87579a42')

prepare() {
    cd "${_srcname}-${pkgver}"
    
    autoreconf -i
}

build() {
    cd "${_srcname}-${pkgver}"
    
    ./configure \
        --prefix='/usr' \
        --enable-shared='yes' \
        --with-libva_drm='yes' \
        --with-libva_x11='yes' \
        --with-pic
        
    make
}

package() {
    cd "${_srcname}-${pkgver}"
    
    make DESTDIR="$pkgdir" install
    
    # fix version in pkg-config file
    sed -i "/Version:/s/[0-9]\.[0-9]\{2\}/${pkgver}/" "${pkgdir}/usr/lib/pkgconfig/libmfx.pc"
    
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
