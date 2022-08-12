# Maintainer: Chuan Ji <chuan@jichu4n.com>
# Contributor: farseerfc <farseerfc@archlinuxcn.org>

pkgname=jfbview
pkgver=0.6.0
pkgrel=3
pkgdesc="PDF and image viewer for the Linux framebuffer"
arch=('i686' 'pentium4' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/jichu4n/jfbview"
license=('Apache')
makedepends=('cmake' 'git')
depends=('freetype2' 'harfbuzz' 'imlib2' 'libjpeg-turbo' 'ncurses' 'openjpeg2' 'zlib')
source=("git+${url}.git#tag=${pkgver}")
sha512sums=('SKIP')

prepare() {
  cd "${srcdir}/${pkgname}"
  git submodule update --init --recursive
}

build(){
  cd "${srcdir}/${pkgname}"
  LDFLAGS='-lImlib2' \
  cmake -H. -Bbuild \
      -DBUILD_TESTING=OFF \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package(){
  cd "${srcdir}/${pkgname}/build"
  make DESTDIR="${pkgdir}" install
}

# vim:set ts=2 sw=2 et:
