# $Id: PKGBUILD 106614 2014-03-05 23:48:29Z flexiondotorg $
# Maintainer : Martin Wimpress <code@flexion.org>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Hugo Doria <hugo@archlinux.org>

pkgname=system-tools-backends
pkgver=2.10.2
pkgrel=5
pkgdesc='Backends for Gnome/MATE System Tools.'
arch=('i686' 'x86_64')
url='http://system-tools-backends.freedesktop.org/'
license=('GPL')
depends=('dbus-glib' 'perl' 'perl-net-dbus' 'polkit')
makedepends=('intltool' 'perl-xml-parser')
source=("http://ftp.gnome.org/pub/gnome/sources/${pkgname}/2.10/${pkgname}-${pkgver}.tar.bz2")
sha256sums=('1dbe5177df46a9c7250735e05e77129fe7ec04840771accfa87690111ca2c670')

build() {
    cd "${pkgname}-${pkgver}"
    ./configure \
        --prefix=/usr \
        --with-dbus-sys=/etc/dbus-1/system.d \
        --localstatedir=/var \
        --mandir=/usr/share \
        --sbindir=/usr/bin \
        --disable-static
    make
}

package() {
    cd "${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
    #clean up man
    rm -rf "${pkgdir}/usr/share/system-tools-backends-2.0/modules/share/"
}