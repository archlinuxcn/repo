# Maintainer: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=('mangohud' 'mangoapp' 'mangohud-common')
pkgbase=mangohud
pkgver=0.6.8
pkgrel=5
_imgui_ver=1.81
pkgdesc="A Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more."
arch=('x86_64')
url="https://github.com/flightlessmango/MangoHud"
license=('MIT')
makedepends=('appstream' 'dbus' 'git' 'glew' 'glfw-x11' 'glslang' 'libglvnd' 'libxnvctrl' 'meson'
             'nlohmann-json' 'python-mako' 'spdlog' 'vulkan-headers')
_commit=efdcc6d2f54e37a3a32475453407f1eb33d1bef2
source=("git+https://github.com/flightlessmango/MangoHud.git#commit=${_commit}"
        'git+https://github.com/flightlessmango/minhook.git'
        "https://github.com/ocornut/imgui/archive/refs/tags/v${_imgui_ver}/imgui-${_imgui_ver}.tar.gz"
        "https://wrapdb.mesonbuild.com/v2/imgui_${_imgui_ver}-1/get_patch#/imgui-${_imgui_ver}-1-wrap.zip")
sha256sums=('SKIP'
            'SKIP'
            'f7c619e03a06c0f25e8f47262dbc32d61fd033d2c91796812bf0f8c94fca78fb'
            '6d00b442690b6a5c5d8f898311daafbce16d370cf64f53294c3b8c5c661e435f')

pkgver() {
  cd "$srcdir/MangoHud"
  git describe --tags | sed 's/^v//;s/-/+/g'
}

prepare() {
  cd "$srcdir/MangoHud"
  git submodule init modules/minhook
  git config submodule.minhook.url "$srcdir/minhook"
  git -c protocol.file.allow=always submodule update

  ln -sfv "$srcdir/imgui-${_imgui_ver}" subprojects
}

build() {
local meson_options=(
  -Duse_system_spdlog=enabled
  -Duse_system_vulkan=enabled
  -Dmangoapp=true
  -Dmangohudctl=true
  -Dmangoapp_layer=true
)

  arch-meson MangoHud build "${meson_options[@]}"
  meson compile -C build
}

check() {
  cd "$srcdir/MangoHud"
  appstreamcli validate --pedantic "data/io.github.flightlessmango.$pkgbase.metainfo.xml"
}

package_mangohud() {
  depends=('mangohud-common' 'dbus' 'fmt' 'gcc-libs' 'libx11' 'spdlog' 'vulkan-icd-loader')
  optdepends=('libxnvctrl: NVIDIA GPU stats by XNVCtrl'
              'mangoapp')
  replaces=("$pkgname-x11" "$pkgname-wayland")

  meson install --tags runtime,scripts -C build --destdir "$pkgdir"
}

package_mangoapp() {
  pkgdesc="A transparent background OpenGL application with a built-in MangoHud designed to be run inside a gamescope instance"
  depends=('glew' 'glfw-x11' 'mangohud')
  optdepends=('gamescope')

  meson install --tags "$pkgname" -C build --destdir "$pkgdir"
}

package_mangohud-common() {
  pkgdesc="Common files for MangoHud"
  replaces=("$pkgname-x11" "$pkgname-wayland")

  meson install --tags doc,man -C build --destdir "$pkgdir"

  cd "$srcdir/MangoHud"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgbase/"
}
