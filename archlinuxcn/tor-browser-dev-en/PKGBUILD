# Maintainer: Yurii Kolesnykov <root@yurikoles.com>
# Ex-Maintainer: end222 <pabloorduna98 at gmail dot com>
# Ex-Maintainer: Jean Lucas <jean at 4ray dot co>
# Contributor: sekret, mail=$(echo c2VrcmV0QHBvc3Rlby5zZQo= | base64 -d)

pkgname=tor-browser-dev-en
pkgver=8.5a7
_language='en-US'
pkgrel=1
pkgdesc="Tor Browser is +1 for privacy and -1 for mass surveillance"
arch=('i686' 'x86_64')
url="https://www.torproject.org/projects/torbrowser.html.en"
license=('GPL')
depends=('gtk2' 'mozilla-common' 'libxt' 'startup-notification' 'mime-types'
         'dbus-glib' 'alsa-lib' 'desktop-file-utils' 'hicolor-icon-theme'
         'libvpx' 'icu' 'libevent' 'nss' 'hunspell' 'sqlite')
optdepends=('zenity: simple dialog boxes'
            'kdebase-kdialog: KDE dialog boxes'
            'gst-plugins-good: h.264 video'
            'gst-libav: h.264 video'
            'libpulse: PulseAudio audio driver'
            'libnotify: GNOME dialog boxes')
source_i686=("https://dist.torproject.org/torbrowser/${pkgver}/tor-browser-linux32-${pkgver}_${_language}.tar.xz"{,.asc})
source_x86_64=("https://dist.torproject.org/torbrowser/${pkgver}/tor-browser-linux64-${pkgver}_${_language}.tar.xz"{,.asc})
source+=(${pkgname}.desktop
         ${pkgname}.png
         ${pkgname}.sh)
sha256sums=('13d2e1fe85a9a08e9f66116f3c2d6f1e5d37e07d2ad8b08ae4f01890e864a722'
            '4f01e363738e36dc41ca431fbbf5a00b014dc37e2c9a3cfaf2ce182103a1d068'
            'ce19dd89a8ecd9289136f97f0122b7301bdda9bcf0208f4277817e23ea9a95d8')
sha256sums_i686=('b311ae08ce206595253033237c9d34ab43fbdfc16b915b8f361dcc45ed4f1fee'
                 'SKIP')
sha256sums_x86_64=('49c66dd4d5edaeedca8abbaf05daa444c342d84c81eb8df1157d900fe110e6b3'
                   'SKIP')
validpgpkeys=('EF6E286DDA85EA2A4BA7DE684E2C6E8793298290'
	      'A4300A6BC93C0877A4451486D1483FA6C3C07136')
noextract=("tor-browser-linux32-${pkgver}_${_language}.tar.xz"
	   "tor-browser-linux64-${pkgver}_${_language}.tar.xz")

package() {
  cd ${srcdir}

  sed -i \
    -e "s|REPL_NAME|${pkgname}|g" \
    -e "s|REPL_VERSION|${pkgver}|g" \
    -e "s|REPL_LANGUAGE|${_language}|g" \
    ${pkgname}.sh

  sed -i \
    -e "s|REPL_LANGUAGE|${_language}|g" \
    -e "s|REPL_COMMENT|${pkgdesc}|g" \
    -e "s|REPL_NAME|${pkgname}|g" \
    ${pkgname}.desktop

  install -Dm 0644 ${pkgname}.desktop \
    ${pkgdir}/usr/share/applications/${pkgname}.desktop
  install -Dm 0644 ${pkgname}.png \
    ${pkgdir}/usr/share/pixmaps/${pkgname}.png
  install -Dm 0755 ${pkgname}.sh ${pkgdir}/usr/bin/${pkgname}

  if [ "$CARCH" == "i686" ]; then
    install -Dm 0644 tor-browser-linux32-${pkgver}_${_language}.tar.xz \
      ${pkgdir}/opt/${pkgname}/tor-browser-linux32-${pkgver}_${_language}.tar.xz
  else
    install -Dm 0644 tor-browser-linux64-${pkgver}_${_language}.tar.xz \
      ${pkgdir}/opt/${pkgname}/tor-browser-linux64-${pkgver}_${_language}.tar.xz
  fi
}
