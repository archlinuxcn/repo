# $Id$
# Maintainer: Allen Zhong <moeallenz@gmail.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Daenyth <Daenyth+Arch [at] gmail [dot] com>
# Contributor: Jeff Mickey <jeff@archlinux.org>
# Contributor: sh__

_pkgname=libtorrent
pkgname=libtorrent-ipv6
pkgver=0.13.6
pkgrel=4
pkgdesc='BitTorrent library with a focus on high performance and good code, with ipv6 support'
url='http://rakshasa.github.io/rtorrent/'
arch=('x86_64')
license=('GPL')
depends=('openssl')
makedepends=('git')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
source=("$_pkgname-$pkgver::git+https://github.com/rakshasa/libtorrent.git#commit=9eb9ba21720e544af3550f59900318a9b4d4a532")
sha256sums=('SKIP')

prepare() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    sed '/AM_PATH_CPPUNIT/d' -i configure.ac
}

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    ./autogen.sh

    export CXXFLAGS="${CXXFLAGS} -std=c++11 -fno-strict-aliasing"
    ./configure \
        --prefix=/usr \
        --disable-debug

    make
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
