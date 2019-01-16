# Maintainer: Piotr Rogoża <rogoza dot piotr at gmail dot com>
# vim:set ts=2 sw=2 et ft=sh tw=100: expandtab

pkgname=gnome-panel2
_pkgname=gnome-panel
pkgver=2.32.1
_pkgver=${pkgver%.*}
pkgrel=2
pkgdesc="The GNOME Panel (legacy version)"
arch=('i686' 'x86_64')
url="http://www.gnome.org"
license=('GPL')
groups=()
depends=()
depends=(hicolor-icon-theme libgweather2 librsvg gnome-desktop2 libwnck libsm libbonoboui gnome-menus2)
makedepends=(gnome-menus2 libgweather2 gnome-doc-utils intltool gobject-introspection networkmanager libcanberra)
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=('!libtool' '!emptydirs')
install=gnome-panel.install
source=(http://ftp.gnome.org/pub/GNOME/sources/${_pkgname}/${_pkgver}/${_pkgname}-$pkgver.tar.bz2)
noextract=()

build(){
  cd "${srcdir}/${_pkgname}-${pkgver}"
  export LDFLAGS='-lX11'

  PYTHON=/usr/bin/python2 ./configure --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var --disable-static \
      --libexecdir=/usr/lib/gnome-panel \
      --with-in-process-applets=all \
      --disable-schemas-compile \
      --disable-scrollkeeper \
      CFLAGS="${CFLAGS} $(pkg-config --cflags --libs gmodule-2.0)" \
      LIBS="-lm" 
  make
}
package(){
  cd "$srcdir/$_pkgname-$pkgver"
  make GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR="${pkgdir}" install

  install -m755 -d "${pkgdir}/usr/share/gconf/schemas"
  gconf-merge-schema "${pkgdir}/usr/share/gconf/schemas/${_pkgname}.schemas" --domain gnome-panel-3.0 ${pkgdir}/etc/gconf/schemas/*.schemas
  rm -f ${pkgdir}/etc/gconf/schemas/*.schemas
}
md5sums=('a228035e1f7026abf296b797f1f7d2f9')
