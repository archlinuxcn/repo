# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

_pkgname=libav
pkgname=$_pkgname-no-libs-git
pkgver=13_dev0.r1579.g2a9e1c122
pkgrel=1
epoch=1
pkgdesc='Open source audio and video processing tools'
arch=('i686' 'x86_64')
url='https://libav.org/'
license=('LGPL')
depends=('zlib' 'bzip2' 'openssl')
makedepends=('git' 'yasm')
provides=("libav-no-libs=$pkgver" 'libav-git-no-libs')
conflicts=('libav-no-libs')
source=('git+https://github.com/libav/libav.git')
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname
  ( set -o pipefail
    git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
  )
}

build() {
  cd $_pkgname

  ./configure \
    --prefix=/usr \
    --enable-openssl \
    --enable-nonfree

  make
}

package() {
  cd $_pkgname

  make DESTDIR="$pkgdir" install

  rm -r "$pkgdir"/usr/{include,lib}
}
