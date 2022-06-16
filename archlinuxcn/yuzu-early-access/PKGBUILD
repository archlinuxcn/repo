# Maintainer: Brendan Szymanski <bscubed@pm.me>

_pkgname=yuzu
pkgname=$_pkgname-early-access
pkgver=2790
pkgrel=1
pkgdesc="An experimental open-source Nintendo Switch emulator/debugger (early access version)"
arch=('i686' 'x86_64')
url="https://yuzu-emu.org/"
license=('GPL2')
depends=('boost-libs' 'shared-mime-info' 'hicolor-icon-theme' 'sdl2' 'qt5-base' 'qt5-multimedia' 'qt5-webengine' 'libxkbcommon-x11' 'ffmpeg' 'fmt' 'libzip' 'opus' 'libfdk-aac' 'lz4' 'mbedtls' 'openssl' 'zstd')
makedepends=('git' 'glslang' 'cmake' 'ninja' 'graphviz' 'doxygen' 'clang' 'boost' 'catch2' 'nlohmann-json' 'rapidjson' 'qt5-tools' 'desktop-file-utils' 'robin-map')
optdepends=('qt5-wayland: for Wayland support')
provides=('yuzu')
conflicts=('yuzu')
source=("https://github.com/pineappleEA/pineapple-src/archive/EA-${pkgver}.tar.gz"
    "inject-git-info.patch")
md5sums=('c0fabbfaa8fcba996274910c70dfeafc'
         '3f0a9f3d79cbe4759e9ef550dbad0baa')

prepare() {
  cd "$srcdir/pineapple-src-EA-${pkgver}"
  cp $srcdir/inject-git-info.patch patches/

  for i in patches/*.patch; do
    patch -p1 --verbose --ignore-whitespace < $i
  done
  find . -name "CMakeLists.txt" -exec sed -i 's/^.*-Werror$/-W/g' {} +
  #find . -name "CMakeLists.txt" -exec sed -i 's/^.*-Werror=.*)$/ )/g' {} +
  find . -name "CMakeLists.txt" -exec sed -i 's/^.*-Werror=.*$/ /g' {} +
  find . -name "CMakeLists.txt" -exec sed -i 's/-Werror/-W/g' {} +
  sed -i 's/static constexpr/const/g' src/shader_recompiler/frontend/maxwell/structured_control_flow.cpp
  sed -i 's/add_subdirectory(mcl)/add_subdirectory(mcl EXCLUDE_FROM_ALL)/g' externals/dynarmic/externals/CMakeLists.txt
  sed -i -e 's/--quiet //g' src/video_core/host_shaders/CMakeLists.txt
  sed -i -e 's#${SPIRV_HEADER_FILE} ${SOURCE_FILE}#${SPIRV_HEADER_FILE} ${SOURCE_FILE} 2>/dev/null#g' src/video_core/host_shaders/CMakeLists.txt
  sed -i -e '/Name=yuzu/ s/$/ Early Access/' dist/yuzu.desktop
  sed -i -e '/yuzu %f/a StartupWMClass=yuzu' dist/yuzu.desktop
  sed -i -e 's_^MimeType=.*_&application/x-nx-nsp;application/x-nx-xci;_' dist/yuzu.desktop
}
build() {
  cd "$srcdir/pineapple-src-EA-${pkgver}"
	mkdir -p build && cd build
  cmake .. -GNinja \
    -DTITLE_BAR_FORMAT_IDLE="yuzu Early Access $pkgver" \
    -DTITLE_BAR_FORMAT_RUNNING="yuzu Early Access $pkgver | {3}" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DYUZU_ENABLE_COMPATIBILITY_REPORTING=ON \
    -DENABLE_COMPATIBILITY_LIST_DOWNLOAD=ON \
    -DYUZU_USE_QT_WEB_ENGINE=ON \
    -DUSE_DISCORD_PRESENCE=ON \
    -DENABLE_QT_TRANSLATION=ON \
    -DYUZU_USE_EXTERNAL_SDL2=OFF \
    -DYUZU_USE_BUNDLED_OPUS=OFF \
    -DDYNARMIC_NO_BUNDLED_FMT=ON \
    -DDYNARMIC_NO_BUNDLED_ROBIN_MAP=ON \
    -DYUZU_USE_BUNDLED_FFMPEG=OFF

  ninja
}

package() {
	cd "$srcdir/pineapple-src-EA-${pkgver}/build"
	DESTDIR="$pkgdir" ninja install
}
