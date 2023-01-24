# Maintainer: Brendan Szymanski <bscubed@pm.me>

_pkgname=yuzu
pkgname=$_pkgname-early-access
pkgver=3325
pkgrel=1
pkgdesc="An experimental open-source Nintendo Switch emulator/debugger (early access version)"
arch=('i686' 'x86_64')
url="https://yuzu-emu.org/"
license=('GPL2')
depends=('boost-libs' 'shared-mime-info' 'hicolor-icon-theme' 'sdl2' 'qt5-base' 'qt5-multimedia' 'qt5-webengine' 'libxkbcommon-x11' 'ffmpeg' 'fmt' 'libzip' 'opus' 'libfdk-aac' 'lz4' 'openssl' 'zstd' 'cubeb' 'dynarmic' 'enet' 'libinih' 'discord-rpc' 'cpp-httplib')
makedepends=('llvm' 'git' 'glslang' 'cmake' 'ninja' 'graphviz' 'doxygen' 'clang' 'boost' 'catch2' 'nlohmann-json' 'rapidjson' 'qt5-tools' 'desktop-file-utils' 'robin-map' 'cpp-jwt' 'xbyak' 'vulkan-headers' 'spirv-headers' 'dos2unix')
optdepends=('qt5-wayland: for Wayland support')
provides=('yuzu')
conflicts=('yuzu')
source=("https://github.com/pineappleEA/pineapple-src/archive/EA-${pkgver}.tar.gz"
"https://raw.githubusercontent.com/pineappleEA/Pineapple-Linux/master/yuzu.xml"
"https://github.com/pineappleEA/pineapple-src/releases/download/EA-${pkgver}/Windows-Yuzu-EA-${pkgver}.zip")
sha256sums=('aa941abec3b839b2d16b20ef796aaca8e675a02d4dbf73168fce5573383180a1'
            'e76ab2b3566d8135930e570ede5bed3da8f131270b60db818e453d248880bdf2'
            '0c314a3498d2a2699f449bc5eeab417e4600688e99df4f06baeb5f4d50efbaf7')

prepare() {
  cd "$srcdir/yuzu-windows-msvc-early-access"
  tar -xvf *.tar.xz
  cd $(ls *.tar.xz | sed -e 's/.tar.xz//')
  cp -R .git* $srcdir/pineapple-src-EA-${pkgver}/
  
  cd $srcdir/pineapple-src-EA-${pkgver}
  for i in $(git config --file .gitmodules --get-regexp path | awk '{ print $2 }') ; do
      rm -rf "$i"
  done

  git submodule update --init --remote externals/sirit
  git submodule update --init --remote externals/mbedtls

  find . -name "CMakeLists.txt" -exec sed -i 's/^.*-Werror$/-W/g' {} +
  #find . -name "CMakeLists.txt" -exec sed -i 's/^.*-Werror=.*)$/ )/g' {} +
  find . -name "CMakeLists.txt" -exec sed -i 's/^.*-Werror=.*$/ /g' {} +
  find . -name "CMakeLists.txt" -exec sed -i 's/-Werror/-W/g' {} +
  sed -i -e 's/1.3.238/1.3.233/g' CMakeLists.txt
  sed -i -e '/#define VK_NO_PROTOTYPES/a #define VK_ENABLE_BETA_EXTENSIONS' src/video_core/vulkan_common/vulkan_wrapper.h
  sed -i -e 's/--quiet //g' src/video_core/host_shaders/CMakeLists.txt
  sed -i -e 's#${SPIRV_HEADER_FILE} ${SOURCE_FILE}#${SPIRV_HEADER_FILE} ${SOURCE_FILE} 2>/dev/null#g' src/video_core/host_shaders/CMakeLists.txt
  sed -i -e '/Name=yuzu/ s/$/ Early Access/' dist/yuzu.desktop
  sed -i -e '/yuzu %f/a StartupWMClass=yuzu' dist/yuzu.desktop
  sed -i -e 's_^MimeType=.*_&application/x-nx-nsp;application/x-nx-xci;_' dist/yuzu.desktop
  sed -i -e 's| (%2)||' src/yuzu/aboutdialog.ui

  cp -f  $srcdir/yuzu.xml dist/yuzu.xml
}
build() {
  cd "$srcdir/pineapple-src-EA-${pkgver}"
	mkdir -p build && cd build
  cmake .. -GNinja \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_C_FLAGS="$CFLAGS -flto=thin" \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS -flto=thin" \
    -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON \
    -DTITLE_BAR_FORMAT_IDLE="yuzu Early Access $pkgver" \
    -DTITLE_BAR_FORMAT_RUNNING="yuzu Early Access $pkgver | {3}" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DYUZU_ENABLE_COMPATIBILITY_REPORTING=ON \
    -DENABLE_COMPATIBILITY_LIST_DOWNLOAD=ON \
    -DYUZU_USE_QT_WEB_ENGINE=ON \
    -DUSE_DISCORD_PRESENCE=ON \
    -DENABLE_QT_TRANSLATION=ON \
    -DYUZU_USE_BUNDLED_FFMPEG=OFF \
    -DYUZU_USE_BUNDLED_QT=OFF \
    -DYUZU_USE_EXTERNAL_SDL2=OFF \
    -DSIRIT_USE_SYSTEM_SPIRV_HEADERS=ON \
    -DYUZU_CHECK_SUBMODULES=OFF \
    -DYUZU_USE_EXTERNAL_VULKAN_HEADERS=OFF \
    -DYUZU_USE_FASTER_LD=OFF \
    -DYUZU_USE_PRECOMPILED_HEADERS=OFF \
	-DYUZU_USE_QT_MULTIMEDIA=ON \
    -DYUZU_TESTS=OFF
  ninja
}

package() {
	cd "$srcdir/pineapple-src-EA-${pkgver}/build"
	DESTDIR="$pkgdir" ninja install

    rm -rf $pkgdir/usr/lib $pkgdir/usr/include 
}
