# Maintainer: Manuel Hüsers <manuel.huesers@uni-ol.de>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Balló György <ballogyor+arch@gmail.com>
# Contributor: Branchini Massimo <max.bra.gtalk@gmail.com

_pkgbase='libdbusmenu'
pkgbase="lib32-${_pkgbase}"
pkgname=("lib32-${_pkgbase}-glib" "lib32-${_pkgbase}-gtk"{2,3})
pkgver=16.04.0
pkgrel=1
pkgdesc="A library for passing menus over DBus (32-bit)"
arch=('i686' 'x86_64')
url="https://launchpad.net/${_pkgbase}"
license=('GPL3' 'LGPL2.1' 'LGPL3')
makedepends=('gnome-common' 'gnome-doc-utils' 'gobject-introspection' 'intltool' 'vala' 'valgrind-multilib' 'gcc-multilib' 'lib32-gtk'{2,3})
options=('!emptydirs')
source=("https://launchpad.net/libdbusmenu/${pkgver%.?}/${pkgver}/+download/${_pkgbase}-${pkgver}.tar.gz")
sha512sums=('ee9654ac4ed94bdebc94a6db83b126784273a417a645b2881b2ba676a5f67d7fc95dd2bb37bfb0890aa47299ed73cb21ed7de8b75f3fed6b69bfd39065062241')

prepare() {
	cd "${srcdir}"
	rm -rf "${_pkgbase}-gtk"{2,3} &> /dev/null
	cp -rp "${_pkgbase}-${pkgver}" "${pkgbase}-gtk2"
	mv     "${_pkgbase}-${pkgver}" "${pkgbase}-gtk3"
}

build() {
	export CC='gcc -m32'
	export CXX='g++ -m32'
	export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

	export HAVE_VALGRIND_TRUE='#'
	export HAVE_VALGRIND_FALSE=''

	cd "${srcdir}/${pkgbase}-gtk2"
	./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --libdir=/usr/lib32 \
	            --disable-{dumper,static,tests} --with-gtk=2
	make -j1

	cd "${srcdir}/${pkgbase}-gtk3"
	./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --libdir=/usr/lib32 \
	            --disable-{dumper,static,tests} --with-gtk=3
	make -j1
}

package_lib32-libdbusmenu-glib() {
	depends=('lib32-glib2' "${_pkgbase}-glib")

	cd "${srcdir}/${pkgbase}-gtk3"
	make -j1 -C "${_pkgbase}-glib" DESTDIR="${pkgdir}" install
	rm -rf "${pkgdir}"/usr/{include,share,lib,bin}
}

package_lib32-libdbusmenu-gtk2() {
	pkgdesc+=" (GTK+ 2 library)"
	depends=('lib32-gtk2' "lib32-${_pkgbase}-glib" "${_pkgbase}-gtk2")

	cd "${srcdir}/${pkgname}"
	make -j1 -C "${_pkgbase}-glib" DESTDIR="${pkgdir}" install
	make -j1 -C "${_pkgbase}-gtk"  DESTDIR="${pkgdir}" install
	make -j1 -C "${_pkgbase}-glib" DESTDIR="${pkgdir}" uninstall
	rm -rf "${pkgdir}"/usr/{include,share,lib,bin}
}

package_lib32-libdbusmenu-gtk3() {
	pkgdesc+=" (GTK+ 3 library)"
	depends=('lib32-gtk3' "lib32-${_pkgbase}-glib" "${_pkgbase}-gtk3")

	cd "${srcdir}/${pkgname}"
	make -j1 -C "${_pkgbase}-glib" DESTDIR="${pkgdir}" install
	make -j1 -C "${_pkgbase}-gtk"  DESTDIR="${pkgdir}" install
	make -j1 -C "${_pkgbase}-glib" DESTDIR="${pkgdir}" uninstall
	rm -rf "${pkgdir}"/usr/{include,share,lib,bin}
}
