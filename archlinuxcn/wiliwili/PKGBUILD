# Maintainer: Puqns67 <me@puqns67.icu>
# Contributor: yuioto <yuiotochan@outlook.com>

# This PKGBUILD is base on the AUR repo wiliwili-git, by yuioto <yuiotochan@outlook.com>

pkgname=wiliwili
pkgver=1.2.2
pkgrel=1
pkgdesc='专为手柄控制设计的第三方跨平台B站客户端'
arch=('x86_64' 'aarch64')
url='https://github.com/xfangfang/wiliwili'
license=('GPL3')
depends=('mpv' 'opencc' 'pystring')
makedepends=('cmake' 'git' 'libxi' 'python' 'wayland-protocols')
conflicts=("${pkgname}-git")
source=("${pkgname}"::"git+${url}.git#tag=v${pkgver}")
sha512sums=('SKIP')

prepare() {
  git -C "${srcdir}/${pkgname}" submodule update --init --recursive
}

build() {
  cmake \
    -S "${srcdir}/${pkgname}" \
    -B "${srcdir}/build" \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
    -DGLFW_BUILD_WAYLAND=ON \
    -DGLFW_BUILD_X11=ON \
    -DINSTALL=ON \
    -DPLATFORM_DESKTOP=ON \
    -DUSE_SYSTEM_CURL=ON \
    -DUSE_SYSTEM_OPENCC=ON \
    -DUSE_SYSTEM_PYSTRING=ON

  make -C "${srcdir}/build" wiliwili
}

package() {
  DESTDIR="${pkgdir}" make -C "${srcdir}/build" install
}
