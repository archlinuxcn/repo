# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=reframe
pkgver=1.3.0
pkgrel=1
pkgdesc="DRM/KMS based remote desktop for Linux that supports Wayland/NVIDIA/headless/login…"
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://github.com/AlynxZhou/reframe/"
license=("Apache-2.0")
depends=("glib2" "libepoxy" "libvncserver" "libxkbcommon" "libdrm" "systemd-libs" "gcc-libs" "glibc")
makedepends=("meson")
backup=("etc/${pkgname}/example.conf")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('f983f2af66554646f2f9a876a98d8eb2c1aeb1c225404e9b809bef45dd085fa06ab042f3b1ad246a85b83e8a8d72a843b242e2ef34437e44cf661bec274ff4e8')

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
