# Maintainer: willemw <willemw12@gmail.com>
# Contributor: Oliver Rümpelein <arch@pheerai.de>

pkgname=mergerfs
pkgver=2.41.0
pkgrel=1
pkgdesc='Featureful union filesystem. Combines directories from various filesystems into a storage pool'
arch=(x86_64)
url=https://github.com/trapexit/mergerfs
license=(ISC)
#optdepends=('mergerfs-tools: manage data in a pool')
optdepends=('mergerfs-tools-git: manage data in a pool')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('663c358cc48b097cf5268e618096dd8cbde8d71e9e5c382ae33473befe607a52')

prepare() {
  #echo -n "$pkgver" >$pkgname-$pkgver/VERSION
  sed -i "s|^\(VERSION=\).*|\1$pkgver|" $pkgname-$pkgver/buildtools/update-version
}

build() {
  make -C $pkgname-$pkgver # LTO=1
}

package() {
  install -Dm644 $pkgname-$pkgver/LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  make -C $pkgname-$pkgver DESTDIR="$pkgdir" PREFIX=/usr SBINDIR=/usr/bin install
}
