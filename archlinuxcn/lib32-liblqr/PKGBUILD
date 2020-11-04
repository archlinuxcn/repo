# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>

_basename=liblqr
pkgname=lib32-liblqr
pkgver=0.4.2
pkgrel=4
pkgdesc="A seam-carving C/C++ library called Liquid Rescale (32-bit)"
arch=('x86_64')
url="http://liblqr.wikidot.com/"
license=('GPL')
depends=('lib32-glib2' 'liblqr')
options=('!emptydirs')
source=("http://liblqr.wikidot.com/local--files/en:download-page/${_basename}-1-${pkgver}.tar.bz2")
sha256sums=('173a822efd207d72cda7d7f4e951c5000f31b10209366ff7f0f5972f7f9ff137')

build() {
    cd "${_basename}-1-${pkgver}"

    export CC="gcc -m32"
    export CXX="g++ -m32"
    export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32

    make
}

package() {
    cd "${_basename}-1-${pkgver}"

    make DESTDIR="${pkgdir}" install

    rm -rf "${pkgdir}/usr/include"
}
