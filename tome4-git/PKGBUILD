# Maintainer: Harms <thotro at lyse dot net>
# Contributor Pascal Grossé <pascal.grosse@gmail.com>

pkgname=tome4-git
_pkgname=tome4
pkgver=1.5.0.r476.g304327e08
pkgrel=1
pkgdesc="An open-source, single-player, role-playing roguelike game set in the world of Eyal."
arch=('i686' 'x86_64')
url="http://tome.te4.org/"
license=('custom' 'GPL3')
depends=('glu' 'openal' 'libvorbis' 'sdl2_ttf>=2.0.12' 'sdl2_image>=2.0.0' )
makedepends=('git' 'premake' 'zip' 'unzip')
options=(!makeflags emptydirs)
source=("git+http://git.net-core.org/tome/t-engine4.git"
	aur-${_pkgname}.patch
	tome4
	tome4.desktop)
provides=('tome4')
conflicts=('tome4-beta' 'tome4' 'tome4-nomusic')
sha256sums=('SKIP'
            '37f5be7020a06228b7d22f4c622ab5a8843b4dbea7493d7e3b324bd592cd818e'
            '3a1e4901337f91697bcfaf095f488c447c27ccc2484a543e31f024d5aefb61a0'
            '80e663d9eb2d41c6d9c0a6b4b5b52eb33b0872c3412a617530777fd137c0baa1')


pkgver() {
    cd "${srcdir}/t-engine4"
    git describe --long --tags | sed -r 's/([^-]*-g)/r\1/;s/-/./g;s/tome.//g'
}

###############################################################################
# 1. Patch the game.
###############################################################################

prepare() {
	cd "$srcdir"/t-engine4
	patch -p1 < "${srcdir}/aur-${_pkgname}.patch"
}

###############################################################################
# 2. Build the game engine from source.
###############################################################################
build() {
	cd t-engine4
	premake4 gmake
	make config=debug
}

###############################################################################
# 3. Create the package. Copy all that shall be installed into the package dir.
###############################################################################
package() {
	# Extract and install the icon.
	cp "${srcdir}/t-engine4/game/engines/default/data/gfx/te4-icon.png"  "${srcdir}"
	install -Dm644 "${srcdir}/te4-icon.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"

	# Install the documents.
	install -Dm644 "${srcdir}/t-engine4/CONTRIBUTING" "${pkgdir}/usr/share/doc/${_pkgname}/CONTRIBUTING"
	install -Dm644 "${srcdir}/t-engine4/CREDITS" "${pkgdir}/usr/share/doc/${_pkgname}/CREDITS"

	# Install the custom license into standard location.
	install -Dm644 "${srcdir}/t-engine4/COPYING" "${pkgdir}/usr/share/licenses/${_pkgname}/COPYING"
	install -Dm644 "${srcdir}/t-engine4/COPYING-MEDIA" "${pkgdir}/usr/share/licenses/${_pkgname}/COPYING-MEDIA"

	# Install the game executable, and the launcher.
	install -Dm755 "${srcdir}/t-engine4/t-engine" "${pkgdir}/opt/${_pkgname}/t-engine"
	install -Dm755 "${srcdir}/${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
	install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"

	# Install the game data.
	cp -r "${srcdir}/t-engine4/bootstrap" "${pkgdir}/opt/${_pkgname}/"
	cp -r "${srcdir}/t-engine4/game" "${pkgdir}/opt/${_pkgname}/"
}
