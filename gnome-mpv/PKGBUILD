# Maintainer: Ainola

pkgname=gnome-mpv
pkgver=0.13
pkgrel=2
pkgdesc="A simple GTK+ frontend for mpv."
arch=('i686' 'x86_64')
url="https://github.com/gnome-mpv/gnome-mpv"
license=('GPL3')
depends=('gtk3' 'mpv')
makedepends=('meson')
optdepends=('youtube-dl: Video integration to YouTube and other video sites.')
source=("https://github.com/gnome-mpv/gnome-mpv/releases/download/v${pkgver}/gnome-mpv-${pkgver}.tar.xz"
        "update-appdata-and-add-missing-meson-build-file.patch"
        "xdg_config_dir_permissions.patch")
sha256sums=('c5a288c7095ccbe520b3ba419856e29981f4a2d204e7cfa264ee69edab2724f1'
            'fdd2f358ceb72430fca464665ede6eb18f26be6b1830c4919ce065225f3518eb'
            '32cc698e5eb20198b12fa910a8ea9b1a0a4abc323ccaf9afb931e57c66a282dd')

prepare() {
    cd "$srcdir"
    # $XDG_CONFIG would be created with only 0600. Fixed in git upstream:
    # https://github.com/gnome-mpv/gnome-mpv/commit/0f3c23f0d752af1eff7dec7ca95143e4b4f1eb97
    patch -d "$pkgname-$pkgver" -p1 < update-appdata-and-add-missing-meson-build-file.patch
    patch -d "$pkgname-$pkgver" -p1 < xdg_config_dir_permissions.patch
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
