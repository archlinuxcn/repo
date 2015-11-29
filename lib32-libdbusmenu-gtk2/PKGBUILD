# Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgbase=libdbusmenu
_pkgbasename=libdbusmenu-gtk2
pkgname=lib32-libdbusmenu-gtk2
pkgver=12.10.2
pkgrel=10
pkgdesc="Small library that passes a menu structure across DBus (GTK+ 2 library) (32-bit)"
arch=('x86_64')
url="https://launchpad.net/libdbusmenu"
license=('GPL3')
depends=('lib32-gtk2' 'lib32-libdbusmenu-glib' "$_pkgbasename")
makedepends=('gcc-multilib' 'intltool' 'gnome-doc-utils' 'gobject-introspection' 'vala' 'lib32-json-glib')
options=('!emptydirs')
install=$pkgname.install
source=(http://launchpad.net/dbusmenu/${pkgver%.*}/$pkgver/+download/$_pkgbase-$pkgver.tar.gz)
sha256sums=('9d6ad4a0b918b342ad2ee9230cce8a095eb601cb0cee6ddc1122d0481f9d04c9')

build() {
  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  cd "$srcdir/$_pkgbase-$pkgver"
  sed -i 's@^#!.*python$@#!/usr/bin/python2@' tools/dbusmenu-bench
  for _file in $(grep -lr g_type_init ./*); do
    sed -i '/g_type_init();/d' $_file
  done

  ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib/$pkgname \
              --libdir=/usr/lib32 --disable-static --with-gtk=2
  make
}

package() {
  cd "$srcdir/$_pkgbase-$pkgver"

  make -j1 -C libdbusmenu-glib DESTDIR="$pkgdir/" install
  make -j1 -C libdbusmenu-gtk DESTDIR="$pkgdir/" install
  make -j1 -C libdbusmenu-glib DESTDIR="$pkgdir/" uninstall

  rm -rf "${pkgdir}"/usr/{include,share,bin}
}
