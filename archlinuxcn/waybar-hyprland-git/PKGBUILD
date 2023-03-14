# Maintainer: Bruno Ancona <bruno at powerball253 dot com>

pkgname=waybar-hyprland-git
pkgver=0.9.17.r66.gea38eec2
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
)
backup=(
    etc/xdg/waybar/config
    etc/xdg/waybar/style.css
)
optdepends=(
    'otf-font-awesome: Icons in the default configuration'
)
source=("${pkgname}::git+https://github.com/Alexays/Waybar")
sha1sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname}"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "${srcdir}/${pkgname}"
    rm -rf "${srcdir}/build"

    sed -i 's/zext_workspace_handle_v1_activate(workspace_handle_);/const std::string command = "hyprctl dispatch workspace " + name_;\n\tsystem(command.c_str());/g' src/modules/wlr/workspace_manager.cpp # use hyprctl to switch workspaces

    meson --prefix=/usr \
          --buildtype=plain \
          --auto-features=enabled \
          --wrap-mode=nodownload \
          "${srcdir}/build"
    meson configure -Dexperimental=true "${srcdir}/build" # enable experimental features
    ninja -C "${srcdir}/build"
}

package() {
    DESTDIR="$pkgdir" ninja -C "${srcdir}/build" install
    install -Dm644 "${srcdir}/${pkgname}/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname/"
}
