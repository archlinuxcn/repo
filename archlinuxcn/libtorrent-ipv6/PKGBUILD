# $Id$
# Maintainer: Allen Zhong <moeallenz@gmail.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Daenyth <Daenyth+Arch [at] gmail [dot] com>
# Contributor: Jeff Mickey <jeff@archlinux.org>
# Contributor: sh__

_pkgname=libtorrent
pkgname=libtorrent-ipv6
pkgver=0.13.7
pkgrel=1
pkgdesc='BitTorrent library with a focus on high performance and good code, with ipv6 support'
url='http://rakshasa.github.io/rtorrent/'
arch=('x86_64')
license=('GPL')
depends=('openssl')
makedepends=('git')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
source=("$_pkgname::git+https://github.com/rakshasa/libtorrent.git#commit=9f15199ce2312350735b1d87e6db033414b41db0"
        'libtorrent-feature-bind-to-0.13.7.patch')
sha256sums=('SKIP'
            'ef0b0ce4378647ac0246dd88f68dc5fbf01336cac13de60e1f4600dd329629f3')

prepare() {
    cd "${srcdir}/${_pkgname}"
    patch -Np1 -i ../libtorrent-feature-bind-to-0.13.7.patch
    sed '/AM_PATH_CPPUNIT/d' -i configure.ac
}

build() {
    cd "${srcdir}/${_pkgname}"
    ./autogen.sh

    export CXXFLAGS="${CXXFLAGS} -std=c++11 -fno-strict-aliasing"
    ./configure \
        --prefix=/usr \
        --disable-debug

    make
}

package() {
    cd "${srcdir}/${_pkgname}"
    make DESTDIR="${pkgdir}" install
}
