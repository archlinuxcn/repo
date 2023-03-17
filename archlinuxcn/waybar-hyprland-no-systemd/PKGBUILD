# Contributor: Bruno Ancona <bruno at powerball253 dot com>
# Maintainer: Eragon <eragon at eragon dot re>

pkgname=waybar-hyprland-no-systemd
_pkgname=Waybar
pkgver=0.9.17
pkgrel=0
pkgdesc='Highly customizable Wayland bar for Sway and Wlroots based compositors, with workspaces support for Hyprland, without systemd dependency'
arch=('any')
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
    'wireplumber')
makedepends=(
    'cmake'
    'catch2'
    'meson'
    'scdoc'
    'wayland-protocols')
backup=(
    etc/xdg/waybar/config
    etc/xdg/waybar/style.css)
optdepends=('otf-font-awesome: Icons in the default configuration')
source=("https://github.com/Alexays/Waybar/archive/$pkgver.tar.gz"
        meson-build.patch
        meson_options.patch)
sha256sums=('da6f448be343a593ee092486fb4744502aa1e6ad85f4eccc3670d0b84a2a4266'
            '2a403854363b08024f446d17c6056a9a6ae61364f4c14c8f9b4c972d07dab78b'
            '146d1d8b0bc8216b7d29f93f934c4a3716ec091e1dd140b68e79aa487d28afa1')

prepare() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    patch -p1 < ../meson-build.patch
    patch -p1 < ../meson_options.patch
}

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    sed -i 's/zext_workspace_handle_v1_activate(workspace_handle_);/const std::string command = "hyprctl dispatch workspace " + name_;\n\tsystem(command.c_str());/g' src/modules/wlr/workspace_manager.cpp # use hyprctl to switch workspaces

    meson --prefix=/usr \
          --buildtype=plain \
          --auto-features=enabled \
          --wrap-mode=nodownload \
          -Dtests=disabled \
          build
    meson configure -Dexperimental=true build
    ninja -C build
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    DESTDIR="$pkgdir" ninja -C build install
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
