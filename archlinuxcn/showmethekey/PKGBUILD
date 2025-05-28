# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=showmethekey
pkgver=1.18.2
pkgrel=1
pkgdesc="A screenkey alternative that works under Wayland via libinput."
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://showmethekey.alynx.one/"
license=("Apache")
depends=("libevdev" "udev" "libinput" "glib2" "gtk4" "libadwaita" "json-glib" "cairo" "pango" "libxkbcommon" "polkit")
makedepends=("meson" "glib2-devel")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('1632c42115adc1502249755d797fbd52565c635163b033344efeac2eedbd51b7704c267bfdafd46e38f2f93c3fb49b7115a6916b41fe7717615a2f82b0535fea')

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
