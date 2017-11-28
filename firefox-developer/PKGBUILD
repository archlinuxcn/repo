# Maintainer: Andrew Crerar <andrew (at) crerar (dot) io>
# Contributor: John D Jones III AKA jnbek <jnbek1972 -_AT_- g m a i l -_Dot_- com>

_name=firefox
_channel=developer
_locale="en-US"
pkgname="${_name}-${_channel}"
pkgver=58.0b7
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
sha512sums_i686=('5cd9ebf8aabc49bbf0fd7bacfa9f177c893fd5dee92c18305abb7de7bb82f32cc1307ae2fdf5e7f3e182946adf7f9517eef976f0d01a65e0f7db820c4d4b88eb')
sha512sums_x86_64=('a3e4ab4a5e4acb70ca04befafe9e510787c05d5fdcc1d38cb6a2dadc3fa7dd674b9b153ec55e1fce5aa691355ebfcd38386963f2fcbd9c99407e3b08ebf55eee')

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
