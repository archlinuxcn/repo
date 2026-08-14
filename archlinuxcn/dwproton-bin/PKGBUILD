# Maintainer: Shira Nguyen <sn3446409@gmail.com>

_pkgname=dwproton
pkgname=${_pkgname}-bin
_srcver=11.0-11
pkgver=${_srcver//-/_}
pkgrel=2
epoch=1
pkgdesc="Proton builds with the latest Dawn Winery fixes for gacha games, based on Proton-CachyOS."
arch=('x86_64')
url="https://dawn.wine/dawn-winery/dwproton"
license=('BSD-2-Clause' 'LGPL-2.1-only' 'Zlib' 'MIT' 'MPL-2.0' 'custom')
options=(!strip emptydirs)
provides=('proton' 'dwproton')
_srcdir="${_pkgname}-${_srcver}-${CARCH}"
source=("${url}/releases/download/${_pkgname}-${_srcver}/${_srcdir}.tar.xz")
sha512sums=('94e502e935e3d743e33647f580489ebd3b54b0789196d87b066f06456455a8dd7966f149dfcb73e64e9d345a6f2c20ac4b24a9095cad643577b34ae45dcefff5')
depends=(
  bash
  coreutils
  curl
  dbus
  desktop-file-utils
  diffutils
  freetype2
  gcc-libs
  gdk-pixbuf2
  glibc
  hicolor-icon-theme
  libxcrypt
  libxcrypt-compat
  libxkbcommon-x11
  lsb-release
  lsof
  nss
  python
  ttf-font
  usbutils
  vulkan-driver
  vulkan-icd-loader
  xdg-user-dirs
  xorg-xrandr
  xz
  zenity
  mpg123
  libpulse
  libpcap
  openxr
  libvdpau
  nettle3
  libvorbis
  opus
  python-filelock
  libogg
  jsoncpp
  ffmpeg4.4
  lapack
)
depends_x86_64=(
  lib32-alsa-plugins
  lib32-fontconfig
  lib32-gcc-libs
  lib32-glibc
  lib32-libgl
  lib32-libgpg-error
  lib32-libnm
  lib32-pango
  lib32-libva
  lib32-libx11
  lib32-libxcrypt
  lib32-libxcrypt-compat
  lib32-gst-plugins-base-libs
  lib32-lcms2
  lib32-libxinerama
  lib32-libxss
  lib32-nss
  lib32-libxkbcommon
  lib32-pipewire
  lib32-systemd
  lib32-vulkan-driver
  lib32-vulkan-icd-loader
  lib32-libpcap
  lib32-libgudev
  lib32-libusb
  lib32-libpulse
  lib32-libsndfile
  lib32-libvdpau
  lib32-mpg123
  lib32-orc
  lib32-opus
  lib32-cairo
  lib32-libvorbis
  lib32-libwebp
  lib32-libogg
)
optdepends=(
  steam
  lutris
  heroic-games-launcher
  umu-launcher
)
install=${pkgname}.install

prepare() {
    sed -i -E 's/"dwproton-[^"]*"/"dwproton"/g' \
      "${srcdir}/${_srcdir}/compatibilitytool.vdf"
}

package() {
    # License
    install -d "${pkgdir}/usr/share/licenses/${pkgname}"
    mv "${srcdir}/${_srcdir}"/{PATENTS.AV1,LICENSE{,.OFL}} \
       "${pkgdir}/usr/share/licenses/${pkgname}"

    # Proton executable
    install -d "${pkgdir}/usr/share/steam/compatibilitytools.d/${_pkgname}"
    mv "${srcdir}/${_srcdir}"/* \
       "${pkgdir}/usr/share/steam/compatibilitytools.d/${_pkgname}"
}

