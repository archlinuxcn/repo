# Maintainer: Piotr Rogoża <rogoza dot piotr at gmail dot com>
# Contributor: Piotr Rogoża <rogoza dot piotr at gmail dot com>
# vim:set ts=2 sw=2 et ft=sh tw=100: expandtab

pkgname=libgweather2
_pkgname=libgweather
pkgver=2.30.3
_pkgver=${pkgver%.*}
pkgrel=2
pkgdesc="Provides access to weather information from the net (legacy version)"
arch=('i686' 'x86_64')
url="http://www.gnome.org/"
license=('GPL')
groups=()
depends=(gconf libsoup-gnome gtk2)
makedepends=('pkgconfig' 'intltool' 'gtk-doc' 'gobject-introspection' 'gnome-common')
optdepends=()
provides=(libgweather)
conflicts=(libgweather)
replaces=()
backup=()
options=('!libtool' '!emptydirs')
install='libgweather.install'
source=(http://ftp.gnome.org/pub/GNOME/sources/${_pkgname}/${_pkgver}/${_pkgname}-${pkgver}.tar.bz2)
noextract=()

build(){
  cd "$srcdir/$_pkgname-$pkgver"

  gtkdocize
#  autoreconf -fi

  ./configure --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var --disable-static \
      --enable-locations-compression

  make
}
package(){
  cd "$srcdir/$_pkgname-$pkgver"

    make GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR="${pkgdir}" install

    install -m755 -d "${pkgdir}/usr/share/gconf/schemas"
    gconf-merge-schema "${pkgdir}/usr/share/gconf/schemas/${pkgname}.schemas" --domain libgweather ${pkgdir}/etc/gconf/schemas/*.schemas
    rm -f ${pkgdir}/etc/gconf/schemas/*.schemas
}

md5sums=('bf6a0a05051341ecb250f332e3edfb88')
