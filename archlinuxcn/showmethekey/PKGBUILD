# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=showmethekey
pkgver=1.5.0
pkgrel=1
pkgdesc="A screenkey alternative that works under Wayland via libinput."
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://showmethekey.alynx.one/"
license=("Apache")
depends=("libevdev" "udev" "libinput" "glib2" "gtk3" "json-glib" "cairo" "pango" "libxkbcommon" "polkit")
makedepends=("meson")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('73b1dbb8239e9806f84270c593e41520a8937c7672eb17cef642d221bd21329277fa2887fa2832b5c087f83c6bf75d67dc8340792beb064ee36c1bdc4e099063')

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
  DESTDIR="${pkgdir}" meson install
}
