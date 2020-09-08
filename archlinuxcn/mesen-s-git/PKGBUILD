# Maintainer: CrankySupertoon <crankysupertoon@gmail.com.com>
# Contributor: Andrew O'Neill <andrew at meanjollies dot com>
# Contributor: John Jenkins <twodopeshaggy@gmail.com>
# Contributor: Tony Lambiris <tony@criticalstack.com>

pkgname=mesen-s-git
_pkgname=Mesen-S
pkgver=0.4.0.r14.g6d9dc99
pkgrel=1
pkgdesc='A cross-platform Super Nintendo emulator'
arch=('x86_64')
makedepends=('clang' 'gendesk' 'zip')
depends=('mono' 'sdl2')
url='https://github.com/SourMesen/Mesen-S'
conflicts=('mesen-s')
license=('GPL3')
source=("${_pkgname}::git+https://github.com/SourMesen/Mesen-S.git")
sha256sums=('SKIP')

pkgver() {
	cd "${srcdir}/${_pkgname}"

	git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
	cd "${srcdir}/${_pkgname}"

	# Prevent duplicate .desktop from getting created
	sed -i 's/CreateShortcutFile(desktopFile, mimeTypes);//' UI/Config/FileAssociationHelper.cs

	gendesk --pkgname "${_pkgname}" --pkgdesc "${pkgdesc}" --exec "/usr/bin/mesen-s" -n

	# Invoke using mono in a wrapper, since wine (if installed) would open it otherwise
	cat > "${pkgname}" <<-EOT
	#!/bin/sh
	/usr/bin/mono /opt/Mesen-S/Mesen-S "\$@"
	EOT
}

build() {
	cd "${srcdir}/${_pkgname}"

	mkdir -p bin
	make
}

package() {
	cd "${srcdir}/${_pkgname}"

	install -Dm755 "${pkgname}" "${pkgdir}/usr/bin/${pkgname%%-git}"
	install -Dm644 "${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"

	cd "${srcdir}/${_pkgname}/UI/Resources"
	install -Dm644 "MesenSIcon.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"

	cd "${srcdir}/${_pkgname}/bin/x64/Release"
	install -Dm755 "${_pkgname}.exe" "${pkgdir}/opt/${_pkgname}/${_pkgname}"

	cd "${srcdir}/${_pkgname}/InteropDLL/obj.x64"
	install -Dm644 "libMesenSCore.x64.dll" "${pkgdir}/usr/lib/libMesenSCore.dll"
}
