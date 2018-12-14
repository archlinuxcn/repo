# Maintainer: grufo <madmurphy333 AT gmail DOT com>
# Contributor: midgard <arch.midgard AT janmaes DOT com>
# Contributor: TrialnError <autumn-wind AT web DOT de>
# Contributor: Yardena Cohen <yardenack AT gmail DOT com>
# Contributor: Max Roder <maxroder AT web DOT de>
# Contributor: Sebastian Jug <seb AT stianj DOT ug>
# Contributor: Yao YongPeng <iyao.yongpeng AT gmail DOT com>

#
# Before running makepkg, you must do this:
#
# gpg --keyserver hkp://pgp.mit.edu:11371 --recv-keys 0x4E2C6E8793298290
#

# To port this PKGBUILD to another language of tor-browser you have to
# change ONLY the variable ${_language} below

_language='zh-CN'

# This PKGBUILD is based on https://aur.archlinux.org/packages/tor-browser/

_pkgname='tor-browser'
pkgname="${_pkgname}-${_language,,}"
pkgver='8.0.4'
pkgrel='1'
pkgdesc="Tor Browser Bundle: anonymous browsing using Firefox and Tor (${_language})"
url='https://www.torproject.org/projects/torbrowser.html'
arch=('i686' 'x86_64')
_idstr32='linux32'
_idstr64='linux64'
license=('GPL')
depends=('gtk2' 'mozilla-common' 'libxt' 'startup-notification' 'mime-types'
	'dbus-glib' 'alsa-lib' 'desktop-file-utils' 'hicolor-icon-theme'
	'libvpx' 'icu' 'libevent' 'nss' 'hunspell' 'sqlite')
optdepends=('zenity: simple dialog boxes'
	'kdialog: KDE dialog boxes'
	'gst-plugins-good: H.264 video'
	'gst-libav: H.264 video'
	'libpulse: PulseAudio audio driver'
	'libnotify: Gnome dialog boxes')
install="${_pkgname}.install"

_archstr=$([[ "${CARCH}" == 'x86_64' ]] && echo -n "${_idstr64}" || echo -n "${_idstr32}")

validpgpkeys=('EF6E286DDA85EA2A4BA7DE684E2C6E8793298290')

source_i686=("https://dist.torproject.org/torbrowser/${pkgver}/${_pkgname}-${_idstr32}-${pkgver}_${_language}.tar.xz"{,.asc})
source_x86_64=("https://dist.torproject.org/torbrowser/${pkgver}/${_pkgname}-${_idstr64}-${pkgver}_${_language}.tar.xz"{,.asc})
source=("${_pkgname}.desktop"
	"${_pkgname}.png"
	"${_pkgname}.sh")

sha256sums=('e9b6620a5683b2df7878d35a087039bf4449eb8648361a12ddbd968d98b59e8b'
            '17fc2f5784d080233aca16e788d62ab6fe3e57cf781b123cfe32767de97d6d3b'
            '3a491ad1a476f2fb343f274eab4e8df925637438e6dac3591f092b3ef3294da3')
sha256sums_i686=('SKIP'
                 'SKIP')
sha256sums_x86_64=('SKIP'
                   'SKIP')

noextract=("${_pkgname}-${_idstr64}-${pkgver}_${_language}.tar.xz"
	"${_pkgname}-${_idstr32}-${pkgver}_${_language}.tar.xz")

package() {

	cd "${srcdir}"

	sed -i "s/__REPL_LANGUAGE__/${_language}/g"	"${_pkgname}.desktop"
	sed -i "s/__REPL_NAME__/${pkgname}/g"		"${_pkgname}.desktop"

	sed -i "s/__REPL_NAME__/${pkgname}/g"		"${_pkgname}.sh"
	sed -i "s/__REPL_VERSION__/${pkgver}/g"		"${_pkgname}.sh"
	sed -i "s/__REPL_RELEASE__/${pkgrel}/g"		"${_pkgname}.sh"
	sed -i "s/__REPL_LANGUAGE__/${_language}/g"	"${_pkgname}.sh"
	sed -i "s/__REPL_ARCH__/${_archstr}/g"		"${_pkgname}.sh"

	install -Dm 644 "${_pkgname}.desktop"	"${pkgdir}/usr/share/applications/${pkgname}.desktop"
	install -Dm 644 "${_pkgname}.png"	"${pkgdir}/usr/share/pixmaps/${pkgname}.png"
	install -Dm 755 "${_pkgname}.sh"	"${pkgdir}/usr/bin/${pkgname}"

	install -Dm 644 "${_pkgname}-${_archstr}-${pkgver}_${_language}.tar.xz" "${pkgdir}/opt/${pkgname}/${_pkgname}-${_archstr}-${pkgver}_${_language}.tar.xz"

}
