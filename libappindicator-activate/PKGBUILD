# Maintainer: Sebastian Krzyszkowiak <dos@dosowisko.net>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: bitwave <aur@oomlu.de>
# Contributor: willemw <willemw12@gmail.com>
# Contributor: Balló György <ballogyor+arch@gmail.com>

pkgbase=libappindicator-activate
pkgname=('libappindicator-activate-gtk2' 'libappindicator-activate-gtk3' 'libappindicator-activate-sharp')
pkgver=12.10.0
pkgrel=5
pkgdesc='libappindicator patched to improve user experience under Plasma 5 (single click activation via Activate dbus method)'
arch=('i686' 'x86_64')
url='https://launchpad.net/libappindicator'
license=('LGPL')
makedepends=('dbus-glib' 'gobject-introspection' 'gtk-sharp-2'
             'libdbusmenu-gtk2' 'libdbusmenu-gtk3' 'libindicator-gtk2'
             'libindicator-gtk3' 'mono' 'perl-xml-libxml' 'pygtk' 'vala')
options=('!emptydirs')
source=("http://launchpad.net/libappindicator/${pkgver%.*}/${pkgver}/+download/libappindicator-${pkgver}.tar.gz" "0001-Add-support-for-Activate-method-for-improved-Plasma-.patch")
sha256sums=('d5907c1f98084acf28fd19593cb70672caa0ca1cf82d747ba6f4830d4cc3b49f' 'b5ee550484aebc13eccbee181f355416efa1de917317c00b044266104418526a')

prepare() {
    cd libappindicator-${pkgver}

    sed 's|/cli/|/mono/|' -i bindings/mono/{appindicator-sharp-0.1.pc.in,Makefile.in}
    sed 's/example //g' -i Makefile.in
    patch -p1 < ../0001-Add-support-for-Activate-method-for-improved-Plasma-.patch

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

package_libappindicator-activate-gtk2() {
    depends=('libdbusmenu-gtk2' 'libindicator-gtk2')
    provides=('libappindicator' 'libappindicator-gtk2')
    conflicts=('libappindicator' 'libappindicator-gtk2')

    cd libappindicator-gtk2-${pkgver}

    make -j1 DESTDIR="${pkgdir}" install
    make -j1 -C bindings/mono DESTDIR="${pkgdir}" uninstall
    rm -rf "${pkgdir}"/usr/share/gtk-doc
}

package_libappindicator-activate-gtk3() {
    depends=('libdbusmenu-gtk3' 'libindicator-gtk3')
    provides=('libappindicator3' 'libappindicator-gtk3')
    conflicts=('libappindicator3' 'libappindicator-gtk3')

    cd libappindicator-${pkgver}

    make -j1 DESTDIR="${pkgdir}" install
    make -j1 -C bindings/mono DESTDIR="${pkgdir}" uninstall
    rm -rf "${pkgdir}"/usr/share/gtk-doc
}

package_libappindicator-activate-sharp() {
    arch=('any')
    provides=('libappindicator-sharp')
    conflicts=('libappindicator-sharp')

    cd libappindicator-${pkgver}

    make -j1 -C bindings/mono DESTDIR="${pkgdir}" install
}

# vim: ts=2 sw=2 et:

