# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=showmethekey
pkgver=1.2.0
pkgrel=1
pkgdesc="A screenkey alternative that works under Wayland via libinput."
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://github.com/AlynxZhou/showmethekey"
license=("Apache")
depends=("libevdev" "udev" "libinput" "glib2" "gtk3" "json-glib" "cairo" "pango" "libxkbcommon")
makedepends=("meson" "git")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=("c920f540aed77bb888c13a796e01d2ec4db15cd316f9cf79c66a64972fcfd372e4a571a89e020c5119e4e5075997631f932a642710f11d775b73141d5761e1e7")

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
