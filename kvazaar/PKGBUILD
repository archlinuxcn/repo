# Maintainer: Daniel Bermond < yahoo-com: danielbermond >

pkgname=kvazaar
pkgver=1.1.0
pkgrel=4
pkgdesc="An open-source HEVC encoder licensed under LGPLv2.1"
arch=('i686' 'x86_64')
url="http://ultravideo.cs.tut.fi/#encoder"
license=('LGPL2.1')
depends=('glibc' 'gcc-libs' 'crypto++')
makedepends=('yasm')
provides=('libkvazaar.so')
conflicts=('kvazaar-git')
source=("$pkgname"-"$pkgver".tar.gz::"https://github.com/ultravideo/kvazaar/archive/v${pkgver}.tar.gz"
        'kvazaar-1.1.0-gcc7-fix.patch')
sha256sums=('8e382738a51004bfcfca4c832e8b41fe6a17f889f3c39151dc1c1a37261a3a6d'
            'f4f5f25012ad8e659ba404f381acbd60035769c9ce89909fda509711078686ff')

prepare() {
    cd "${pkgname}-${pkgver}"
    ./autogen.sh
    patch -Np1 -i "${srcdir}/kvazaar-1.1.0-gcc7-fix.patch"
}

build() {
    cd "${pkgname}-${pkgver}"
    ./configure \
        --prefix=/usr \
        --enable-largefile \
        --enable-static=no \
        --enable-shared=yes \
        --enable-fast-install=yes \
        --with-cryptopp
    make
}

package() {
    cd "${pkgname}-${pkgver}"
    make DESTDIR="$pkgdir/" install
}
