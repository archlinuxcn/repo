# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=showmethekey
pkgver=1.3.0
pkgrel=1
pkgdesc="A screenkey alternative that works under Wayland via libinput."
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://showmethekey.alynx.one/"
license=("Apache")
depends=("libevdev" "udev" "libinput" "glib2" "gtk3" "json-glib" "cairo" "pango" "libxkbcommon")
makedepends=("meson" "git")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=("df1cd86296c0058d48a69b2925b37f95e57dd676d6d8c1741b1f65cf035df714921298aff4efe20266184dce6c621fba70678cc6195c13d81a1f62355254dbbc")

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
