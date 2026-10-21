# Maintainer: Peter Jung ptr1337 <admin@ptr1337.dev>
# Maintainer: loathingkernel <loathingkernel _a_ gmail _d_ com>

pkgname=proton-cachyos-slr
_srctag=11.0-20261015
pkgver=${_srctag//-/.}
pkgrel=1
epoch=1

_package_name="proton-cachyos-${_srctag}-slr-x86_64"
source=(
  https://github.com/CachyOS/proton-cachyos/releases/download/cachyos-${_srctag}-slr/${_package_name}.tar.xz
  compatibilitytool.vdf.template
  ntsync.conf
)

pkgdesc="A compatibility tool for Steam Play based on Wine and additional components, experimental branch with extra CachyOS flavour (Steam Linux Runtime build)"
url="https://github.com/CachyOS/proton-cachyos"
arch=(x86_64 x86_64_v3)
options=(!strip emptydirs)
license=('BSD' 'LGPL' 'zlib' 'MIT' 'MPL' 'custom')
depends=(
  bash
  coreutils
  curl
  dbus
  desktop-file-utils
  diffutils
  freetype2
  gdk-pixbuf2
  glibc
  hicolor-icon-theme
  libgcc
  libxcrypt
  libxcrypt-compat
  libxkbcommon-x11
  lsb-release
  lsof
  nss
  python
  rtkit
  ttf-font
  usbutils
  vulkan-driver
  vulkan-icd-loader
  xdg-user-dirs
  xorg-xrandr
  xz
)
depends_x86_64=(
  lib32-alsa-plugins
  lib32-fontconfig
  lib32-gcc-libs
  lib32-glibc
  lib32-libgl
  lib32-libgpg-error
  lib32-libnm
  lib32-libva
  lib32-libx11
  lib32-libxcrypt
  lib32-libxcrypt-compat
  lib32-libxinerama
  lib32-libxss
  lib32-nss
  lib32-pipewire
  lib32-systemd
  lib32-vulkan-driver
  lib32-vulkan-icd-loader
)
makedepends=(
  rsync
)
optdepends=(
  steam
  umu-launcher
)
optdepends+=(
  NTSYNC-MODULE
)
provides=('proton-cachyos' 'proton')
replaces=('proton-cachyos')
backup=(
  "usr/share/steam/compatibilitytools.d/${pkgname}/user_settings.py"
)
install=${pkgname}.install

build() {
    cd "${_package_name}"
    sed -r \
      -e "s|##INSTALL_PATH##|.|" \
      -e "s|##DISPLAY_NAME##|proton-cachyos-${_srctag} (steam linux runtime)|" \
      -e "s|##INTERNAL_TOOL_NAME##|${pkgname}|" \
      "${srcdir}/compatibilitytool.vdf.template" > compatibilitytool.vdf
}

package() {
    local _compatdir="${pkgdir}/usr/share/steam/compatibilitytools.d"
    mkdir -p "${_compatdir}/${pkgname}"
    rsync --delete -arx "${_package_name}"/* "${_compatdir}/${pkgname}"

    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    mv "${_compatdir}/${pkgname}"/{PATENTS.AV1,LICENSE{,.OFL}} \
        "${pkgdir}/usr/share/licenses/${pkgname}"

    # Load ntsync module
    install -Dm644 "$srcdir/ntsync.conf" "$pkgdir/usr/lib/modules-load.d/10-$pkgname.conf"
}

b2sums=('11f639f5b48f06e8664f3bfe8f766cc166a66f2f9f612b62b52f7a0b88e58fe08a2acf34d7615916c39077da5c328381feff67bed1193b1ddb7b4979c6340f05'
        'f0a81d83e644ca074a6bf54fc74ae12f5bd047e29d87fab528fba20e4b8d013547ad4b26e912c2b3218a75114f5c76b64aa84fdbc3054d3a1d9bf96635c6212b'
        '964a3ba277821e570aec2127f0d1ae9898da6976c360deb6b196345a50bd3c2c55cb399527507006d8fddef868069032a30b083f23987d5050f185c74dd9de35')
