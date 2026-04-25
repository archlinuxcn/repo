# Maintainer: Puqns67 <me@puqns67.icu>
# Contributor: yuioto <yuiotochan@outlook.com>

# This PKGBUILD is base on the AUR repo wiliwili-git, by yuioto <yuiotochan@outlook.com>

pkgname=wiliwili
pkgver=1.6.0
pkgrel=1
pkgdesc='专为手柄控制设计的第三方跨平台B站客户端'
arch=('x86_64' 'aarch64')
url='https://github.com/xfangfang/wiliwili'
license=('GPL-3.0-or-later')
depends=('curl' 'dbus' 'fmt' 'gcc-libs' 'glibc' 'hicolor-icon-theme' 'libwebp' 'mpv' 'opencc' 'openssl' 'pystring' 'qrcodegencpp-cmake' 'tinyxml2' 'zlib')
makedepends=('cmake' 'git' 'libxi' 'libxinerama' 'ninja' 'python' 'wayland-protocols')
source=("${pkgname}"::"git+${url}.git#tag=v${pkgver}")
b2sums=('4cbc2b1d5d043e1b570345bcc8d5d4e291e4339455a19602fa33f7bbc2fab17c40acf65ef5402b3961416edef63ed48aac4dad3c632fd9307134657ca4cecdaa')

prepare() {
  git -C "${srcdir}/${pkgname}" rm library/{OpenCC,QR-Code-generator,pystring}
  git -C "${srcdir}/${pkgname}" submodule update --init --recursive

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
