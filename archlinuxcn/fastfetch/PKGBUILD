# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=fastfetch
pkgver=1.11.3
pkgrel=1
pkgdesc="Like Neofetch, but much faster because written in C"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/LinusDierheimer/fastfetch"
license=('MIT')
depends=('gcc-libs')
makedepends=('chafa' 'cmake' 'dbus' 'dconf' 'imagemagick' 'libnm' 'libpulse'
             'libxcb' 'libxrandr' 'mesa' 'ocl-icd' 'opencl-headers' 'pciutils'
             'vulkan-headers' 'vulkan-icd-loader' 'wayland' 'xfconf' 'zlib')
optdepends=(
  'chafa: Image output as ascii art'
  'dbus: Bluetooth, Player & Media detection'
  'dconf: Needed for values that are only stored in DConf + Fallback for GSettings'
  'glib2: Output for values that are only stored in GSettings'
  'imagemagick: Image output using sixel or kitty graphics protocol'
  'libnm: Used for Wifi detection'
  'libpulse: Used for Sound detection'
  'mesa: Needed by the OpenGL module for gl context creation.'
  'libxrandr: Multi monitor support'
  'ocl-icd: OpenCL module'
  'pciutils: GPU output'
  'vulkan-icd-loader: Vulkan module & fallback for GPU output'
  'xfconf: Needed for XFWM theme and XFCE Terminal font'
  'zlib: Faster image output when using kitty graphics protocol'
)
backup=("etc/$pkgname/config.conf")
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('699ee59b0677121411a11119a06bdb5bc45dc04b551904c9d9d30477e2142358')

build() {
  cmake -B build -S "$pkgname-$pkgver" \
    -DCMAKE_BUILD_TYPE='RelWithDebInfo' \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -DBUILD_TESTS='ON' \
    -DENABLE_SQLITE3='OFF' \
    -DENABLE_RPM='OFF' \
    -DENABLE_IMAGEMAGICK6='OFF' \
    -DENABLE_LIBCJSON='OFF' \
    -Wno-dev
  cmake --build build
}

check() {
  ctest --test-dir build --output-on-failure
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
