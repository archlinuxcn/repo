# Original Maintainer: Lantald  <lantald at Gmx dot com>
# Maintainer: Danilo <aur at dbrgn dot ch>

pkgname=spatialindex
pkgver=1.8.5
pkgrel=1
pkgdesc='An extensible framework that supports robust spatial indexing methods and sophisticated spatial queries.'
arch=('i686' 'x86_64')
url="http://libspatialindex.github.com/"
license=('MIT')
depends=(gcc-libs)
provides=(spatialindex)
conflicts=(libspatialindex-git)
source=("http://download.osgeo.org/libspatialindex/$pkgname-src-$pkgver.tar.gz"
        'LICENSE')
sha256sums=('7caa46a2cb9b40960f7bc82c3de60fa14f8f3e000b02561b36cbf2cfe6a9bfef'
            '170961cdd7754bed14e465eff7d4f22c5df11d8d104310a56a7ee3ab201bc279')

build() {
  cd "$srcdir/$pkgname-src-$pkgver/"
  ./configure --prefix=/usr
  make
}

check() {
  cd "$srcdir/$pkgname-src-$pkgver/"
  make -k check
}

package() {
  cd "$srcdir/$pkgname-src-$pkgver/"
  make DESTDIR="$pkgdir/" install
  install -D -m644 ${srcdir}/LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
