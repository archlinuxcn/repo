# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Brett Cornwall <ainola@archlinux.org>
# Contributor: Adrian Perez de Castro <aperez@igalia.com>

pkgdesc='A library to create panels and other desktop components for Wayland using the Layer Shell protocol and GTK4'
pkgname=gtk4-layer-shell
pkgver=1.0.2
pkgrel=1
arch=(x86_64 aarch64)
license=(MIT)
url="https://github.com/wmww/gtk4-layer-shell"
depends=(
    "gtk4"
    "wayland"
)
makedepends=(
    "gtk-doc"
    "gobject-introspection"
    "meson"
    "ninja"
    "valabind"
    "python"
    "luajit"
)
checkdepends=(
    "lua51-lgi"
)
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('a3a827845612fa15de30734eb29c01db329c32f8e279d8bc5251facc69220b86')

build() {
    meson setup \
          --prefix=/usr \
          --wrap-mode=nofallback \
          --buildtype=plain \
          -Dtests=true \
          -Ddocs=true \
          -Dintrospection=true \
          -Dvapi=true \
          -Dexamples=true \
          "$pkgname-$pkgver" \
          build
    ninja -C build
}




# See:
# - https://github.com/wmww/gtk4-layer-shell/issues/28
# - https://github.com/mesonbuild/meson/issues/6999
# check() {
# ninja -C build test
# }

package() {
    DESTDIR="$pkgdir" ninja -C build install
    install -D -m 644 "$pkgname-$pkgver/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
