# Maintainer: grufo <madmurphy333 AT gmail DOT com>
# Contributor: TrialnError <autumn-wind AT web DOT de>
# Contributor: Yardena Cohen <yardenack AT gmail DOT com>
# Contributor: Max Roder <maxroder AT web DOT de>
# Contributor: Sebastian Jug <seb AT stianj DOT ug>

#
# Before running makepkg, you must do this:
#
# gpg --keyserver hkp://pgp.mit.edu:11371 --recv-keys D1483FA6C3C07136
#

pkgname='tor-browser'
pkgver='7.0.2'
pkgrel=1
pkgdesc='Tor Browser Bundle: Anonymous browsing using firefox and tor (language-agnostic PKGBUILD)'
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
	'gst-plugins-good: h.264 video'
	'gst-libav: h.264 video'
	'libpulse: PulseAudio audio driver'
	'libnotify: Gnome dialog boxes')
install="${pkgname}.install"

_archstr=$([ $CARCH = 'x86_64' ] && echo "${_idstr64}" || echo "${_idstr32}")

_localetor() {

	#
	# Checking if a `tor-browser` package exists for current locale; a different language can be
	# chosen by giving a `TORBROWSER_PKGLANG` environment variable to `makepkg`, for instance:
	#
	#	TORBROWSER_PKGLANG='en-US' makepkg
	#

	if [ -z "${TORBROWSER_PKGLANG}" ]; then

		local _urlbase="https://dist.torproject.org/torbrowser/${pkgver}/${pkgname}-${_archstr}-${pkgver}"
		local _fulllocale="$(locale | grep LANG | cut -d= -f2 | cut -d. -f1 | sed s/_/\-/)"
		local _shortlocale="$(locale | grep LANG | cut -d= -f2 | cut -d_ -f1)"

		if curl --output /dev/null --silent --head --fail "${_urlbase}_${_fulllocale}.tar.xz"; then
			echo -n "${_fulllocale}"
		elif curl --output /dev/null --silent --head --fail "${_urlbase}_${_shortlocale}.tar.xz"; then
			echo -n "${_shortlocale}"
		else
			echo 'en-US'
		fi

	else

		echo "${TORBROWSER_PKGLANG}"

	fi

}

_language="$(_localetor)"

validpgpkeys=('EF6E286DDA85EA2A4BA7DE684E2C6E8793298290')

source_i686=("https://dist.torproject.org/torbrowser/${pkgver}/${pkgname}-${_idstr32}-${pkgver}_${_language}.tar.xz"{,.asc})
source_x86_64=("https://dist.torproject.org/torbrowser/${pkgver}/${pkgname}-${_idstr64}-${pkgver}_${_language}.tar.xz"{,.asc})
source=("${pkgname}.desktop"
	"${pkgname}.install"
	"${pkgname}.png"
	"${pkgname}.sh")

md5sums=('f294787c2d7993b2f6022e6014e582e7'
	'ef1de5f4e269f1084f20122d2703e954'
	'494afbfa60fb4ce21840244cc3f7208c'
	'3ef08aff0e2afebb1a2a7ffbf8f65897')
md5sums_i686=('SKIP'
	'SKIP')
md5sums_x86_64=('SKIP'
	'SKIP')

noextract=("${pkgname}-${_idstr64}-${pkgver}_${_language}.tar.xz"
	"${pkgname}-${_idstr32}-${pkgver}_${_language}.tar.xz")

package() {

	cd "${srcdir}"

	sed -i "s/REPL_LANGUAGE/${_language}/g" "${pkgname}.desktop"

	sed -i "s/REPL_NAME/${pkgname}/g"	"${pkgname}.sh"
	sed -i "s/REPL_VERSION/${pkgver}/g"	"${pkgname}.sh"
	sed -i "s/REPL_LANGUAGE/${_language}/g" "${pkgname}.sh"

	install -Dm 644 "${pkgname}.desktop"	"${pkgdir}/usr/share/applications/${pkgname}.desktop"
	install -Dm 644 "${pkgname}.png"	"${pkgdir}/usr/share/pixmaps/${pkgname}.png"
	install -Dm 755 "${pkgname}.sh"		"${pkgdir}/usr/bin/${pkgname}"

	install -Dm 644 "${pkgname}-${_archstr}-${pkgver}_${_language}.tar.xz" "${pkgdir}/opt/${pkgname}/${pkgname}-${_archstr}-${pkgver}_${_language}.tar.xz"

}
