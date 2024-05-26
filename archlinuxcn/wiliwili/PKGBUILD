# Maintainer: Puqns67 <me@puqns67.icu>
# Contributor: yuioto <yuiotochan@outlook.com>

# This PKGBUILD is base on the AUR repo wiliwili-git, by yuioto <yuiotochan@outlook.com>

pkgname=wiliwili
pkgver=1.4.0
pkgrel=1
pkgdesc='专为手柄控制设计的第三方跨平台B站客户端'
arch=('x86_64' 'aarch64')
url='https://github.com/xfangfang/wiliwili'
license=('GPL-3.0-or-later')
depends=('curl' 'dbus' 'gcc-libs' 'glibc' 'hicolor-icon-theme' 'libwebp' 'mpv' 'opencc' 'openssl' 'pystring' 'tinyxml2' 'zlib')
makedepends=('cmake' 'git' 'libxi' 'libxinerama' 'ninja' 'python' 'wayland-protocols')
source=("${pkgname}"::"git+${url}.git#tag=v${pkgver}")
b2sums=('59dbdbd732a122695608be7c2fd6ab2e153ecb395419ffd7e8bab79330589f922ba78fc57772eafa548d4cefa6f2757b6910d3f3dff072e1dfccc98d33121050')

prepare() {
  git -C "${srcdir}/${pkgname}" submodule update --init --recursive

  cmake \
    -B "${srcdir}/build" \
    -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_INSTALL_PREFIX='/usr' \
    -D INSTALL=ON \
    -D PLATFORM_DESKTOP=ON \
    -D USE_SYSTEM_CURL=ON \
    -D USE_SYSTEM_PYSTRING=ON \
    -D USE_SYSTEM_OPENCC=ON \
    -D USE_SYSTEM_TINYXML2=ON \
    -D USE_SYSTEM_SDL2=ON \
    -D GLFW_BUILD_WAYLAND=ON \
    -D GLFW_BUILD_X11=ON \
    -G Ninja \
    -S "${srcdir}/${pkgname}"
}

build() {
  cmake --build "${srcdir}/build"
}

package() {
  DESTDIR="${pkgdir}" cmake --install "${srcdir}/build"
}
