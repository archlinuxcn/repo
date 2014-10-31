# Maintainer: ValHue <vhuelamo at gmail dot com>
# https://github.com/ValHue/AUR-PKGBUILDs
#
# $Id: PKGBUILD 198164 2013-10-30 13:11:04Z allan $
# Contributor: Jan Alexander Steffens (heftig) <jan dot steffens at gmail dot com>
# Contributor: Ionut Biru <ibiru at archlinux dot org>
# Contributor: Sergej Pupykin <pupykin.s+arch at gmail dot com>

pkgname=libgee06
_pkgname=libgee
pkgver=0.6.8
pkgrel=1
pkgdesc="GObject collection library (legacy)"
url="http://live.gnome.org/Libgee"
license=('LGPL2.1')
arch=('i686' 'x86_64')
depends=('glib2')
makedepends=('gobject-introspection')
source=("http://ftp.gnome.org/pub/GNOME/sources/${_pkgname}/${pkgver::3}/${_pkgname}-${pkgver}.tar.xz")
sha256sums=('a61f8d796173d41f6144a030d4bd22461f0bb3fa18a3ebe02341b315feebf5d3')

build() {
    cd "${_pkgname}-${pkgver}"
    ./configure --prefix=/usr --disable-static
    make
}

package() {
    cd "${_pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
