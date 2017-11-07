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
pkgver='7.0.9'
pkgrel='1'
pkgdesc='Tor Browser Bundle: Anonymous browsing using firefox and tor (international PKGBUILD)'
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

_archstr=$([[ "${CARCH}" == 'x86_64' ]] && echo -n "${_idstr64}" || echo -n "${_idstr32}")

_localetor() {

	#
	# Checking if a `tor-browser` package exists for current locale; a different language can be
	# chosen by giving a `TORBROWSER_PKGLANG` environment variable to `makepkg`, for instance:
	#
	#	TORBROWSER_PKGLANG='en-US' makepkg
	#

	if [[ -z "${TORBROWSER_PKGLANG}" ]]; then

		local _urlbase="https://dist.torproject.org/torbrowser/${pkgver}/${pkgname}-${_archstr}-${pkgver}"
		local _fulllocale="$(locale | grep LANG | cut -d= -f2 | cut -d. -f1 | sed s/_/\-/)"
		local _shortlocale="$(locale | grep LANG | cut -d= -f2 | cut -d_ -f1)"

		if curl --output /dev/null --silent --head --fail "${_urlbase}_${_fulllocale}.tar.xz"; then
			echo -n "${_fulllocale}"
		elif curl --output /dev/null --silent --head --fail "${_urlbase}_${_shortlocale}.tar.xz"; then
			echo -n "${_shortlocale}"
		else
			echo -n 'en-US'
		fi

	else

		echo -n "${TORBROWSER_PKGLANG}"

	fi

}

validpgpkeys=('EF6E286DDA85EA2A4BA7DE684E2C6E8793298290')

_language="$(_localetor)"

source_i686=("https://dist.torproject.org/torbrowser/${pkgver}/${pkgname}-${_idstr32}-${pkgver}_${_language}.tar.xz"{,.asc})
source_x86_64=("https://dist.torproject.org/torbrowser/${pkgver}/${pkgname}-${_idstr64}-${pkgver}_${_language}.tar.xz"{,.asc})
source=("${pkgname}.desktop"
	"${pkgname}.png"
	"${pkgname}.sh")

md5sums=('914bc94601657ac143f21acd8ed75747'
	'494afbfa60fb4ce21840244cc3f7208c'
	'120910366e4094c652fe7c4ee55abbca')
md5sums_i686=('SKIP'
	'SKIP')
md5sums_x86_64=('SKIP'
	'SKIP')

noextract=("${pkgname}-${_idstr64}-${pkgver}_${_language}.tar.xz"
	"${pkgname}-${_idstr32}-${pkgver}_${_language}.tar.xz")

package() {

	# use colors only if we have them
	if [[ $(which tput > /dev/null 2>&1 && tput -T "${TERM}" colors || echo -n '0') -ge 8 ]] ; then
		local _COL_YELLOW_='\e[0;33m'
		local _COL_LIGHTGREY_='\e[0;37m'
		local _COL_BRED_='\e[1;31m'
		local _COL_BBLUE_='\e[1;34m'
		local _COL_BWHITE_='\e[1;37m'
		local _COL_DEFAULT_='\e[0m'
	fi

	cd "${srcdir}"

	msg "Packaging ${pkgname} (language: ${_language})..."

	if [[ -z "${TORBROWSER_PKGLANG}" ]]; then
		echo -e "\n  ${_COL_BBLUE_}->${_COL_DEFAULT_} ${_COL_BRED_}NOTE:${_COL_DEFAULT_} If you want to package ${_COL_BWHITE_}${pkgname}${_COL_DEFAULT_} in a different language, please"
		echo -e "     set a \`${_COL_YELLOW_}TORBROWSER_PKGLANG${_COL_DEFAULT_}\` environment variable before running makepkg.\n"
		echo '     For instance:'
		echo -e "\n        ${_COL_LIGHTGREY_}TORBROWSER_PKGLANG='en-US' makepkg${_COL_DEFAULT_}\n"
	fi

	sed -i "s/__REPL_LANGUAGE__/${_language}/g"	"${pkgname}.desktop"

	sed -i "s/__REPL_NAME__/${pkgname}/g"		"${pkgname}.sh"
	sed -i "s/__REPL_VERSION__/${pkgver}/g"		"${pkgname}.sh"
	sed -i "s/__REPL_RELEASE__/${pkgrel}/g"		"${pkgname}.sh"
	sed -i "s/__REPL_LANGUAGE__/${_language}/g"	"${pkgname}.sh"
	sed -i "s/__REPL_ARCH__/${_archstr}/g"		"${pkgname}.sh"

	install -Dm 644 "${pkgname}.desktop"	"${pkgdir}/usr/share/applications/${pkgname}.desktop"
	install -Dm 644 "${pkgname}.png"	"${pkgdir}/usr/share/pixmaps/${pkgname}.png"
	install -Dm 755 "${pkgname}.sh"		"${pkgdir}/usr/bin/${pkgname}"

	install -Dm 644 "${pkgname}-${_archstr}-${pkgver}_${_language}.tar.xz" "${pkgdir}/opt/${pkgname}/${pkgname}-${_archstr}-${pkgver}_${_language}.tar.xz"

}
