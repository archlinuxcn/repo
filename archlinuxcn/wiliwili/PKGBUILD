# Maintainer: Puqns67 <me@puqns67.icu>
# Contributor: yuioto <yuiotochan@outlook.com>

# This PKGBUILD is base on the AUR repo wiliwili-git, by yuioto <yuiotochan@outlook.com>

pkgname=wiliwili
pkgver=1.5.3
pkgrel=1
pkgdesc='专为手柄控制设计的第三方跨平台B站客户端'
arch=('x86_64' 'aarch64')
url='https://github.com/xfangfang/wiliwili'
license=('GPL-3.0-or-later')
depends=('curl' 'dbus' 'fmt' 'gcc-libs' 'glibc' 'hicolor-icon-theme' 'libwebp' 'mpv' 'opencc' 'openssl' 'pystring' 'qrcodegencpp-cmake' 'tinyxml2' 'zlib')
makedepends=('cmake' 'git' 'libxi' 'libxinerama' 'ninja' 'python' 'wayland-protocols')
source=("${pkgname}"::"git+${url}.git#tag=v${pkgver}")
b2sums=('c2922996bd4f4d5e1c8f92145e5e4e5e53d846cd3f0a1fb1179b90ae2bb82b2c15eba6995b23a914c5aaf1e009fef65b4d51214c4d5d8ecaec4e7b8819eb9aa8')

prepare() {
  git -C "${srcdir}/${pkgname}" rm library/{OpenCC,QR-Code-generator,pystring}
  git -C "${srcdir}/${pkgname}" submodule update --init --recursive

  # Update borealis to the latest commit to temporarily fix a CMake version compatibility issue.
  # Please delete this line after the new version is released.
  git -C "${srcdir}/${pkgname}" submodule update --remote library/borealis

  cmake \
    -B "${srcdir}/build" \
    -D CMAKE_BUILD_TYPE=RelWithDebInfo \
    -D CMAKE_INSTALL_PREFIX=/usr \
    -D INSTALL=ON \
    -D PLATFORM_DESKTOP=ON \
    -D USE_SYSTEM_CURL=ON \
    -D USE_SYSTEM_QRCODEGEN=ON \
    -D USE_SYSTEM_PYSTRING=ON \
    -D USE_SYSTEM_OPENCC=ON \
    -D USE_SYSTEM_FMT=ON \
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
