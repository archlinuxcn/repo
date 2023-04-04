# Maintainer: Kyle Keen <keenerd@gmail.com>
# Contributor: Maarten Baert

pkgname=simplescreenrecorder
pkgver=0.4.4
pkgrel=2
pkgdesc="A feature-rich screen recorder that supports X11 and OpenGL."
arch=("x86_64")
url="https://www.maartenbaert.be/simplescreenrecorder/"
license=("GPL3")
depends=("qt5-base" "qt5-x11extras"
    "ffmpeg" "alsa-lib" "libpulse" "jack" "libgl" "glu"
    "libx11" "libxext" "libxfixes" "libxi" "libxinerama"
    "desktop-file-utils" "gtk-update-icon-cache")
optdepends=("lib32-simplescreenrecorder: OpenGL recording of 32-bit applications")
makedepends=("git" "cmake" "qt5-tools")
source=("git+https://github.com/MaartenBaert/ssr.git#tag=$pkgver"
         ffmpeg5.patch::https://patch-diff.githubusercontent.com/raw/MaartenBaert/ssr/pull/934.patch)
sha256sums=('SKIP'
            '4b01938615a34127236a21ee0ffa20bbb179c8bfcc5ecef872fc5a246727d2e1')

install=simplescreenrecorder.install

prepare() {
  cd ssr
  mkdir -p build

  patch -p1 -i ../ffmpeg5.patch # Fix build with ffmpeg 5
}

build() {
  cd ssr/build
  # fPIC is only required for qt5 + gcc5
  #CXXFLAGS="$CXXFLAGS -fPIC"
  #./configure --prefix=/usr --disable-assert --with-qt5
  #./configure --prefix=/usr --disable-assert
  #  -DLRELEASE='/usr/bin/lrelease-qt4' \
  cmake -DCMAKE_INSTALL_PREFIX="/usr" -DCMAKE_BUILD_TYPE=Release \
    -DWITH_QT5=on \
    -DCMAKE_INSTALL_LIBDIR='lib' ../
  make
}
package() {
  cd ssr/build
  make DESTDIR="$pkgdir" install
}
