# Maintainer: farseerfc <farseerfc@gmail.com>

pkgname=glmark2
pkgver=2020.04
pkgrel=1
pkgdesc="OpenGL (ES) 2.0 benchmark"
arch=('i686' 'x86_64')
url="https://launchpad.net/glmark2"
license=('GPL' 'zlib' 'custom')
groups=()
depends=('libjpeg-turbo' 'libpng' 'libx11' 'libxcb' 'libgl' 'python2')
makedepends=()
optdepends=()
source=("https://github.com/glmark2/glmark2/archive/$pkgver.tar.gz")
md5sums=('a90713700a740180fef3576f7ee3c9db')

prepare(){
  cd "$srcdir/$pkgname-$pkgver"
  sed -i "s|-Werror ||g" wscript
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
