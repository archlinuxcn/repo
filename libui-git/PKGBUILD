# Contributor: Yauheni Kirylau <yawghen-gmail-dot-com>

_pkgname=libui
pkgname=${_pkgname}-git
pkgver=r1914.84b392d
pkgrel=1
pkgdesc='A portable GUI library for C'
arch=('i686' 'x86_64')
url='https://github.com/andlabs/libui'
license=('MIT')
depends=('gtk3' 'libx11' 'libxcb' 'libffi')
makedepends=('make' 'gcc')
provides=('libui')
conflicts=('libui')
source=("$pkgname::git://github.com/andlabs/libui.git")
md5sums=('SKIP')

pkgver() {
  cd $pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd $pkgname
  make
}

package() {
  cd $pkgname
  mkdir -p $pkgdir/usr/{lib,include}
  make DESTDIR="$pkgdir/" install
}
