# Maintainer: Heavysink <winstonwu91 at gmail>

_pkgname=yuzu
_link="$(curl -s $(curl -s https://raw.githubusercontent.com/pineappleEA/pineappleEA.github.io/master/index.html | head -n -2 | grep -o 'https://.*.7z' | head -n 1) | grep -o 'https://cdn-.*.7z' | head -n 1)"
pkgname=$_pkgname-early-access
pkgver=1229
pkgrel=1
pkgdesc="An experimental open-source Nintendo Switch emulator/debugger"
arch=('i686' 'x86_64')
url="https://yuzu-emu.org"
license=('GPL2')
depends=('boost-libs' 'shared-mime-info' 'hicolor-icon-theme' 'sdl2' 'qt5-base' 'qt5-multimedia' 'qt5-tools' 'qt5-webengine' 'libxkbcommon-x11' 'ffmpeg' 'fmt' 'libzip' 'opus' 'libfdk-aac' 'lz4' 'mbedtls' 'openssl' 'zstd')
makedepends=('p7zip' 'cmake' 'glslang' 'ninja' 'python2' 'graphviz' 'doxygen' 'clang' 'boost' 'catch2' 'nlohmann-json' 'rapidjson' 'desktop-file-utils' 'wget')
optdepends=('qt5-wayland: for Wayland support')
provides=('yuzu')
conflicts=('yuzu-canary-git' 'yuzu-master-git' 'yuzu-mainline-git' 'yuzu-git' 'yuzu-early-access-kiku233-git' 'yuzu-ea-bin')
source=("$_pkgname.7z::$_link")
md5sums=('1840fe92af1923e7a425d03cbf2fde8a')

pkgver () {
  curl -s https://raw.githubusercontent.com/pineappleEA/pineappleEA.github.io/master/index.html | grep -Po 'Yuzu EA \d+' | sed 's/Yuzu EA //' | head -n 1
}

prepare() {
	cd "$srcdir"
  mv yuzu-windows-msvc-early-access $_pkgname
  cd $_pkgname

  tar -xf yuzu-windows-msvc-source-*
  rm yuzu-windows-msvc-source-*.tar.xz 

  cd $(ls -d yuzu-windows-msvc-source-*)
  find -path ./dist -prune -o -type f -exec sed -i 's/\r$//' {} ';'
  find . -exec touch {} +

  wget -q https://raw.githubusercontent.com/PineappleEA/Pineapple-Linux/master/inject-git-info.patch
  wget -q https://raw.githubusercontent.com/PineappleEA/Pineapple-Linux/master/warning-to-warning.patch
  wget -q https://raw.githubusercontent.com/PineappleEA/Pineapple-Linux/master/disable-shadow-error.patch
  patch -p1 < inject-git-info.patch
  patch -p1 < warning-to-warning.patch
  patch -p1 < disable-shadow-error.patch

  sed -i 's/1.73/1.72/g' CMakeLists.txt
}

build() {
	# Trick the compiler into thinking we're building from a continuous
	# integration tool so the build number is correctly shown in the title
	cd "$srcdir/$_pkgname"
  srcd="$(ls -d yuzu-windows-msvc-source-*)"
  cd $srcd

  msvc=$(echo "${PWD##*/}"|sed 's/.*-//')
  
  mkdir -p build && cd build
  pwd
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
  cd "$srcdir/$_pkgname"
  cd $(ls -d yuzu-windows-msvc-source-*)
  cd build

  ninja test
}

package() {
  cd "$srcdir/$_pkgname"
  cd $(ls -d yuzu-windows-msvc-source-*)
  cd build

  DESTDIR="$pkgdir" ninja install
}
