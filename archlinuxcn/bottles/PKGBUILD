# Maintaner: Francesco Masala <mail@francescomasala.me>
# Contributor: lotation <xlapsiu@gmail.com>

pkgname=bottles
_pkgname=Bottles
pkgver=51.21
pkgrel=1
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
  disable-flatpak-check.patch
)
sha256sums=(
  3a5653464839d5dbe36d44eabb823d422421897325f3c7944cddc9475575869d
  eec371407a6a8cc196330e68535e15a1332c31e38f47eb1891be1cf754d76802
)

prepare() {
  patch --forward --directory="${srcdir}/${_pkgname}-${pkgver}" --strip=1 --input="${srcdir}/disable-flatpak-check.patch"
  # cd "${srcdir}/${_pkgname}-${pkgver}"
  
  # Fix warning about flatpak and sandbox environment
  # patch -Np0 -i ../disable-flatpak-check.patch
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
