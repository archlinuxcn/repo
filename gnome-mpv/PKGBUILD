# Maintainer: Ainola

pkgname=gnome-mpv
pkgver=0.10
pkgrel=2
pkgdesc="GNOME frontend for MPV"
arch=('i686' 'x86_64')
url="https://github.com/gnome-mpv/gnome-mpv"
license=('GPL3')
depends=('gtk3' 'mpv')
makedepends=('intltool')
optdepends=('youtube-dl: Video integration to YouTube and other video sites.')
source=("https://github.com/gnome-mpv/gnome-mpv/releases/download/v${pkgver}/gnome-mpv-${pkgver}.tar.xz"
        "update_mpv_properties.patch")
sha256sums=('92d967bbbbfabdfa3ab1f19be625f684959513890b2035ca6102292392fbf183'
            '6f8cbbe298c10e50ab8c661111beed23701e73e0e31f7fe1e2c4214ae798ad8f')

prepare() {
    cd "$srcdir"
    # Fixes missing seek widget until the next version is released.
    # See https://github.com/gnome-mpv/gnome-mpv/issues/241
    patch -d "gnome-mpv-$pkgver" -p1 < update_mpv_properties.patch
}

build() {
    cd "${pkgname}-${pkgver}"
    ./configure --prefix=/usr
    make
}

package() {
    cd "${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
