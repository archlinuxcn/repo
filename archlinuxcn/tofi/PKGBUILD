# Maintainer: Philip Jones <philj56@gmail.com>
pkgname=tofi
pkgver=0.9.1
pkgrel=2
pkgdesc="Tiny rofi / dmenu replacement for wlroots-based Wayland compositors."
arch=("x86_64")
url="https://github.com/philj56/tofi"
license=("MIT")
groups=()
depends=("freetype2" "harfbuzz" "cairo" "pango" "wayland" "libxkbcommon" "glib2")
makedepends=("meson" "scdoc" "wayland-protocols")
provides=("${pkgname}")
conflicts=("${pkgname}")
replaces=()
backup=()
options=()
install=
source=("https://github.com/philj56/${pkgname}/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz")
noextract=()
sha512sums=(a14ab5ecf2c6e1ecb0ec3366c436140aa422995d464de513e81e454df0f303fc9661b534a3f40df4f14897629cd0cc299bb449482b676fbf254002731ac02231)

prepare() {
	rm -rf build
        CFLAGS=$CFLAGS LDFLAGS=$LDFLAGS meson setup "${pkgname}-${pkgver}" build --prefix /usr -Dbuildtype=release
}

build() {
        ninja -C build
}

check() {
	ninja -C build test
}

package() {
        DESTDIR="$pkgdir" ninja -C build install
}
