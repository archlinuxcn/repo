# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Timothy Redaelli <timothy.redaelli@gmail.com>

pkgname="libnbcompat"
pkgver=20180822
_commit=be9f9298fd165ea01a0769c4ffa29a3ec0d22023
pkgrel=1
pkgdesc="Portable NetBSD compatibility library"
arch=('i686' 'x86_64')
url="http://www.netbsd.org/"
license=('BSD')
# The git repo is maintained by Debian
# LICENSE is extracted from nbcompat.h
source=("git+https://github.com/jgoerzen/libnbcompat#commit=$_commit"
        'LICENSE')
md5sums=('SKIP'
         'beab088c74f4e3e456da604c0d62c2e3')
makedepends=('bmake' 'git')
options=('!makeflags')

build() {
  cd libnbcompat

  ./configure \
    --prefix=/usr \
    --enable-db \
    --enable-bsd-getopt

  bmake
}

package() {
  cd libnbcompat

  bmake install DESTDIR="$pkgdir"

  install -Dm644 ../LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
