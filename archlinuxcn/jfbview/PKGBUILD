# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Chuan Ji <ji@chu4n.com>

pkgname=jfbview
pkgver=0.6.0
pkgrel=2
pkgdesc="PDF and image viewer for the Linux framebuffer"
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/jichu4n/jfbview"
license=('Apache')
makedepends=('cmake')
depends=('ncurses' 'imlib2' 'libjpeg-turbo')
conflicts=('jfbpdf')
replaces=('jfbpdf')
source=("https://github.com/jichu4n/jfbview/releases/download/${pkgver}/jfbview-${pkgver}-full-source.zip")
md5sums=('ac41da35a97c008424662d7dc489b841')

build(){
  cd "${srcdir}/${pkgname}-${pkgver}-full-source"
  cmake -H. -Bbuild \
      -DBUILD_TESTING=OFF \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package(){
  cd "${srcdir}/${pkgname}-${pkgver}-full-source/build"
  make DESTDIR="${pkgdir}" install
}

# vim:set ts=2 sw=2 et:
