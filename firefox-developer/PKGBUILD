# Maintainer: Andrew Crerar <andrew (at) crerar (dot) io>
# Contributor: John D Jones III AKA jnbek <jnbek1972 -_AT_- g m a i l -_Dot_- com>

_name=firefox
_channel=developer
_locale="en-US"
pkgname="${_name}-${_channel}"
pkgver=58.0b10
pkgrel=1
pkgdesc='Standalone web browser from mozilla.org, developer build'
arch=('i686' 'x86_64')
license=('MPL' 'GPL' 'LGPL')
url='http://www.mozilla.org/firefox/developer'
depends=('dbus-glib' 'gtk2' 'gtk3' 'libxt' 'nss')
optdepends=('pulseaudio: audio/video playback'
            'ffmpeg: h.264 video'
            'hunspell: spell checking'
            'hyphen: hyphenation')
_srcurl="https://download-installer.cdn.mozilla.net/pub/devedition/releases"
source=("${_name}-${_channel}.desktop" "vendor.js")
source_i686=("${_srcurl}/${pkgver}/linux-i686/${_locale}/${_name}-${pkgver}.tar.bz2")
source_x86_64=("${_srcurl}/${pkgver}/linux-x86_64/${_locale}/${_name}-${pkgver}.tar.bz2")
sha512sums=('9075e0d67e4dc153dcf514f3aa2b2415ce8b39275eedbf02a3cd122949b95bf4af9dad358516145decf445d1a903d52a634f4eeeb44bb67864de02e646a76631'
            'bae5a952d9b92e7a0ccc82f2caac3578e0368ea6676f0a4bc69d3ce276ef4f70802888f882dda53f9eb8e52911fb31e09ef497188bcd630762e1c0f5293cc010')
sha512sums_i686=('1e0bb5bd83b408eff3e23795fd873f0edb43dc60addeeb6d518cd811a0c88146cabadff348d4d6a275ce85fb64f7625cf13ca4eaa005712f66bd153a0f1dc5c3')
sha512sums_x86_64=('b8b7e163d83323798d2be09b01130c39cf7a965c47c7d8a717e768605ec7af257bd8c562e5383d5e423e7277117a28fb58c23013dc2e7fe2e7f381ff6f190a7f')

package() {
  OPT_PATH="opt/${pkgname}"

  install -d "$pkgdir"/{usr/{bin,share/{applications,pixmaps}},opt}
  cp -r firefox "$pkgdir"/"${OPT_PATH}"

  ln -s /"${OPT_PATH}"/firefox "$pkgdir"/usr/bin/"${_name}-${_channel}"

  SRC_LOC="${srcdir}"/"${_name}"/browser
  DEST_LOC="${pkgdir}"/usr/share/icons/hicolor
  for i in 16 32 48; do
    install -Dm644 "${SRC_LOC}"/chrome/icons/default/default"${i}".png "${DEST_LOC}"/"${i}"x"${i}"/apps/"${pkgname}".png
  done

  install -m644 "$srcdir"/firefox/browser/icons/mozicon128.png "$pkgdir"/usr/share/pixmaps/"$pkgname"-icon.png

  install -m644 "$srcdir"/"${_name}"-"${_channel}".desktop "$pkgdir"/usr/share/applications/
  install -Dm644 "$srcdir"/vendor.js "$pkgdir"/opt/firefox-"$_channel"/browser/defaults/preferences/vendor.js

  # Use system-provided dictionaries
  rm -rf "${pkgdir}"/"${OPT_PATH}"/{dictionaries,hyphenation}
  ln -sf /usr/share/hunspell "${pkgdir}"/"${OPT_PATH}"/dictionaries
  ln -sf /usr/share/hyphen "${pkgdir}"/"${OPT_PATH}"/hyphenation
}
