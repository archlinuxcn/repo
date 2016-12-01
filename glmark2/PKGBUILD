# Maintainer: farseerfc <farseerfc@gmail.com>

pkgname=glmark2
pkgver=2014.03
pkgrel=2
pkgdesc="OpenGL (ES) 2.0 benchmark"
arch=('i686' 'x86_64')
url="https://launchpad.net/glmark2"
license=('GPL' 'zlib' 'custom')
groups=()
depends=('libjpeg-turbo' 'libpng' 'libx11' 'libxcb' 'libgl' 'python2')
makedepends=()
optdepends=()
source=("https://launchpad.net/glmark2/trunk/$pkgver/+download/$pkgname-$pkgver.tar.gz"
        'pr24.patch::https://patch-diff.githubusercontent.com/raw/glmark2/glmark2/pull/24.patch'
        'libpng16.patch::https://github.com/glmark2/glmark2/commit/499aa81a68fb4c8aac1c80f0d6a4cce05941c4cc.patch')
md5sums=('739859cf57d4c8a23452c43e84f66e56'
         '108cbcdf594782dbdcb5908f68db86d7'
         'e1e498bbaf059a1ce886999b25e6ed78')

prepare(){
  cd "$srcdir/$pkgname-$pkgver"
  patch -p1 <../pr24.patch
  patch -p1 <../libpng16.patch
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python2 ./waf configure --prefix=/usr --with-flavors x11-gl,x11-glesv2
  python2 ./waf
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python2 ./waf install --destdir="$pkgdir/"
}
