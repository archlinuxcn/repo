# Maintainer: Ronald van Haren <ronald.archlinux.org>
# Contributor: Damir Perisa <damir.perisa@bluewin.ch>

pkgname=stellarium
pkgver=0.22.0
pkgrel=1
pkgdesc="A stellarium with great graphics and a nice database of sky-objects"
arch=('x86_64')
url="https://stellarium.org/"
license=('GPL2')
depends=('libpng' 'libgl' 'freetype2' 'openssl' 'gpsd'
         'qt5-serialport' 'qt5-multimedia' 'qt5-location' 'qt5-charts' 'qt5-script')
makedepends=('cmake' 'mesa' 'qt5-tools')
source=(https://github.com/Stellarium/stellarium/releases/download/v$pkgver/$pkgname-$pkgver.tar.gz{,.asc})
validpgpkeys=('79151C2E6351E7278DA1A730BF38D4D02A328DFF')  # Alexander Wolf <alex.v.wolf@gmail.com>
sha256sums=('0b4dc23cf9054b5e76cd9bc5ad68e172eb221999e90af37e93667d04fe78c885'
            'SKIP')

build() {
  cd ${pkgname}-${pkgver}

  cmake . -DCMAKE_INSTALL_PREFIX=/usr
  make
}


package() {
  cd ${pkgname}-${pkgver}
 
  make DESTDIR="${pkgdir}" install
}
