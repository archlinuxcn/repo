# Maintainer: Ainola

pkgname=gnome-mpv
pkgver=0.12
pkgrel=4
pkgdesc="A simple GTK+ frontend for mpv."
arch=('i686' 'x86_64')
url="https://github.com/gnome-mpv/gnome-mpv"
license=('GPL3')
depends=('gtk3' 'mpv')
makedepends=('meson')
optdepends=('youtube-dl: Video integration to YouTube and other video sites.')
source=("https://github.com/gnome-mpv/gnome-mpv/releases/download/v${pkgver}/gnome-mpv-${pkgver}.tar.xz"
        "meson-version-0.12.patch")
sha256sums=('6c121261a1ea7e8065379c5355c2b2061eb4abbff0c8121ada211d4777fa9635'
            'bc0983bfc1af703a0bc330b06dd7c0c9d3318d9e6a9fe25d913a8b98e185c2aa')

prepare() {
    cp "$srcdir/meson-version-0.12.patch" "$srcdir/$pkgname-$pkgver"
    cd "${pkgname}-${pkgver}"
    patch -p1 < meson-version-0.12.patch
}

build() {
    cd "${pkgname}-${pkgver}"
    # Remove any potential residual build files
    rm -rf _build
    meson _build --buildtype=release --prefix=/usr
    ninja -C _build
}

package() {
    cd "${pkgname}-${pkgver}"
    env DESTDIR="$pkgdir" ninja -C _build install
}
