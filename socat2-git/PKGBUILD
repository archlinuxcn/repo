# Maintainer: Yen Chi Hsuan <yan12125 at gmail.com>
#
# This is based on AUR packages socat2. The original maintainer is:
# Maintainer: Stefan Haller <haliner@googlemail.com>
#
# The original PKGBUILD for socat in the official repository was written by:
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Juergen Hoetzel <juergen@archlinux.org>
# Contributor: John Proctor <jproctor@prium.net>

_pkgname=socat2
pkgname=${_pkgname}-git
pkgver=2.0.0.b9.0.g7beb9b3
pkgrel=3
pkgdesc='Multipurpose relay (development version)'
url='http://www.dest-unreach.org/socat/socat-version2.html'
license=('GPL2')
arch=('i686' 'x86_64')
depends=('readline' 'openssl-1.0')
makedepends=('yodl' 'git')
source=(
    "$_pkgname"::"git+http://repo.or.cz/socat.git#branch=socat2"
    sslv3.patch
)
sha256sums=('SKIP'
            '3744575806f489ad0d3673e6a397badd4b61ecbd6e474ece67b347e13c5076b5')

pkgver() {
    cd "${srcdir}/${_pkgname}"

    git describe --long --tags | sed 's/^tag-//;s/-/./g'
}

prepare() {
    cd "${srcdir}/${_pkgname}"

    patch -Np1 -i ../sslv3.patch
}

build() {
    cd "${srcdir}/${_pkgname}"

    msg "Running autoconf..."
    autoconf

    CPPFLAGS="-I/usr/include/openssl-1.0" \
    LDFLAGS="-L/usr/lib/openssl-1.0" \
    ./configure \
        --prefix=/usr \
        --mandir=/usr/share/man \

    make
}

package() {
    cd "${srcdir}/${_pkgname}"

    make DESTDIR="${pkgdir}" install

    # Make it co-installable with socat
    find "${pkgdir}/usr/bin/" -type f -executable -exec mv {} {}2 \;
    find "${pkgdir}/usr/share/man" -type f | while read manfile
    do
        mv $manfile ${manfile%.*}2.${manfile##*.}
    done
}
