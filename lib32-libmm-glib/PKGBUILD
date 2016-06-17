# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=lib32-libmm-glib
pkgver=1.4.14
pkgrel=2
pkgdesc='ModemManager library'
arch=('x86_64')
url='http://www.freedesktop.org/wiki/Software/ModemManager/'
license=('GPL2' 'LGPL2.1')
depends=('lib32-glib2' 'libmm-glib')
makedepends=('gcc-multilib' 'gobject-introspection' 'intltool' 'lib32-libmbim'
             'lib32-libqmi' 'lib32-polkit' 'lib32-systemd' 'python2' 'vala')
source=("http://www.freedesktop.org/software/ModemManager/ModemManager-${pkgver}.tar.xz")
sha256sums=('abe6cdd515a774bcba3afdcdb1e504569801e79282ccdf26099f33cbb8731ba2')

build() {
  cd ModemManager-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --localstatedir='/var' \
    --sbindir='/usr/bin' \
    --sysconfdir='/etc' \
    --disable-gtk-doc-html \
    --disable-static \
    --with-polkit='permissive' \
    --with-udev-base-dir='/usr/lib32/udev'
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make -C libmm-glib
  make -C data
}

package() {
  cd ModemManager-${pkgver}

  make DESTDIR="${pkgdir}" -C libmm-glib install
  make DESTDIR="${pkgdir}" -C data install
  rm -rf "${pkgdir}"/{etc,usr/{include,lib,share}}
}

# vim: ts=2 sw=2 et:
