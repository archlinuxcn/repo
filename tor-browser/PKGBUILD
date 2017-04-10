# Maintainer: grufo <madmurphy333 at gmail dot com>
# Contributor: Yardena Cohen <yardenack at gmail dot com>
# Contributor: Max Roder <maxroder@web.de>
# Contributor: Sebastian Jug <seb AT stianj DOT ug>

pkgname='tor-browser'
pkgver='6.5.1'
pkgrel=1
pkgdesc='Tor Browser Bundle: Anonymous browsing using firefox and tor (language-agnostic PKGBUILD)'
url='https://www.torproject.org/projects/torbrowser.html.en'
arch=('x86_64')
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

_urlbase="https://dist.torproject.org/torbrowser/${pkgver}/${pkgname}-linux64-${pkgver}"

_localetor() {

	local _fulllocale="$(locale | grep LANG | cut -d= -f2 | cut -d. -f1 | sed s/_/\-/)"
	local _shortlocale="$(locale | grep LANG | cut -d= -f2 | cut -d_ -f1)"

	if curl --output /dev/null --silent --head --fail "${_urlbase}_${_fulllocale}.tar.xz"; then
		echo -n "${_fulllocale}"
	elif curl --output /dev/null --silent --head --fail "${_urlbase}_${_shortlocale}.tar.xz"; then
		echo -n "${_shortlocale}"
	else
		echo 'en-US'
	fi

}

_language=$(_localetor)

source=("${_urlbase}_${_language}.tar.xz"
        "${pkgname}.desktop"
        "${pkgname}.install"
        "${pkgname}.png"
        "${pkgname}.sh")

md5sums=('SKIP'
         'f0cfc7681d58a77251abc49b250802d3'
         '2bf2f92d3aef0e39a3a6d6ec0701d19c'
         '494afbfa60fb4ce21840244cc3f7208c'
         '3ef08aff0e2afebb1a2a7ffbf8f65897')

noextract=("tor-browser-linux64-${pkgver}_${_language}.tar.xz")

package() {

   cd "${srcdir}"

   sed -i "s/REPL_NAME/${pkgname}/g"       ${pkgname}.sh
   sed -i "s/REPL_VERSION/${pkgver}/g"	   ${pkgname}.sh
   sed -i "s/REPL_LANGUAGE/${_language}/g" ${pkgname}.sh

   sed -i "s/REPL_NAME/${pkgname}/g"       ${pkgname}.desktop
   sed -i "s/REPL_LANGUAGE/${_language}/g" ${pkgname}.desktop
   sed -i "s/REPL_COMMENT/${pkgdesc}/g"    ${pkgname}.desktop

   install -Dm 644 ${pkgname}.desktop      ${pkgdir}/usr/share/applications/${pkgname}.desktop
   install -Dm 644 ${pkgname}.png          ${pkgdir}/usr/share/pixmaps/${pkgname}.png
   install -Dm 755 ${pkgname}.sh           ${pkgdir}/usr/bin/${pkgname}

   install -Dm 644 tor-browser-linux64-${pkgver}_${_language}.tar.xz ${pkgdir}/opt/${pkgname}/tor-browser-linux64-${pkgver}_${_language}.tar.xz

}
