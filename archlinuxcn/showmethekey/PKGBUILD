# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=showmethekey
pkgver=1.3.3
pkgrel=1
pkgdesc="A screenkey alternative that works under Wayland via libinput."
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://showmethekey.alynx.one/"
license=("Apache")
depends=("libevdev" "udev" "libinput" "glib2" "gtk3" "json-glib" "cairo" "pango" "libxkbcommon")
makedepends=("meson")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=("a8df31e0cfeffcf09d53889421b0135cffdc591e88e3180de73b4f4b910ca81ef79ba594dc8f01de78d8b2083659e136598007ea7df46cfe4e67e293869cb1d6")

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
