# Maintainer: FadeMind <fademind@gmail.com>
# Contributor: Jameson Pugh <imntreal@gmail.com>

pkgbase=lib32-libindicator
pkgname=('lib32-libindicator-gtk2' 'lib32-libindicator-gtk3')
pkgver=12.10.1
pkgrel=4
pkgdesc="Libary with a set of symbols and convience functions that all indicators would like to use"
arch=('i686' 'x86_64')
url="https://launchpad.net/libindicator"
license=('GPL')
makedepends=(gcc-multilib lib32-gtk{2,3})
options=('!libtool')
install=${pkgbase}.install
source=("libindicator-${pkgver}.tar.gz::${url}/${pkgver%.*}/${pkgver}/+download/libindicator-${pkgver}.tar.gz")
sha256sums=('b2d2e44c10313d5c9cd60db455d520f80b36dc39562df079a3f29495e8f9447f')

prepare() {
    sed '/-Werror/s/$/ -Wno-deprecated-declarations/' -i                libindicator-${pkgver}/libindicator/Makefile.{am,in}
    sed 's/LIBINDICATOR_LIBS+="$LIBM"/LIBINDICATOR_LIBS+=" $LIBM"/g' -i libindicator-${pkgver}/configure
    sed 's/LIBM="-lmw"/LIBM=" -lmw"/g' -i                               libindicator-${pkgver}/configure
    sed 's/LIBM="-lm"/LIBM=" -lm"/g' -i                                 libindicator-${pkgver}/configure
    sed 's/LIBS="-lm  $LIBS"/LIBS=" -lm  $LIBS"/g' -i                   libindicator-${pkgver}/configure
    sed 's/LIBS="-lmw  $LIBS"/LIBS=" -lmw  $LIBS"/g' -i                 libindicator-${pkgver}/configure
    sed 's/LIBM="-lm"/LIBM=" -lm"/g' -i                                 libindicator-${pkgver}/m4/libtool.m4
    rm -rf libindicator-gtk{2,3} &> /dev/null
    cp -r "libindicator-${pkgver}" "libindicator-gtk2"
    mv    "libindicator-${pkgver}" "libindicator-gtk3"
}

build() {
    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    cd "${srcdir}/libindicator-gtk3"
    ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib32/libindicator-gtk3 \
                --libdir=/usr/lib32 --disable-{static,tests}
    make

    cd "${srcdir}/libindicator-gtk2"
    ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib32/libindicator-gtk2 \
                --libdir=/usr/lib32 --disable-{static,tests} --with-gtk=2
    make
}

package_lib32-libindicator-gtk3() {
    pkgdesc="Libary with a set of symbols and convience functions that all indicators would like to use (GTK+ 3 library)"
    depends=('lib32-gtk3' 'libindicator-gtk3')
    cd "${srcdir}/libindicator-gtk3"

    make -j1 DESTDIR="$pkgdir/" install
    rm -rf "${pkgdir}"/usr/{include,share,bin}
}

package_lib32-libindicator-gtk2() {
    pkgdesc="Libary with a set of symbols and convience functions that all indicators would like to use (GTK+ 2 library)"
    depends=('lib32-gtk2' 'libindicator-gtk2')
    provides=('lib32-libindicator')
    conflicts=('lib32-libindicator')
    cd "${srcdir}/libindicator-gtk2"

    make -j1 DESTDIR="$pkgdir/" install
    rm -rf "${pkgdir}"/usr/{include,share,bin}
}
