# $Id: PKGBUILD 258410 2016-01-19 13:36:55Z heftig $
# Maintainer: Aaron Griffin <aaron@archlinux.org>

pkgname=goffice0.8
pkgver=0.8.17
pkgrel=4
pkgdesc="A library of document-centric objects and utilities built on top of GLib and Gtk+"
arch=('i686' 'x86_64')
url="http://www.gnome.org"
license=('GPL')
depends=('gtk2' 'gconf' 'libgsf')
conflicts=('goffice<0.10')
makedepends=('intltool' 'gtk-doc')
source=(https://download.gnome.org/sources/goffice/${pkgver%.*}/goffice-${pkgver}.tar.xz
        use-apiver-for-dirs.patch)
sha256sums=('165070beb67b84580afe80a8a100b674a81d553ab791acd72ac0c655f4fadb15'
            '4507a49f6ccb13e55c0b3cc6831b7e0dcec7badb58a3661190e843f8607fa270')

build() {
  cd "${srcdir}/goffice-${pkgver}"
  patch -Np0 -i "${srcdir}/use-apiver-for-dirs.patch"
  sed -i -e 's/glib\/gregex.h/glib.h/' configure.in
  autoreconf -fi
  ./configure --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var --disable-static
  make CFLAGS="${CFLAGS} -Wno-error=format-nonliteral"
}

package() {
  cd "${srcdir}/goffice-${pkgver}"
  make DESTDIR="${pkgdir}" install
}
