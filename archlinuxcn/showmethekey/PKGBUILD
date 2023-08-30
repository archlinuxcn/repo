# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=showmethekey
pkgver=1.11.1
pkgrel=1
pkgdesc="A screenkey alternative that works under Wayland via libinput."
arch=("x86_64" "i686" "aarch64" "armv7h" "armv6h")
url="https://showmethekey.alynx.one/"
license=("Apache")
depends=("libevdev" "udev" "libinput" "glib2" "gtk4" "libadwaita" "json-glib" "cairo" "pango" "libxkbcommon" "polkit")
makedepends=("meson")
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('afd9759a9a01a4487a9a0915a645020e89088afd1a2d910fcd19cb0e7142c4005574eea5f3265e6321844275c026a3ebb4c6d9a596229496c0e3c636fdd5139d')

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
