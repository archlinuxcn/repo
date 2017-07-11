# Maintainer: wangjiezhe <wangjiezhe AT yandex DOT com>
pkgname=baidupcs-git
_pkgname=BaiduPCS
pkgver=0.2.6.27.g1abd895
pkgrel=1
pkgdesc="The terminal utility for Baidu Network Disk"
arch=('i686' 'x86_64')
url="https://github.com/GangZhuo/BaiduPCS"
license=('MIT')
depends=('curl' 'openssl')
source=("${_pkgname}::git+${url}.git")
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  git describe --tags | sed 's/-/./g'
}

prepare() {
  cd "$srcdir/$_pkgname"
  sed -i "s|http://|https://|g;s|^inline|static inline|" pcs/pcs.c
}

build() {
  cd "$srcdir/$_pkgname"
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/$_pkgname"
  make install DESTDIR=$pkgdir
}

# vim:set ts=2 sw=2 et:
