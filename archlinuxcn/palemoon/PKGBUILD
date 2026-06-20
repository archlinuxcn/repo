# Maintainer:  WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: artiom <a.mv at gmx dot fr>
# Contributor: ilikenwf
# Contributor: American_Jesus
# Contributor: Mufflone
# Contributor: switchnode
pkgname=palemoon
_repo=Pale-Moon
epoch=1
pkgver=34.3.0.1
# Commit ID can be found at https://repo.palemoon.org/MoonchildProductions/Pale-Moon/tags
_commit=973993c59c
pkgrel=1
pkgdesc="Open source web browser based on Firefox focusing on efficiency."
arch=('i686' 'x86_64')
url="https://www.palemoon.org/"
license=('MPL-2.0')
depends=(
  'alsa-lib'
  'at-spi2-core'
  'bash'
  'cairo'
  'dbus'
  'fontconfig'
  'freetype2'
  'gdk-pixbuf2'
  'glib2'
  'glibc'
  'gtk2'
  'hicolor-icon-theme'
  'libgcc'
  'libstdc++'
  'libx11'
  'libxcb'
  'libxext'
  'libxrender'
  'libxt'
  'pango'
)
makedepends=(
  'git'
  'libpulse'
  'nasm'
  'python'
  'tar'
  'unzip'
  'yasm'
  'zip'
)
optdepends=('libpulse: PulseAudio audio driver'
            'ffmpeg: various video and audio support')
source=(git+"https://repo.palemoon.org/MoonchildProductions/${_repo}?signed#commit=${_commit}"
        git+"https://repo.palemoon.org/MoonchildProductions/UXP"
        mozconfig.in)
validpgpkeys=('3DAD8CD107197488D2A2A0BD40481E7B8FCF9CEC')
sha1sums=('aab88a7a027ddde10b3c9a67967cbb799ad4c6f5'
          'SKIP'
          'a45ac7de3b664dcadb0917a975ee0b859385b719')
sha256sums=('94474c1f64830270782e37694ca694be5f180a2bf5bc0402ec47ac152152aa43'
            'SKIP'
            'd74ba2d07f5ddb9a8268c64745995a310f5aa2033ca3c8634a22e0cbcf0fa3c2')

prepare() {
  sed 's#%SRCDIR%#'"${srcdir}"'#g' mozconfig.in > mozconfig
  cd ${_repo}
  git submodule init
  git config submodule.platform.url "${srcdir}/UXP"
  git -c protocol.file.allow=always submodule update
}

build() {
  cd ${_repo}

  # Remove option not supported by ld.gold to prevent configure failure
  export LDFLAGS="${LDFLAGS/-Wl,-z,pack-relative-relocs/}"
  export MOZBUILD_STATE_PATH="${srcdir}/mozbuild"
  export MOZCONFIG="${srcdir}/mozconfig"
  export CPPFLAGS="${CPPFLAGS} -O2"

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
  install -Dm644 "${srcdir}/${_repo}/palemoon/branding/official/palemoon.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}
