# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor:  Martin Wimpress <code@flexion.org>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

pkgname=lib32-dbus-glib
pkgver=0.106
pkgrel=1
pkgdesc='GLib bindings for DBUS'
arch=('x86_64')
license=('GPL')
url='http://www.freedesktop.org/wiki/Software/DBusBindings'
depends=('dbus-glib' 'lib32-glib2')
makedepends=('gcc-multilib')
options=('!emptydirs')
source=("http://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-${pkgver}.tar.gz")
sha256sums=('b38952706dcf68bad9c302999ef0f420b8cf1a2428227123f0ac4764b689c046')

build() {
  cd dbus-glib-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --localstatedir='/var' \
    --sysconfdir='/etc' \
    --disable-bash-completion \
    --disable-checks \
    --disable-gtk-doc-html \
    --disable-static
  make
}

package() {
  cd dbus-glib-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}/usr"/{bin,include,share}
}

# vim: ts=2 sw=2 et:
