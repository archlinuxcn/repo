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
pkgrel=3
pkgdesc='BitTorrent library with a focus on high performance and good code, with ipv6 support'
url='http://rakshasa.github.io/rtorrent/'
arch=('i686' 'x86_64')
license=('GPL')
depends=('openssl')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
source=("$_pkgname-$pkgver.tar.gz::https://github.com/rakshasa/${_pkgname}/archive/${pkgver}.tar.gz"
        "${_pkgname}-ipv6.patch"
        libtorrent-openssl-1.1.patch::"https://github.com/rakshasa/libtorrent/commit/4607bbf7.patch"
        fixing-memleak-with-getifaddrs.patch::"https://github.com/inste/libtorrent/commit/bdf08623.patch")
sha256sums=('bf963ac6e73e194a2cd87ebdf809988b5b3d6244bb7cd43d7d0c4852fc501524'
            'e359fe6ab6671c4db25c1cda92e0604d12943dc693abbdccd0a9d8a356581526'
            '82f639c1e7cf3299c2a44a705e69286abd33a75c70d2da0594d41d5a08cd8c1a'
            '513b14dda844082f90b486384d853ddaa316652ba5cb5f8e31c819878d0c59ba')

prepare() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    patch -uNp1 -i "${srcdir}/${_pkgname}-ipv6.patch"
    # https://github.com/inste/libtorrent/commit/bdf086234cc6ea07364c6ef20e08c5fc504b70db
    patch -uNp1 -i "${srcdir}/fixing-memleak-with-getifaddrs.patch"
    sed '/AM_PATH_CPPUNIT/d' -i configure.ac
    # fix build against openssl 1.1
    patch -uNp1 -i "${srcdir}"/libtorrent-openssl-1.1.patch
}

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    ./autogen.sh

    export CXXFLAGS="${CXXFLAGS} -fno-strict-aliasing"
    ./configure \
        --prefix=/usr \
        --disable-debug

    make
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
