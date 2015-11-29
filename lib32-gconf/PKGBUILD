# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

pkgname=lib32-gconf
pkgver=3.2.6
pkgrel=1
pkgdesc='A configuration database system'
arch=('x86_64')
license=('LGPL')
url='http://www.gnome.org'
depends=('gconf' 'lib32-dbus-glib' 'lib32-gtk3')
makedepends=('gcc-multilib' 'gobject-introspection' 'intltool' 'python2')
install='gconf.install'
source=("http://ftp.gnome.org/pub/gnome/sources/GConf/3.2/GConf-${pkgver}.tar.xz"
        'gconf-reload.patch'
        '01_xml-gettext-domain.patch')
sha256sums=('1912b91803ab09a5eed34d364bf09fe3a2a9c96751fde03a4e0cfa51a04d784c'
            '567b78d8b4b4bbcb77c5f134d57bc503c34867fcc6341c0b01716bcaa4a21694'
            'c883dec2b96978874a53700cfe7f26f24f8296767203e970bc6402b4b9945eb8')

prepare() {
  cd GConf-${pkgver}

  patch -Np1 -i ../gconf-reload.patch
  patch -Np1 -i ../01_xml-gettext-domain.patch
  sed -i '1s|#!/usr/bin/env python$|&2|' gsettings/gsettings-schema-convert
}

build() {
  cd GConf-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --libexecdir='/usr/lib32/GConf' \
    --sysconfdir='/etc' \
    --localstatedir='/var' \
    --enable-defaults-service \
    --disable-gtk-doc-html \
    --disable-orbit \
    --disable-static \
    --with-gtk='3.0'

  make pkglibdir=/usr/lib32/GConf
}

package() {
  cd GConf-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/{etc,usr/{bin,include,share}}
}

# vim: ts=2 sw=2 et:
