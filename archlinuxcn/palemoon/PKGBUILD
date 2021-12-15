# Maintainer:  WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: artiom <a.mv at gmx dot fr>
# Contributor: ilikenwf
# Contributor: American_Jesus
pkgname=palemoon
pkgver=29.4.3
pkgrel=1
pkgdesc="Open source web browser based on Firefox focusing on efficiency."
arch=('i686' 'x86_64')
url="https://www.palemoon.org/"
license=('MPL' 'GPL' 'LGPL')
depends=('gtk2' 'dbus-glib' 'desktop-file-utils' 'libxt' 'mime-types' 'alsa-lib'
         'startup-notification')
makedepends=('git' 'python2' 'autoconf2.13' 'unzip' 'zip' 'yasm' 'gcc10'
             'libpulse')
optdepends=('libpulse: PulseAudio audio driver'
            'ffmpeg: various video and audio support')
# as of 29.4.1, upstream have switched to unsigned source archives instead of git
source=("https://archive.palemoon.org/source/palemoon-${pkgver}.source.tar.xz"{,.sig}
        mozconfig.in)
validpgpkeys=('3DAD8CD107197488D2A2A0BD40481E7B8FCF9CEC')
sha1sums=('2478add219d4b5c301c33d80698e382c488b383c'
          'SKIP'
          '5fc8e164a8c1731ad2cce6270c9b0e9a5145194c')
sha256sums=('77e70d8b7ba061ff6157294d9bf188c304f8554c23601d704f6086dac4a3fb3f'
            'SKIP'
            'a8ded94beaef0dfa4a5d6b109c1a669967cb7d38d4fe70b3a4d7725ef4b47394')

prepare() {
  sed 's#%SRCDIR%#'"${srcdir}"'#g' mozconfig.in > mozconfig
}

build() {
  export MOZBUILD_STATE_PATH="${srcdir}/mozbuild"
  export MOZCONFIG="${srcdir}/mozconfig"
  export CPPFLAGS="${CPPFLAGS} -O2 -Wno-format-overflow"
  cd palemoon-source
  ./mach build
}

package() {
  cd pmbuild
  make package
  cd dist
  install -d "${pkgdir}"/usr/{bin,lib}
  cp -r palemoon/ "${pkgdir}/usr/lib/${pkgname}"
  ln -s "../lib/${pkgname}/palemoon" "${pkgdir}/usr/bin/palemoon"

  # icons
  install -Dm644 palemoon/browser/chrome/icons/default/default16.png \
    "${pkgdir}/usr/share/icons/hicolor/16x16/apps/${pkgname}.png"
  install -Dm644 palemoon/browser/chrome/icons/default/default32.png \
    "${pkgdir}/usr/share/icons/hicolor/32x32/apps/${pkgname}.png"
  install -Dm644 palemoon/browser/chrome/icons/default/default48.png \
    "${pkgdir}/usr/share/icons/hicolor/48x48/apps/${pkgname}.png"
  install -Dm644 palemoon/browser/icons/mozicon128.png \
    "${pkgdir}/usr/share/icons/hicolor/128x128/apps/${pkgname}.png"

  # install desktop file
  install -Dm644 "${srcdir}/palemoon-source/palemoon/branding/official/palemoon.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}
