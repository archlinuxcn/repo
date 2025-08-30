# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=reframe
pkgver=1.1.0
pkgrel=1
pkgdesc="DRM/KMS based remote desktop for Linux that supports Wayland/NVIDIA/headless/login…"
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://github.com/AlynxZhou/reframe/"
license=("Apache-2.0")
depends=("glib2" "libepoxy" "libvncserver" "libxkbcommon" "libdrm" "systemd-libs" "gcc-libs" "glibc")
makedepends=("meson")
backup=("etc/${pkgname}/example.conf")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('2ca9bfcb73710b8c0d72083219ba57283223c9301a077b7dfb6bad3b8d6320f0416e71e506db911fd4dee77a5ae96ed20ad692ec706c5a2a6b382cd27e2fee80')

prepare() {
  cd "${pkgname}-${pkgver}"
  mkdir -p build
}

build() {
  cd "${pkgname}-${pkgver}/build"
  arch-meson . ..
  meson compile
}

package() {
  cd "${pkgname}-${pkgver}/build"
  meson install --destdir "${pkgdir}"
}
