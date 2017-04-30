# Maintainer: Allen Zhong <moeallenz@gmail.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor:  Daenyth <Daenyth [at] gmail [dot] com>
# Contributor: Jeff Mickey <jeff@archlinux.org>
# Contributor: sh__

_pkgname=rtorrent
pkgname=rtorrent-ipv6
pkgver=0.9.6
pkgrel=3
pkgdesc='Ncurses BitTorrent client based on libTorrent, with IPv6 patch'
url='http://rakshasa.github.io/rtorrent/'
license=('GPL')
arch=('i686' 'x86_64')
depends=('libtorrent-ipv6=0.13.6' 'curl' 'xmlrpc-c' 'libsigc++')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
source=("$_pkgname-$pkgver.tar.gz::https://github.com/rakshasa/${_pkgname}/archive/${pkgver}.tar.gz"
        "${_pkgname}-ipv6.patch")
sha256sums=('8ca89ca9e8f0cf984198d030203087e93d24743dfa158091a5d225a70ca4c8cf'
            '3bd16fe842362929a0018bbe4f0aec422a069800b675d04bc1b0246d21171028')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    patch -uNp1 -i "${srcdir}/${_pkgname}-ipv6.patch"
    sed '/AM_PATH_CPPUNIT/d' -i configure.ac
    ./autogen.sh

    export CXXFLAGS="${CXXFLAGS} -std=c++11 -fno-strict-aliasing"
    ./configure \
        --prefix=/usr \
        --disable-debug \
        --with-xmlrpc-c \
        --enable-ipv6

    make
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
    install -D doc/rtorrent.rc "${pkgdir}"/usr/share/doc/rtorrent/rtorrent.rc
}
