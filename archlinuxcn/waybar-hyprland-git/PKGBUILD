# Maintainer: Bruno Ancona <bruno at powerball253 dot com>

pkgname=waybar-hyprland-git
pkgver=0.9.17.r134.g8aafe817
pkgrel=1
pkgdesc='Highly customizable Wayland bar for Sway and Wlroots based compositors, with workspaces support for Hyprland (git version)'
arch=('x86_64' 'aarch64')
url='https://github.com/Alexays/Waybar/'
license=('MIT')
provides=('waybar')
conflicts=('waybar')
depends=(
    'gtkmm3'
    'libjsoncpp.so'
    'libsigc++'
    'fmt'
    'jack' 'libjack.so'
    'wayland'
    'libdate-tz.so'
    'libspdlog.so'
    'gtk-layer-shell'
    'libupower-glib.so'
    'upower'
    'libevdev'
    'libinput'
    'libpulse'
    'libnl'
    'libappindicator-gtk3'
    'libdbusmenu-gtk3'
    'libmpdclient'
    'libsndio.so'
    'libxkbcommon'
    'wireplumber'
    'playerctl'
)
makedepends=(
    'git'
    'cmake'
    'catch2'
    'meson'
    'scdoc'
    'wayland-protocols'
    'curl'
)
backup=(
    etc/xdg/waybar/config
    etc/xdg/waybar/style.css
)
optdepends=(
    'otf-font-awesome: Icons in the default configuration'
    'cava: Cava plugin support'
)
source=("${pkgname}::git+https://github.com/Alexays/Waybar"
        hyprctl.patch
        cava.patch)
sha256sums=('SKIP'
          'b4819ed456b27c355f24c460bcf3ff2fec6dade8c210263b64361c6744a9147c'
          '51fbf6cf8767cebf66e26b8f393e696859ef02c70ad7c88fe55025534e2515ab')

pkgver() {
    cd "${srcdir}/${pkgname}"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
    cd "${srcdir}/${pkgname}"

    git apply ../hyprctl.patch # use hyprctl to switch workspaces
    git apply ../cava.patch # fix cava dependency not found

    mkdir "subprojects/packagecache"
    filename=$(grep source_filename subprojects/cava.wrap | rev | cut -d' ' -f1 | rev)
    url=$(grep source_url subprojects/cava.wrap | rev | cut -d' ' -f1 | rev)
    curl -Lo "subprojects/packagecache/${filename}" "$url" # pre=download cava dependency
}

build() {
    cd "${srcdir}/${pkgname}"
    rm -rf "${srcdir}/build"

    meson --prefix=/usr \
          --buildtype=plain \
          --auto-features=enabled \
          --wrap-mode=nodownload \
          -Dexperimental=true \
          "${srcdir}/build"
    ninja -C "${srcdir}/build"
}

package() {
    DESTDIR="$pkgdir" ninja -C "${srcdir}/build" install
    install -Dm644 "${srcdir}/${pkgname}/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname/"
}
