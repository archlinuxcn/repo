# Maintainer: Manuel Hüsers <manuel.huesers@uni-ol.de>
# Contributor: Jameson Pugh <imntreal@gmail.com>
# Contributor: Swift Geek < swift geek Ã¢t gmail dÃ¸t cÃ¸m>

_pkgbase='libappindicator'
pkgbase="lib32-${_pkgbase}"
pkgname=("lib32-${_pkgbase}-gtk2" "lib32-${_pkgbase}-gtk3" "lib32-${_pkgbase}-sharp")
#_actual_ver=12.10.1
#_extra_ver=+15.04.20141110
#pkgver=${_actual_ver}${_extra_ver/+/.}
pkgver=12.10.0
pkgrel=7
pkgdesc='Allow applications to export a menu into the Unity Menu bar (32-bit)'
arch=('i686' 'x86_64')
url="https://launchpad.net/${_pkgbase}"
license=('GPL3')
makedepends=('dbus-glib' 'lib32-libdbusmenu-gtk2' 'lib32-libdbusmenu-gtk3'
             'lib32-libindicator-gtk2' 'lib32-libindicator-gtk3' 'gobject-introspection'
              'gtk-doc' 'gtk-sharp-2' 'perl-xml-libxml' 'pygtk' 'vala')
options=('!emptydirs')
#source=("https://launchpad.net/ubuntu/+archive/primary/+files/${_pkgbase}_${_actual_ver}${_extra_ver}.orig.tar.gz"
source=("https://launchpad.net/${_pkgbase}/${pkgver%.*}/${pkgver}/+download/${_pkgbase}-${pkgver}.tar.gz"
        #'0001-Glib.Timeout-fix.patch'
        #'0002-Fix-mono-nunit-pkgconfig-name.patch'
        #'0003-Fix-Mono-assemblies-directory.patch'
        'python-gtfo.patch')
#sha512sums=('328378d86fe81b6e154327ab53fb0d9ead4c2d7eae17f689966c381e65014bdaa91ec675857f6398c740560814346dd28a9de510f847facc9241efaccb2e33a6'
sha512sums=('317a22a23c8ed84e74207b64b2e9683992d1fb7208176637a051dfe925974f966d1cfa31e650b45eaf839ab61641dee8fbebc8a07882a09b0dd766d88b8d5b9a'
            #'e717a7e50ec4828bc4ea1701a4f707ddc695e16dfab2487c0e4f2f85ac50d2d215c99450e4191f0e29d402f0b28bf7b71d5cf2321d3b3b27b396a8bf8f3a393b'
            #'ea1822c3a09ef4c59d91b267d2ea0d0c9003c04ea0d8d4fb6a73e1b51084faccafbf41d6390a9c0e1326fd3334421539bdbb86a2a5e5022fa96e9d5196ef2d1d'
            #'22e15f875a636bbbf8b1e80867a219b4b47b334d1bfe759f4ce79bf3665fc63af36b57fddb6c92aa7db148b5ea9ed789e510a9b23d87324b1b48695ad1ca9bc7'
            '6f65cf77b30edfa00f307f4006383238bd0c993ab2419ebb829cf0b051986e81cbf7c533e317c9d87ca1e967cb5a3faea132bb891b9ef2086a430de4a8d8b5b6')

prepare() {
	#cd "${srcdir}/${_pkgbase}-${_actual_ver}${_extra_ver}"
	cd "${srcdir}/${_pkgbase}-${pkgver}"
	#patch -p1 -i '../0001-Glib.Timeout-fix.patch'
	#patch -p1 -i '../0002-Fix-mono-nunit-pkgconfig-name.patch'
	#patch -p1 -i '../0003-Fix-Mono-assemblies-directory.patch'

	gtkdocize
	autoreconf -vfi

	# not needed in new version
	sed 's|/cli/|/mono/|' -i bindings/mono/{appindicator-sharp-0.1.pc.in,Makefile.in}
	sed 's/example //g' -i Makefile.in
	###########################

	rm -rf 'bindings/python'
	patch -p1 -i '../python-gtfo.patch'

	cd "${srcdir}"
	rm -rf ${_pkgbase}-gtk{2,3} &> /dev/null
	#cp -r "${_pkgbase}-${_actual_ver}${_extra_ver}" "${pkgbase}-gtk2"
	#mv    "${_pkgbase}-${_actual_ver}${_extra_ver}" "${pkgbase}-gtk3"
	cp -r "${_pkgbase}-${pkgver}" "${pkgbase}-gtk2"
	mv    "${_pkgbase}-${pkgver}" "${pkgbase}-gtk3"
}

build() {
	export CC='gcc -m32'
	export CXX='g++ -m32'
	export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
	export CFLAGS+=" -Wno-error=deprecated-declarations"

	#export MCS=/usr/bin/mcs
	#export CSC=/usr/bin/mcs
	#export GMCS=/usr/bin/mcs

	cd "${srcdir}/${pkgbase}-gtk2"
	./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --libdir=/usr/lib32 \
	            --disable-{gtk-doc-html,mono-test,static,tests} --with-gtk=2
	make CSC=dmcs -j1

	cd "${srcdir}/${pkgbase}-gtk3"
	./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --libdir=/usr/lib32 \
	            --disable-{gtk-doc-html,mono-test,static,tests} --with-gtk=3
	make CSC=dmcs -j1
}

package_lib32-libappindicator-gtk2() {
	pkgdesc+=" (GTK+ 2 library)"
	depends=('lib32-libdbusmenu-gtk2' 'lib32-libindicator-gtk2')
	provides=("lib32-${_pkgbase}")
	conflicts=("lib32-${_pkgbase}")

	cd "${srcdir}/${pkgname}"
	make -j1 DESTDIR="${pkgdir}" install
	make -j1 -C bindings/mono DESTDIR="${pkgdir}" uninstall
	rm -rf "${pkgdir}"/usr/{include,share}
}

package_lib32-libappindicator-gtk3() {
	pkgdesc+=" (GTK+ 3 library)"
	depends=('lib32-libdbusmenu-gtk3' 'lib32-libindicator-gtk3')
	provides=("lib32-${_pkgbase}3")
	conflicts=("lib32-${_pkgbase}3")

	cd "${srcdir}/${pkgname}"
	make -j1 -C src DESTDIR="${pkgdir}" install
	make -j1 -C bindings/mono DESTDIR="${pkgdir}" uninstall
	rm -rf "${pkgdir}"/usr/{include,share}
}

package_lib32-libappindicator-sharp() {
	arch=('any')

	cd "${srcdir}/${pkgbase}-gtk3"
	make -C bindings/mono DESTDIR="${pkgdir}" install
	cp -dr --no-preserve=ownership "${pkgdir}/usr/lib/mono/appindicator-sharp" "${pkgdir}/usr/lib32/mono/"
	cp -dr --no-preserve=ownership "${pkgdir}/usr/lib/mono/gac" "${pkgdir}/usr/lib32/mono/"
	rm -rf "${pkgdir}"/usr/{include,share,lib}
}
