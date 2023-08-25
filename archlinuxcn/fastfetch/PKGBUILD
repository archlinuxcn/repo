# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=fastfetch
pkgver=2.0.4
pkgrel=1
pkgdesc="Like Neofetch, but much faster because written in C"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/fastfetch-cli/fastfetch"
license=('MIT')
depends=('gcc-libs')
makedepends=('chafa' 'cmake' 'dbus' 'dconf' 'ddcutil' 'imagemagick' 'libnm' 'libpulse'
             'libxcb' 'libxrandr' 'mesa' 'ocl-icd' 'opencl-headers' 'pciutils'
             'vulkan-headers' 'vulkan-icd-loader' 'wayland' 'xfconf' 'zlib')
optdepends=(
  'chafa: Image output as ascii art'
  'dbus: Bluetooth, Player & Media detection'
  'dconf: Needed for values that are only stored in DConf + Fallback for GSettings'
  'ddcutil: Brightness detection of external displays'
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
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('91d83cfa69f2eb4815c40dfe9bd931a24634f6818ecf5bfb8238a87f27ae8d3b')

build() {
  cmake -B build -S "$pkgname-$pkgver" \
    -DCMAKE_BUILD_TYPE='RelWithDebInfo' \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -DBUILD_TESTS='ON' \
    -DENABLE_SQLITE3='OFF' \
    -DENABLE_RPM='OFF' \
    -DENABLE_IMAGEMAGICK6='OFF' \
    -DENABLE_DDCUTIL='ON' \
    -Wno-dev
  cmake --build build
}

check() {
  ctest --test-dir build --output-on-failure
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
