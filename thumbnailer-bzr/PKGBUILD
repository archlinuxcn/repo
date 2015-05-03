# Original uploader in CCR: FranzMari
# Original uploader in AUR: Llumex03

pkgname=thumbnailer-bzr
_pkgname=thumbnailer
pkgver=119
pkgrel=1
pkgdesc="A simple shared library that produces and stores thumbnails"
arch=('x86_64' 'x64')
license=('GPL3')
url=("https://launchpad.net/thumbnailer")
provides=('thumbnailer')
depends=('qt5-base' 'gstreamer' 'gst-plugins-base' 'gdk-pixbuf2' 'libexif' 'libsoup' 'libxml2' 'qt5-declarative')
makedepends=('cmake' 'bzr' 'gtest')
source=(bzr+lp:thumbnailer)
md5sums=('SKIP')
 
pkgver() {
 
    cd $_pkgname
    bzr revno
}
 
prepare() {
    cd $_pkgname
    mkdir -p build
}
 
build() {
  cd $_pkgname/build
  cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib
  make
}
 
package(){
 
  cd $_pkgname/build
  make DESTDIR="$pkgdir" install
}  
 
