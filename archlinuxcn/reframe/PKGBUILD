# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=reframe
pkgver=1.4.3
pkgrel=1
pkgdesc="DRM/KMS based remote desktop for Linux that supports Wayland/NVIDIA/headless/login…"
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://github.com/AlynxZhou/reframe/"
license=("Apache-2.0")
depends=("glib2" "libepoxy" "libvncserver" "libxkbcommon" "libdrm" "systemd-libs" "gcc-libs" "glibc")
makedepends=("meson")
backup=("etc/${pkgname}/example.conf")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('b7f48d567be72c33cc5cdf8b7e00559ba82d682d188cd3dc49fb73ee20a916523c8a292ed18f921dc1e6286e2c65c1253338890dc7b2830fa4ae4d0e66db3522')

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
