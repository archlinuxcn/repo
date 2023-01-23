# Maintainer: madmurphy <madmurphy333 AT gmail DOT com>
# Contributor: midgard <arch.midgard AT janmaes DOT com> 
# Contributor: TrialnError <autumn-wind AT web DOT de>
# Contributor: Yardena Cohen <yardenack AT gmail DOT com>
# Contributor: Max Roder <maxroder AT web DOT de>
# Contributor: Sebastian Jug <seb AT stianj DOT ug>
# Contributor: BrLi

#
# Before running makepkg, you must do this (as normal user):
#
#     gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org
#
# If you want to update tor-browser from AUR without AUR helpers you can run in a terminal:
#
#     tor-browser -u


pkgname='tor-browser'
pkgver='12.0.2'
pkgrel=1
pkgdesc='Tor Browser Bundle: anonymous browsing using Firefox and Tor'
url='https://www.torproject.org/projects/torbrowser.html'
arch=('i686' 'x86_64')
license=('GPL')
depends=('libxt' 'startup-notification' 'mime-types' 'dbus-glib'
	'alsa-lib' 'desktop-file-utils' 'hicolor-icon-theme'
	'libvpx' 'icu' 'libevent' 'nss' 'hunspell' 'sqlite')
optdepends=('zenity: simple dialog boxes'
	'kdialog: KDE dialog boxes'
	'gst-plugins-good: H.264 video'
	'gst-libav: H.264 video'
	'libpulse: PulseAudio audio driver'
	'libnotify: Gnome dialog boxes')
install="${pkgname}.install"
validpgpkeys=('EF6E286DDA85EA2A4BA7DE684E2C6E8793298290')

_tag_i686='linux32'
_tag_x86_64='linux64'
_urlbase="https://dist.torproject.org/torbrowser/${pkgver}"
_archstr=$([[ "${CARCH}" == 'x86_64' ]] && echo -n "${_tag_x86_64}" || echo -n "${_tag_i686}")
_pkgsuffx='ALL'

# Syntax: _dist_checksum 'linux32'/'linux64'
_dist_checksum() {

	(curl --silent --fail "${_urlbase}/sha256sums-signed-build.txt" || \
		curl --silent --fail "${_urlbase}/sha256sums-unsigned-build.txt") | \
		grep "${1}-${pkgver}_${_pkgsuffx}.tar.xz\$" | cut -d ' ' -f1

}

# Make a string suitable for `sed`, by escaping `[]/&$.*^\` - syntax: `_sed_escape STRING`
_sed_escape() {
	echo "${1}" | sed 's/[]\/&.*$^[]/\\&/g'
}

source_i686=("${_urlbase}/${pkgname}-${_tag_i686}-${pkgver}_${_pkgsuffx}.tar.xz"{,.asc})
source_x86_64=("${_urlbase}/${pkgname}-${_tag_x86_64}-${pkgver}_${_pkgsuffx}.tar.xz"{,.asc})
source=("${pkgname}.desktop.in"
	"${pkgname}.in"
	"${pkgname}.png"
	"${pkgname}.svg")

### IMPORTANT #################################################################
# No need for `makepkg -g`: the following sha256sums¸don't need to be updated #
# with each release, everything is done automatically! Leave them like this!  #
###############################################################################
sha256sums=('5dd2b61bd4edf4d1499a81127f97a1de7ec272a885df97331b61969a5a07f05f'
            '1143d23e347605b498b3793992e84e95563efd94aa4da17837b37104a6d4a090'
            'f25ccf68b47f5eb14c6fec0664c74f30ea9c6c58d42fc6abac3b64670aaa3152'
            '7b28b5dbe8ad573bb46e61b4d542b33e01ca240825ca640b4893fee6203b021f')
sha256sums_i686=("$(_dist_checksum "${_tag_i686}")"
                 'SKIP')
sha256sums_x86_64=("$(_dist_checksum "${_tag_x86_64}")"
                   'SKIP')

noextract=("${pkgname}-${_tag_i686}-${pkgver}_${_pkgsuffx}.tar.xz"
           "${pkgname}-${_tag_x86_64}-${pkgver}_${_pkgsuffx}.tar.xz")

package() {

	cd "${srcdir}"

	local _sed_subst="
		s/@PACKAGE_NAME@/$(_sed_escape "${pkgname}")/g
		s/@PACKAGE_VERSION@/$(_sed_escape "${pkgver}")/g
		s/@PACKAGE_RELEASE@/$(_sed_escape "${pkgrel}")/g
		s/@PACKAGE_SUFFIX@/$(_sed_escape "${_pkgsuffx}")/g
		s/@PACKAGE_ARCH@/$(_sed_escape "${_archstr}")/g
	"

	install -dm755 "${pkgdir}/usr/bin"
	sed "${_sed_subst}" "${pkgname}.in" > "${pkgdir}/usr/bin/${pkgname}"
	chmod +x "${pkgdir}/usr/bin/${pkgname}"

	install -dm755 \
		"${pkgdir}/usr/share/icons/hicolor/scalable/apps" \
		"${pkgdir}/usr/share/icons/hicolor/128x128/apps"

	install -Dm644 "${srcdir}/${pkgname}.png" "${pkgdir}/usr/share/icons/hicolor/128x128/apps/${pkgname}.png"
	install -Dm644 "${srcdir}/${pkgname}.svg" "${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg"

	install -dm755 "${pkgdir}/usr/share/applications"
	sed "${_sed_subst}" "${pkgname}.desktop.in" > \
		"${pkgdir}/usr/share/applications/${pkgname}.desktop"

	install -Dm444 "${pkgname}-${_archstr}-${pkgver}_${_pkgsuffx}.tar.xz" \
		"${pkgdir}/opt/${pkgname}/${pkgname}-${_archstr}-${pkgver}_${_pkgsuffx}.tar.xz"

}


