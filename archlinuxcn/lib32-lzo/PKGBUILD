# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: rafaelff <rafaelff@gnome.org>

_pkgbasename=lzo
pkgname=lib32-"$_pkgbasename"
pkgver=2.10
pkgrel=2
pkgdesc='Portable lossless data compression library (32 bit)'
arch=('x86_64')
url='https://www.oberhumer.com/opensource/lzo/'
license=('GPL')
depends=('lib32-glibc' "$_pkgbasename")
source=("https://www.oberhumer.com/opensource/lzo/download/${_pkgbasename}-${pkgver}.tar.gz")
sha256sums=('c0f892943208266f9b6543b3ae308fab6284c5c90e627931446fb49b4221a072')

build() {
    cd "${_pkgbasename}-${pkgver}"
    
    export CC='gcc -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
    
    ./configure \
        --prefix='/usr' \
        --libdir='/usr/lib32' \
        --enable-shared
        
    make
    
    # build minilzo
    $CC $CFLAGS -fpic -Iinclude/lzo -o minilzo/minilzo.o -c minilzo/minilzo.c
    $CC $LDFLAGS -g -shared -o libminilzo.so.0 -Wl,-soname,libminilzo.so.0 minilzo/minilzo.o
}

check() {
    cd "${_pkgbasename}-${pkgver}"
    
    make test # larger test
    make check
}

package() {
    cd "${_pkgbasename}-${pkgver}"
    
    make DESTDIR="$pkgdir" install
    
    rm -r "$pkgdir"/usr/{include,share}
    
    # install minilzo
    install -m 755 libminilzo.so.0 "$pkgdir"/usr/lib32
    ln -s libminilzo.so.0 "$pkgdir"/usr/lib32/libminilzo.so
}
