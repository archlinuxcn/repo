# $Id: PKGBUILD 219618 2014-08-12 11:48:23Z bpiotrowski $
# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Michal Bozon <michal.bozon__at__gmail.com>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libyaml
pkgname=libx32-libyaml
pkgver=0.1.6
pkgrel=1.1
pkgdesc="YAML 1.1 library (x32 ABI)"
arch=('x86_64')
url="http://pyyaml.org/wiki/LibYAML"
license=('MIT')
depends=('libx32-glibc' $_pkgbasename)
source=(http://pyyaml.org/download/libyaml/yaml-$pkgver.tar.gz)
md5sums=('5fe00cda18ca5daeb43762b80c38e06e')

build() {
  export CC='gcc -mx32'
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH=/usr/libx32/pkgconfig

  cd "$srcdir/yaml-$pkgver"
  ./configure --prefix=/usr --libdir=/usr/libx32
  make
}

package() {
  cd "$srcdir/yaml-$pkgver"
  make DESTDIR="$pkgdir" install

  rm -rf "${pkgdir}/usr/include"

  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

