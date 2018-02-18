# Maintainer: Ainola

pkgname=gnome-mpv
pkgver=0.14
pkgrel=1
pkgdesc="A simple GTK+ frontend for mpv."
arch=('i686' 'x86_64')
url="https://github.com/gnome-mpv/gnome-mpv"
license=('GPL3')
depends=('gtk3' 'mpv')
makedepends=('meson')
optdepends=('youtube-dl: Video integration to YouTube and other video sites.')
source=("https://github.com/gnome-mpv/gnome-mpv/releases/download/v${pkgver}/gnome-mpv-${pkgver}.tar.xz")
sha256sums=('23c9bde58da8ccf0e36c30b7d94d504aca9502288e4bb8ad5425022c4be3720e')

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
