# Maintainer: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Co-Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=('mangohud' 'mangoapp' 'mangohud-common')
pkgbase=mangohud
pkgver=0.6.9.1
pkgrel=1
_imgui_ver=1.81
_vulkan_ver=1.2.158
pkgdesc="A Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more."
arch=('x86_64')
url="https://github.com/flightlessmango/MangoHud"
license=('MIT')
makedepends=('appstream' 'cmocka' 'dbus' 'git' 'glew' 'glfw-x11' 'glslang' 'libglvnd'
             'libxnvctrl' 'meson' 'nlohmann-json' 'python-mako' 'spdlog')
_commit=7f945627f57ecc56afea342c2dc0544d0d43728e  # tags/v0.6.9-1^0
source=("git+https://github.com/flightlessmango/MangoHud.git#commit=${_commit}"
        'git+https://github.com/flightlessmango/minhook.git'
        "https://github.com/ocornut/imgui/archive/refs/tags/v${_imgui_ver}/imgui-${_imgui_ver}.tar.gz"
        "https://wrapdb.mesonbuild.com/v2/imgui_${_imgui_ver}-1/get_patch#/imgui-${_imgui_ver}-1-wrap.zip"
        "Vulkan-Headers-${_vulkan_ver}.tar.gz::https://github.com/KhronosGroup/Vulkan-Headers/archive/v${_vulkan_ver}.tar.gz"
        "https://wrapdb.mesonbuild.com/v2/vulkan-headers_${_vulkan_ver}-2/get_patch#/vulkan-headers-${_vulkan_ver}-2-wrap.zip")
sha256sums=('SKIP'
            'SKIP'
            'f7c619e03a06c0f25e8f47262dbc32d61fd033d2c91796812bf0f8c94fca78fb'
            '6d00b442690b6a5c5d8f898311daafbce16d370cf64f53294c3b8c5c661e435f'
            '53361271cfe274df8782e1e47bdc9e61b7af432ba30acbfe31723f9df2c257f3'
            '860358cf5e73f458cd1e88f8c38116d123ab421d5ce2e4129ec38eaedd820e17')

pkgver() {
  cd "$srcdir/MangoHud"
#  git describe --tags | sed 's/^v//;s/-/+/g'
  git describe --tags | sed 's/^v//;s/-/./g'
}

prepare() {
  cd "$srcdir/MangoHud"
  git submodule init modules/minhook
  git config submodule.subprojects/minhook.url "$srcdir/minhook"
  git -c protocol.file.allow=always submodule update

  ln -sfv \
    "$srcdir/imgui-${_imgui_ver}" \
    "$srcdir/Vulkan-Headers-${_vulkan_ver}" \
      subprojects/

  # Use system cmocka instead of subproject
  sed -i "s/  cmocka = subproject('cmocka')//g" meson.build
  sed -i "s/cmocka_dep = cmocka.get_variable('cmocka_dep')/cmocka_dep = dependency('cmocka')/g" meson.build
}

build() {
local meson_options=(
  -Duse_system_spdlog=enabled
  -Dmangoapp=true
  -Dmangohudctl=true
  -Dmangoapp_layer=true
)

  arch-meson MangoHud build "${meson_options[@]}"
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs || :
}

package_mangohud() {
  depends=('mangohud-common' 'dbus' 'fmt' 'gcc-libs' 'spdlog' 'vulkan-icd-loader')
  optdepends=('libxnvctrl: NVIDIA GPU stats by XNVCtrl'
              'mangoapp')
  provides=('libMangoHud.so' 'libMangoHud_dlsym.so')
  replaces=("$pkgname-x11" "$pkgname-wayland")

  meson install --tags runtime,scripts -C build --destdir "$pkgdir"
}

package_mangoapp() {
  pkgdesc="A transparent background OpenGL application with a built-in MangoHud designed to be run inside a gamescope instance"
  depends=('glfw-x11' 'libglvnd' 'libx11' 'mangohud')
  optdepends=('gamescope')
  provides=('libMangoApp.so')

  meson install --tags "$pkgname" -C build --destdir "$pkgdir"
}

package_mangohud-common() {
  pkgdesc="Common files for MangoHud"
  replaces=("$pkgname-x11" "$pkgname-wayland")

  meson install --tags doc,man -C build --destdir "$pkgdir"

  cd "$srcdir/MangoHud"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgbase/"
}
