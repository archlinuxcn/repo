# Contributor: FigoDaPaura <ffigoDaPaura>

pkgname=lib32-virtualgl
pkgver=2.3.2
pkgrel=1
pkgdesc="32-bit serverside components for 64-bit VirtualGL servers."
arch=('x86_64')
url="http://virtualgl.org"
license=('LGPL')
depends=('virtualgl' 'lib32-libxv' 'lib32-turbojpeg' 'lib32-mesa' 'lib32-libx11' 'lib32-libxext' 'lib32-libxau')
makedepends=('cmake' 'gcc-multilib')
conflicts=('virtualgl32-bin')
md5sums=('29aaf0607a1031fa326444ff0321bcec')
 
source=("http://downloads.sourceforge.net/project/virtualgl/VirtualGL/$pkgver/VirtualGL-$pkgver.tar.gz")
 
build() {
  cd "$srcdir/VirtualGL-$pkgver"
 
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
 
  mkdir -p build
  cd build
 
  cmake .. -DCMAKE_INSTALL_PREFIX=/opt/VirtualGL -DTJPEG_INCLUDE_DIR=/usr/include -DTJPEG_LIBRARY=/usr/lib32/libturbojpeg.so \
    -DVGL_LIBDIR=/usr/lib32 -DVGL_BINDIR=/usr/bin -DX11_X11_LIB=/usr/lib32/libX11.so -DX11_Xext_LIB=/usr/lib32/libXext.so \
    -DOPENGL_gl_LIBRARY=/usr/lib32/libGL.so
  make
}
 
package() {
  cd "$srcdir/VirtualGL-$pkgver/build"
  make install DESTDIR="$pkgdir"
 
  cd "$pkgdir/usr"
  mv bin/glxspheres glxspheres-32
  rm -rf bin
  mkdir -p bin
  mv glxspheres-32 bin/
 
  cd "$pkgdir/opt/VirtualGL"
  rm -rf doc
  rm -rf include
}
