# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: bitwave <aur@oomlu.de>
# Contributor: willemw <willemw12@gmail.com>
# Contributor: Balló György <ballogyor+arch@gmail.com>

pkgbase=libappindicator
pkgname=('libappindicator-gtk2' 'libappindicator-gtk3' 'libappindicator-sharp')
pkgver=12.10.0
pkgrel=5
pkgdesc='Allow applications to export a menu into the Unity Menu bar'
arch=('i686' 'x86_64')
url='https://launchpad.net/libappindicator'
license=('LGPL')
makedepends=('dbus-glib' 'gobject-introspection' 'gtk-sharp-2'
             'libdbusmenu-gtk2' 'libdbusmenu-gtk3' 'libindicator-gtk2'
             'libindicator-gtk3' 'mono' 'perl-xml-libxml' 'pygtk' 'vala')
options=('!emptydirs')
source=("http://launchpad.net/libappindicator/${pkgver%.*}/${pkgver}/+download/libappindicator-${pkgver}.tar.gz")
sha256sums=('d5907c1f98084acf28fd19593cb70672caa0ca1cf82d747ba6f4830d4cc3b49f')

prepare() {
  cd libappindicator-${pkgver}

  sed 's|/cli/|/mono/|' -i bindings/mono/{appindicator-sharp-0.1.pc.in,Makefile.in}
  sed 's/example //g' -i Makefile.in

  cd ..

  cp -r libappindicator-${pkgver} libappindicator-gtk2-${pkgver}
}

build() {
  cd libappindicator-${pkgver}

  export CFLAGS="$CFLAGS -Wno-deprecated-declarations"
  export CSC='/usr/bin/mcs'

  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' \
              --disable-{gtk-doc-html,mono-test,static,tests} --with-gtk='3'
  make -j1

  cd ../libappindicator-gtk2-${pkgver}

  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' \
              --disable-{gtk-doc-html,mono-test,static,tests}
  make -j1
}

package_libappindicator-gtk2() {
  depends=('libdbusmenu-gtk2' 'libindicator-gtk2')
  provides=('libappindicator')
  conflicts=('libappindicator')

  cd libappindicator-gtk2-${pkgver}

  make -j1 DESTDIR="${pkgdir}" install
  make -j1 -C bindings/mono DESTDIR="${pkgdir}" uninstall
  rm -rf "${pkgdir}"/usr/share/gtk-doc
}

package_libappindicator-gtk3() {
  depends=('libdbusmenu-gtk3' 'libindicator-gtk3')
  provides=('libappindicator3')
  conflicts=('libappindicator3')

  cd libappindicator-${pkgver}

  make -j1 DESTDIR="${pkgdir}" install
  make -j1 -C bindings/mono DESTDIR="${pkgdir}" uninstall
  rm -rf "${pkgdir}"/usr/share/gtk-doc
}

package_libappindicator-sharp() {
arch=('any')

  cd libappindicator-${pkgver}

  make -j1 -C bindings/mono DESTDIR="${pkgdir}" install
}

# vim: ts=2 sw=2 et:
