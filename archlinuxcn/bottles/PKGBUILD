# Maintaner: Francesco Masala <mail@francescomasala.me>
# Contributor: lotation <xlapsiu@gmail.com>

pkgname=bottles
_pkgname=Bottles
pkgver=51.17
pkgrel=3
epoch=2
pkgdesc='Easily manage wine and proton prefix'
arch=(any)
url="https://github.com/bottlesdevs/Bottles"
license=(GPL-3.0-only)
depends=(
  cabextract
  dconf
  gtk4
  gtksourceview5
  hicolor-icon-theme
  icoextract
  imagemagick
  libadwaita
  libportal-gtk4
  p7zip
  patool
  python
  python-chardet
  python-fvs
  python-gobject
  python-markdown
  python-orjson
  python-pathvalidate
  python-pycurl
  python-requests
  python-steamgriddb
  python-yaml
  webkit2gtk
  xorg-xdpyinfo
  vkbasalt-cli
)
optdepends=(
  gamemode
  gvfs 
  lib32-gamemode
  lib32-gnutls
  lib32-vkd3d 
  lib32-vulkan-icd-loader 
  vkd3d
  vulkan-icd-loader
  wine
)
makedepends=(
  blueprint-compiler
  meson
  ninja
)
source=(
  "${_pkgname}-${pkgver}.tar.gz::https://github.com/bottlesdevs/Bottles/archive/refs/tags/${pkgver}.tar.gz"
  allow-non-flatpak.patch
  disable-flatpak-check.patch
)
sha256sums=(
  f0fdb62e2093206e46f9ceda94726927fc28436e253c89be3e0c248c975baf91
  51e33e3227db9d42162df32bd6f77f318b34aac50192ded9c2399188efc636af
  013a88ff60d66a011f3c2c0e4b8d01a25d24b2cca52695737f34d4fd09ac3010
)

prepare() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  
  # Disable check for the .flatpak-info file
  patch -Np1 -i ../allow-non-flatpak.patch

  # Fix warning about needed sandbox environment
  patch -Np1 -i ../disable-flatpak-check.patch
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  meson setup --prefix='/usr' build
  ninja -C build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  DESTDIR="${pkgdir}" ninja -C build install
}

# vim: set ft=sh ts=2 sw=2 et:
