# Maintainer: Andrew Crerar <andrew (at) crerar (dot) io>
# Contributor: John D Jones III AKA jnbek <jnbek1972 -_AT_- g m a i l -_Dot_- com>

_name=firefox
_channel=developer
_locale="en-US"
pkgname="${_name}-${_channel}"
pkgver=58.0b4
pkgrel=2
pkgdesc='Standalone web browser from mozilla.org, developer build'
arch=('x86_64')
license=('MPL' 'GPL' 'LGPL')
url='http://www.mozilla.org/firefox/developer'
depends=('dbus-glib' 'gtk2' 'gtk3' 'libxt' 'nss')
optdepends=('pulseaudio: audio/video playback'
            'ffmpeg: h.264 video'
            'hunspell: spell checking'
            'hyphen: hyphenation')
_srcurl="https://download-installer.cdn.mozilla.net/pub/devedition/releases"
source=("${_name}-${_channel}.desktop" "vendor.js")
source_i686=("${_srcurl}/${pkgver}/linux-${CARCH}/${_locale}/${_name}-${pkgver}.tar.bz2")
source_x86_64=("${_srcurl}/${pkgver}/linux-${CARCH}/${_locale}/${_name}-${pkgver}.tar.bz2")
sha512sums=('9075e0d67e4dc153dcf514f3aa2b2415ce8b39275eedbf02a3cd122949b95bf4af9dad358516145decf445d1a903d52a634f4eeeb44bb67864de02e646a76631'
            'bae5a952d9b92e7a0ccc82f2caac3578e0368ea6676f0a4bc69d3ce276ef4f70802888f882dda53f9eb8e52911fb31e09ef497188bcd630762e1c0f5293cc010')
sha512sums_i686=('5d6a83e863419e46474277cc09259f4417defa87dbf175756da16c867a2d683a3699d3a09ba0c6fa646b0f3ee87bf39bfa4d9723bfb9da8eda6f49dd7c56b531')
sha512sums_x86_64=('e5456d4d7e7cbada59f0a0ebe6c074a52e370b5543065813336f64e17f99e392199e2bb3086ef2b15bfeb284ff9d4d7c8acc0eb232e02de6255cf766a9305a6a')

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
