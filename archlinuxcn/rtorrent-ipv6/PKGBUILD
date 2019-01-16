# Maintainer: Allen Zhong <moeallenz@gmail.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor:  Daenyth <Daenyth [at] gmail [dot] com>
# Contributor: Jeff Mickey <jeff@archlinux.org>
# Contributor: sh__

_pkgname=rtorrent
pkgname=rtorrent-ipv6
pkgver=0.9.7
pkgrel=1
pkgdesc='Ncurses BitTorrent client based on libTorrent, with IPv6 patch'
url='http://rakshasa.github.io/rtorrent/'
license=('GPL')
arch=('i686' 'x86_64')
depends=('libtorrent-ipv6=0.13.7' 'curl' 'xmlrpc-c' 'libsigc++')
makedepends=('git')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
source=("$_pkgname::git+https://github.com/rakshasa/${_pkgname}.git#commit=5be10fe2513b11368519a2ea984d41e96898bc4c"
        'rtorrent-feature-bind-to-0.9.7.patch')
sha256sums=('SKIP'
            '4ac23255bed12a31763a08d78b206b664db500396a146369aa997b1e1354963b')

prepare() {
    cd "${srcdir}/${_pkgname}"
    patch -Np1 -i ../rtorrent-feature-bind-to-0.9.7.patch
    sed '/AM_PATH_CPPUNIT/d' -i configure.ac
    ./autogen.sh
}

build() {
    cd "${srcdir}/${_pkgname}"
    export CXXFLAGS="${CXXFLAGS} -std=c++11 -fno-strict-aliasing"
    ./configure \
        --prefix=/usr \
        --disable-debug \
        --with-xmlrpc-c \
        --enable-ipv6

    make
}

package() {
    cd "${srcdir}/${_pkgname}"
    make DESTDIR="${pkgdir}" install
    install -D doc/rtorrent.rc "${pkgdir}"/usr/share/doc/rtorrent/rtorrent.rc
}
