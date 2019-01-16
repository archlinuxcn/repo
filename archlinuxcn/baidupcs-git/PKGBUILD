# Maintainer: wangjiezhe <wangjiezhe AT yandex DOT com>
pkgname=baidupcs-git
_pkgname=BaiduPCS
pkgver=0.3.1.9.g82f5b7e
pkgrel=1
pkgdesc="The terminal utility for Baidu Network Disk"
arch=('x86_64')
url="https://github.com/GangZhuo/BaiduPCS"
license=('MIT')
depends=('curl' 'openssl')
makedepends=('git')
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
