# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: Johannes Dewender  arch at JonnyJD dot net
# Contributor: josephgbr <rafael.f.f1@gmail.com>

_pkgbasename=lame
pkgname=lib32-"$_pkgbasename"
pkgver=3.100
pkgrel=2
pkgdesc='A high quality MPEG Audio Layer III (MP3) encoder (32 bit)'
arch=('x86_64')
url='http://lame.sourceforge.net/'
depends=('lib32-ncurses' "$_pkgbasename")
makedepends=('nasm')
license=('LGPL')
source=("https://downloads.sourceforge.net/sourceforge/lame/${_pkgbasename}-${pkgver}.tar.gz")
sha256sums=('ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e')

build() {
    cd "${_pkgbasename}-${pkgver}"
    
    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
    
    ./configure \
        --prefix='/usr' \
        --libdir='/usr/lib32' \
        --enable-shared='yes' \
        --enable-nasm
    
    make
}

package() {
    cd "${_pkgbasename}-${pkgver}"
    
    make DESTDIR="$pkgdir" install
    
    rm -r "$pkgdir"/usr/{bin,include,share}
}
