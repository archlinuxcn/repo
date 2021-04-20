# Maintainer: Brendan Szymanski <bscubed@pm.me>

_pkgname=yuzu
pkgname=$_pkgname-early-access
pkgver=1617
pkgrel=1
pkgdesc="An experimental open-source Nintendo Switch emulator/debugger (mainline GIT version)"
arch=('i686' 'x86_64')
url="https://yuzu-emu.org/"
license=('GPL2')
depends=('boost-libs' 'shared-mime-info' 'hicolor-icon-theme' 'sdl2' 'qt5-base' 'qt5-multimedia' 'qt5-webengine' 'libxkbcommon-x11' 'ffmpeg' 'fmt' 'libzip' 'opus' 'libfdk-aac' 'lz4' 'mbedtls' 'openssl' 'zstd')
makedepends=('git' 'glslang' 'cmake' 'ninja' 'python2' 'graphviz' 'doxygen' 'clang' 'boost' 'catch2' 'nlohmann-json' 'rapidjson' 'qt5-tools' 'desktop-file-utils')
optdepends=('qt5-wayland: for Wayland support')
provides=('yuzu' 'yuzu-canary-git' 'yuzu-cmd' 'yuzu-mainline' 'yuzu-canary')
conflicts=('yuzu-canary-git' 'yuzu-master-git')
replaces=('yuzu-canary-git')
source=("https://github.com/pineappleEA/pineapple-src/archive/EA-${pkgver}.tar.gz")
md5sums=('d19e28c6102598411221aa5aed3b22f6')

prepare() {
  cd "$srcdir/pineapple-src-EA-${pkgver}"
  for i in patches/*.patch; do
    patch -p1 < $i
  done
  find . -name "CMakeLists.txt" -exec sed -i 's/^.*-Werror$/-W/g' {} +
  find . -name "CMakeLists.txt" -exec sed -i 's/^.*-Werror=.*)$/ )/g' {} +
  find . -name "CMakeLists.txt" -exec sed -i 's/^.*-Werror=.*$/ /g' {} +
  find . -name "CMakeLists.txt" -exec sed -i 's/-Werror/-W/g' {} +
}
build() {
  cd "$srcdir/pineapple-src-EA-${pkgver}"
	mkdir -p build && cd build
  cmake .. -GNinja \
    -DTITLE_BAR_FORMAT_IDLE="yuzu Early Access $pkgver" \
    -DTITLE_BAR_FORMAT_RUNNING="yuzu Early Access $pkgver | {3}" \
    -DGIT_BRANCH="HEAD" \
    -DGIT_DESC="$msvc" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DYUZU_ENABLE_COMPATIBILITY_REPORTING=ON \
    -DYUZU_USE_BUNDLED_UNICORN=ON \
    -DENABLE_COMPATIBILITY_LIST_DOWNLOAD=ON \
    -DYUZU_USE_QT_WEB_ENGINE=ON \
    -DUSE_DISCORD_PRESENCE=ON

  ninja
}

check() {
	cd "$srcdir/pineapple-src-EA-${pkgver}/build"
	ninja test
}

package() {
	cd "$srcdir/pineapple-src-EA-${pkgver}/build"
	DESTDIR="$pkgdir" ninja install
}
