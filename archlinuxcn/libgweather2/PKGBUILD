# Maintainer: Piotr Rogoża <rogoza dot piotr at gmail dot com>
# Contributor: Piotr Rogoża <rogoza dot piotr at gmail dot com>

pkgname=libgweather2
_pkgname=libgweather
pkgver=2.91.6
_pkgver=${pkgver%.*}
pkgrel=1
pkgdesc="Provides access to weather information from the net (legacy version)"
arch=('i686' 'x86_64')
url="http://www.gnome.org/"
license=('GPL')
depends=(gconf libsoup gtk2)
makedepends=('pkgconfig' 'intltool' 'gtk-doc' 'gobject-introspection' 'gnome-common')
provides=(libgweather)
conflicts=(libgweather)
options=('!libtool' '!emptydirs')
# install='libgweather.install'
source=(http://ftp.gnome.org/pub/GNOME/sources/${_pkgname}/${_pkgver}/${_pkgname}-${pkgver}.tar.bz2)
sha256sums=('186b7ed8f8fbeb50ddd39e9f4518163a0dcfde17be72a5e85af2d271b3a337bf')

build(){
  cd "$srcdir/$_pkgname-$pkgver"

  gtkdocize
#  autoreconf -fi
  _configure=(
    --prefix=/usr
    --sysconfdir=/etc
    --localstatedir=/var
    --disable-static
    --enable-locations-compression
  )
  ./configure ${_configure[@]}
  make
}
package(){
  cd "$srcdir/$_pkgname-$pkgver"

  make GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR="${pkgdir}" install

  install -m755 -d "${pkgdir}/usr/share/gconf/schemas"
  gconf-merge-schema "${pkgdir}/usr/share/gconf/schemas/${pkgname}.schemas" --domain libgweather ${pkgdir}/etc/gconf/schemas/*.schemas
  rm -f ${pkgdir}/etc/gconf/schemas/*.schemas
}
