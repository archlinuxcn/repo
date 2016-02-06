# Maintainer: Manuel Hüsers <manuel.huesers@uni-ol.de>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Balló György <ballogyor+arch@gmail.com>
# Contributor: Branchini Massimo <max.bra.gtalk@gmail.com

_pkgbase='libdbusmenu'
pkgbase="lib32-${_pkgbase}"
pkgname=("lib32-${_pkgbase}-gtk2" "lib32-${_pkgbase}-gtk3" "lib32-${_pkgbase}-glib")
_actual_ver=12.10.3
_extra_ver=+15.04.20150410.2
pkgver=${_actual_ver}${_extra_ver/+/.}
pkgrel=1
pkgdesc="A library for passing menus over DBus (32-bit)"
arch=('i686' 'x86_64')
url="https://launchpad.net/${_pkgbase}"
license=('GPL3')
makedepends=('gnome-common' 'gnome-doc-utils' 'gobject-introspection' 'intltool' 'vala' 'gcc-multilib' lib32-gtk{2,3})
options=('!emptydirs')
source=("https://launchpad.net/ubuntu/+archive/primary/+files/${_pkgbase}_${_actual_ver}${_extra_ver}.orig.tar.gz")
sha512sums=('c15b79464bc6498cb1e912efbe648606b7bf3b5c521c4d4e5c7decf002b4e8362444177922a5abd8a057a803a8cc00e72de6e36209189eb255efb83e2ded0b06')

prepare() {
	cd "${srcdir}"
	rm -rf ${_pkgbase}-gtk{2,3} &> /dev/null
	cp -r "${_pkgbase}-${_actual_ver}${_extra_ver}" "${pkgbase}-gtk2"
	mv    "${_pkgbase}-${_actual_ver}${_extra_ver}" "${pkgbase}-gtk3"
}

build() {
	export CC='gcc -m32'
	export CXX='g++ -m32'
	export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

	export HAVE_VALGRIND_TRUE='#'
	export HAVE_VALGRIND_FALSE=''

	cd "${srcdir}/${pkgbase}-gtk2"
	./autogen.sh --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --libdir=/usr/lib32 \
	             --disable-{dumper,static,tests} --with-gtk=2
	make -j1

	cd "${srcdir}/${pkgbase}-gtk3"
	./autogen.sh --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --libdir=/usr/lib32 \
	             --disable-{dumper,static,tests} --with-gtk=3
	make -j1
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

package_lib32-libdbusmenu-glib() {
	depends=('lib32-glib2' "${_pkgbase}-glib")

	cd "${srcdir}/${pkgbase}-gtk3"
	make -j1 -C "${_pkgbase}-glib" DESTDIR="${pkgdir}" install
	rm -rf "${pkgdir}"/usr/{include,share,lib,bin}
}
