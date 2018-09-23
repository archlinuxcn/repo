# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

_pkgname=ext4fuse
pkgname=$_pkgname-git
pkgver=0.1.3.r15.g325bf27
pkgrel=2
pkgdesc="EXT4 implementation for FUSE"
arch=('i686' 'x86_64')
license=('GPL2')
url='https://github.com/gerard/ext4fuse'
depends=('glibc' 'fuse2')
makedepends=('git')
source=("git+https://github.com/gerard/ext4fuse")
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname
  ( set -o pipefail
    git describe --long --tag 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
  )
}

prepare() {
  cd $_pkgname

  mkdir -p "$srcdir"/tmp
  sed -i "s#mktemp /tmp#mktemp \"$srcdir\"/tmp#" test/lib.sh
}

build() {
  cd $_pkgname

  make
}

check() {
  cd $_pkgname

  # sudo make test
}

package() {
  cd $_pkgname

  install -Dm755 ext4fuse "$pkgdir"/usr/bin/ext4fuse
}
