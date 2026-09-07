# Maintainer: Maxime Gauduin <alucryd@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=lib32-libvdpau
pkgver=1.5
pkgrel=5
pkgdesc='Nvidia VDPAU library'
arch=(x86_64)
url=https://www.freedesktop.org/wiki/Software/VDPAU/
license=(custom)
depends=(
  lib32-libxext
  libvdpau
)
makedepends=(
  git
  meson
  xorgproto
)
optdepends=(
  'lib32-nvidia-utils: driver for NVIDIA'
)
provides=(
  libvdpau.so
)
_tag=b40ac3c8f6cac061ddd5ed70c8305238f97a1b25
source=(git+https://gitlab.freedesktop.org/vdpau/libvdpau.git#tag=${_tag})
b2sums=('SKIP')

pkgver() {
  cd libvdpau
  git describe --tags | sed 's/[^-]*-g/r&/;s/-/+/g'
}

build() {
  arch-meson libvdpau build --cross-file lib32
  meson compile -C build
}

# According to BLFS's documentation there is only one test for this package (dlclose), and it's known to failed on some systems. Disabled until further notice
# check() {
#  meson test -C build --print-errorlogs
# }

package() {
  meson install -C build --destdir "$pkgdir"
  rm -rf "${pkgdir}"/{etc,usr/include}

  install -dm 755 "${pkgdir}"/usr/share/licenses
  ln -s libvdpau "${pkgdir}"/usr/share/licenses/lib32-libvdpau
}

# vim:set sw=2 sts=-1 et:
