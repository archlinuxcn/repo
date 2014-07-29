# $Id: PKGBUILD 115672 2014-07-14 07:16:56Z lcarlier $
# Maintainer : Ionut Biru <ibiru@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=libx32-libdbus
_pkgbasename=libdbus
pkgver=1.8.6
pkgrel=1
pkgdesc="DBus library (x32 ABI)"
arch=('x86_64')
url="http://www.freedesktop.org/Software/dbus"
license=('GPL' 'custom')
depends=('libx32-glibc' 'libx32-expat' 'libdbus')
makedepends=('gcc-multilib-x32' 'libx32-libx11')
provides=('libx32-dbus-core' 'libx32-dbus')
conflicts=('libx32-dbus-core' 'libx32-dbus')
replaces=('libx32-dbus-core' 'libx32-dbus')
source=(http://dbus.freedesktop.org/releases/dbus/dbus-${pkgver}.tar.gz)
md5sums=('6a08ba555d340e9dfe2d623b83c0eea8')

build() {
    export CC="gcc -mx32"
    export CXX="g++ -mx32"
    export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

    cd "${srcdir}/dbus-${pkgver}"

    ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --libdir=/usr/libx32 \
        --libexecdir=/usr/lib/dbus-1.0 --with-dbus-user=81 \
        --with-system-pid-file=/run/dbus.pid \
        --with-console-auth-dir=/run/console/ \
        --enable-inotify --disable-dnotify \
        --disable-verbose-mode --disable-static \
        --disable-tests --disable-asserts --disable-systemd		

    make
}

package() {
    cd "${srcdir}/dbus-${pkgver}"
    make DESTDIR=${pkgdir} install

    rm -rf "${pkgdir}"/usr/{bin,include,lib,share}
    rm -rf "${pkgdir}"/{etc,var}

    mkdir -p "${pkgdir}/usr/share/licenses"
    ln -s ${_pkgbasename} "${pkgdir}/usr/share/licenses/${pkgname}"
}
