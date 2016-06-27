# Maintainer: Fredrik Haikarainen <fredrik.haikarainen@gmail.com>
pkgname=light
pkgver=0.9
pkgrel=1
pkgdesc='Program to easily change brightness on backlight-controllers.'
arch=('any')
url="https://github.com/haikarainen/light"
license=('GPL3')
makedepends=('git')
conflicts=('lightscript' 'light-git')
provides=('lightscript' 'light-git')
replaces=('lightscript')
source=('git+https://github.com/haikarainen/light.git#tag=v0.9')
md5sums=('SKIP')

build(){
  cd "$srcdir/light"
  make
}

package(){
  cd "$srcdir/light"
  make DESTDIR="$pkgdir/" install
}
