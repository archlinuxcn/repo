# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=showmethekey
pkgver=1.10.0
pkgrel=1
pkgdesc="A screenkey alternative that works under Wayland via libinput."
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://showmethekey.alynx.one/"
license=("Apache")
depends=("libevdev" "udev" "libinput" "glib2" "gtk4" "libadwaita" "json-glib" "cairo" "pango" "libxkbcommon" "polkit")
makedepends=("meson")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('65c13452294ed9458090fbbc0bc172e9d247f6d3fa819b214952fbccf930f3bc8a1753048b47b701bcc3a3ea04e6771c6c8b2a6ac8364487f9c3025037b60664')

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
  # Meson sets 755 for dirs, but polkit is 750.
  install -d -o root -g 102 -m 750 "$pkgdir/usr/share/polkit-1/rules.d"
}
