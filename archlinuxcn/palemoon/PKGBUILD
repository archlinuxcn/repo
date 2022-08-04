# Maintainer:  WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: artiom <a.mv at gmx dot fr>
# Contributor: ilikenwf
# Contributor: American_Jesus
pkgname=palemoon
_repo=Pale-Moon
epoch=1
pkgver=31.2.0.1
# Commit ID can be found at https://repo.palemoon.org/MoonchildProductions/Pale-Moon/releases
_commit=a70dc0b10c
pkgrel=1
pkgdesc="Open source web browser based on Firefox focusing on efficiency."
arch=('i686' 'x86_64')
url="https://www.palemoon.org/"
license=('MPL' 'GPL' 'LGPL')
depends=('gtk2' 'dbus-glib' 'desktop-file-utils' 'libxt' 'mime-types' 'alsa-lib'
         'startup-notification')
makedepends=('python2' 'autoconf2.13' 'unzip' 'zip' 'yasm'
             'libpulse' 'git')
optdepends=('libpulse: PulseAudio audio driver'
            'ffmpeg: various video and audio support')
source=(git+"https://repo.palemoon.org/MoonchildProductions/${_repo}?signed#commit=${_commit}"
        git+"https://repo.palemoon.org/MoonchildProductions/UXP"
        mozconfig.in
        glibc2.36-fix.patch)
validpgpkeys=('3DAD8CD107197488D2A2A0BD40481E7B8FCF9CEC'
              '3059E09144F56804F0FBF4E126B40624BDBFD9F3')
sha1sums=('SKIP'
          'SKIP'
          '6afaa85faa54ff26be6852009871cb60aea418d7'
          '21f9ef1825cd26928e23bd95ceac2b23ce9bfa2b')
sha256sums=('SKIP'
            'SKIP'
            '3617fc2a6dd369fff1f7fa6349abf295a0a9350bdd82f3544bbc6abd60f48009'
            'e938be99b0f08ca4778ad032c40baa73077ba2cb47f1dc95200fce7946fe04e7')

prepare() {
  sed 's#%SRCDIR%#'"${srcdir}"'#g' mozconfig.in > mozconfig
  cd ${_repo}
  git submodule init
  git config submodule.platform.url "${srcdir}/UXP"
  git submodule update
  patch -Np1 -i "${srcdir}/glibc2.36-fix.patch"
}

build() {
  cd ${_repo}

  export MOZBUILD_STATE_PATH="${srcdir}/mozbuild"
  export MOZCONFIG="${srcdir}/mozconfig"
  export CPPFLAGS="${CPPFLAGS} -O2 -Wno-format-overflow"
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
