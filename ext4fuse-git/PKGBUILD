# Maintainer: Yen Chi Hsuan <yan12125@gmail.com>

_pkgname=ext4fuse
pkgname=$_pkgname-git
pkgver=0.1.3.r7.gba01a66
pkgrel=1
pkgdesc="EXT4 implementation for FUSE"
arch=('i686' 'x86_64')
license=('GPL2')
url='https://github.com/gerard/ext4fuse'
depends=('glibc' 'fuse')
makedepends=('git')
source=("git+https://github.com/gerard/ext4fuse")
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  ( set -o pipefail
    git describe --long --tag 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

build() {
    cd "$srcdir/$_pkgname"

    make
}

package() {
    cd "$srcdir/$_pkgname"

    install -Dm755 ext4fuse "$pkgdir"/usr/bin/ext4fuse
}

