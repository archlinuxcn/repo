# Maintainer: willemw <willemw12@gmail.com>
# Contributor: Oliver Rümpelein <arch@pheerai.de>

pkgname=mergerfs
pkgver=2.42.0
pkgrel=2
pkgdesc='Featureful union filesystem. Combines directories from various filesystems into a storage pool'
arch=(x86_64)
url=https://github.com/trapexit/mergerfs
license=(ISC)
depends=(lshw)
optdepends=(
  'lsb-release: for mergerfs.collect-info'
  'lshw: for mergerfs.collect-info'
  #'mergerfs-tools: manage data in a pool'
  'mergerfs-tools-git: manage data in a pool')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('b805ddcb9dbee66f6bdfc3901ef3e1d978b4fd2973d5b2c9907c9aed937ef705')

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
