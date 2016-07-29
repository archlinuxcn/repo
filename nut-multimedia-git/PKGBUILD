# Maintainer: Gustavo Alvarez <sl1pkn07@gmail.com>

pkgname=nut-multimedia-git
pkgver=20140619.383658f
pkgrel=1
pkgdesc="Free multimedia container format. (Git Version)"
arch=('i686' 'x86_64')
url="http://wiki.multimedia.cx/index.php?title=NUT"
license=('GPL')
depends=('glibc')
makedepends=('git')
conflicts=('nut-multimedia' 'libnut-git')
provides=('nut-multimedia' 'libnut')
source=("git://git.ffmpeg.org/nut.git")
sha1sums=('SKIP')

pkgver() {
  cd nut
  echo "$(git log -1 --format="%cd" --date=short | tr -d '-').$(git log -1 --format="%h")"
}

build() {
  CFLAGS+=" -fPIC" make -C nut/src/trunk PREFIX=/usr libnut/libnut.so
  make -C nut/src/trunk PREFIX=/usr nututils
}

package() {
  make -C nut/src/trunk PREFIX=/usr DESTDIR="${pkgdir}" install-libnut-shared
  make -C nut/src/trunk PREFIX=/usr DESTDIR="${pkgdir}" install-nututils
}