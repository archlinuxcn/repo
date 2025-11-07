# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=reframe
pkgver=1.2.2
pkgrel=1
pkgdesc="DRM/KMS based remote desktop for Linux that supports Wayland/NVIDIA/headless/login…"
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://github.com/AlynxZhou/reframe/"
license=("Apache-2.0")
depends=("glib2" "libepoxy" "libvncserver" "libxkbcommon" "libdrm" "systemd-libs" "gcc-libs" "glibc")
makedepends=("meson")
backup=("etc/${pkgname}/example.conf")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('80bd0399f6b21a1484ff48a05f5f1dcdf7e40606c414914453907554adc87949202e3a9a6802333da3588998ac44fa378cbc295dc7be9559205c221ef5a104f6')

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
