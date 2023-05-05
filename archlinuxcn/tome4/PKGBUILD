# Maintainer: Harms <thotro at lyse dot net>
# Contributor Pascal Grossé <pascal.grosse@gmail.com>

pkgname=tome4
pkgver=1.7.5
pkgrel=1
pkgdesc="An open-source, single-player, role-playing roguelike game set in the world of Eyal."
arch=('i686' 'x86_64')
url="http://tome.te4.org/"
license=('custom' 'GPL3')
depends=('glu' 'openal' 'libvorbis' 'sdl2_ttf' 'sdl2_image' )
makedepends=('premake' 'zip' 'unzip' 'glew')
options=(!makeflags emptydirs)
source=("http://te4.org/dl/t-engine/t-engine4-src-${pkgver}.tar.bz2"
    aur-${pkgname}.patch
	tome4
	tome4.desktop)
conflicts=('tome4-beta' 'tome4-git' 'tome4-nomusic')
sha256sums=('4a365b10d15c1065e20e193887b4c01e1cce1269699e9d1b3e4533bd58c84ada'
            '8e1821d1fe4bd2b48115179a83d71eaefa8b6bda70de77ca75d122d5d3053410'
            '3a1e4901337f91697bcfaf095f488c447c27ccc2484a543e31f024d5aefb61a0'
            '80e663d9eb2d41c6d9c0a6b4b5b52eb33b0872c3412a617530777fd137c0baa1')

###############################################################################
# 1. Patch the game.
###############################################################################
prepare() {
	cd "$srcdir"/t-engine4-src-${pkgver}
	cp premake4.lua premake5.lua
	patch -p1 < "${srcdir}/aur-${pkgname}.patch"
}

###############################################################################
# 2. Build the game engine from source.
###############################################################################
build() {
	cd t-engine4-src-${pkgver}
	premake5 gmake
	make config=release
}

###############################################################################
# 3. Create the package. Copy all that shall be installed into the package dir.
###############################################################################
package() {
	# Extract and install the icon.
	unzip -oj -qq "${srcdir}/t-engine4-src-${pkgver}/game/engines/te4-${pkgver}.teae" \
		"data/gfx/te4-icon.png" -d "${srcdir}"
	install -Dm644 "${srcdir}/te4-icon.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
	
	# Install the documents.
	install -Dm644 "${srcdir}/t-engine4-src-${pkgver}/CONTRIBUTING" "${pkgdir}/usr/share/doc/${pkgname}/CONTRIBUTING"
	install -Dm644 "${srcdir}/t-engine4-src-${pkgver}/CREDITS" "${pkgdir}/usr/share/doc/${pkgname}/CREDITS"
	
	# Install the custom license into standard location.
	install -Dm644 "${srcdir}/t-engine4-src-${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
	install -Dm644 "${srcdir}/t-engine4-src-${pkgver}/COPYING-MEDIA" "${pkgdir}/usr/share/licenses/${pkgname}/COPYING-MEDIA"

	# Install the game executable, and the launcher.
	install -Dm755 "${srcdir}/t-engine4-src-${pkgver}/t-engine" "${pkgdir}/opt/${pkgname}/t-engine"
	install -Dm755 "${srcdir}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
	install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
	
	# Install the game data.
	cp -r "${srcdir}/t-engine4-src-${pkgver}/bootstrap" "${pkgdir}/opt/${pkgname}/"
	cp -r "${srcdir}/t-engine4-src-${pkgver}/game" "${pkgdir}/opt/${pkgname}/"
}
