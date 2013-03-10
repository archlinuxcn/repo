# Contributor: FigoDaPaura <ffigoDaPaura>
# Some tweaks by Andres Jimenez

pkgname=virtualgl
pkgver=2.3.2
pkgrel=1
pkgdesc="Redirects 3D commands from an OpenGL application onto a server-side 3D graphics card."
arch=('i686' 'x86_64')
url="http://virtualgl.org"
license=('LGPL')
depends=('libgl' 'libxv' 'glu' 'turbojpeg')
makedepends=('cmake' 'mesa')
provides=('virtualgl')
 
source=("http://downloads.sourceforge.net/project/virtualgl/VirtualGL/$pkgver/VirtualGL-$pkgver.tar.gz")
 
sha1sums=('f042862c21ceaba57c6e1f0ec72adb4f838725e9')
 
build() {
  cd "$srcdir/VirtualGL-$pkgver"
 
  mkdir -p build
  cd build
 
  cmake .. -DCMAKE_INSTALL_PREFIX=/opt/VirtualGL -DTJPEG_INCLUDE_DIR=/usr/include -DTJPEG_LIBRARY=/usr/lib/libturbojpeg.so \
    -DVGL_LIBDIR=/usr/lib -DVGL_BINDIR=/usr/bin
  make
}
 
package() {
  cd "$srcdir/VirtualGL-$pkgver/build"
  make install DESTDIR="$pkgdir"
 
  mkdir -p "$pkgdir/opt/VirtualGL/bin"
  mv "$pkgdir"/usr/bin/glxinfo "$pkgdir/opt/VirtualGL/bin"
}