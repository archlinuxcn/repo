# Maintainer: willemw <willemw12@gmail.com>
# Contributor: Oliver Rümpelein <arch@pheerai.de>

pkgname=mergerfs
pkgver=2.38.0
pkgrel=1
pkgdesc='Featureful union filesystem'
arch=(x86_64)
url=https://github.com/trapexit/mergerfs
license=(custom:ISC)
# Optional makedepend: 'pandoc: build man page'
#optdepends=('fuse2: mount via fstab' 'mergerfs-tools: manage data in a pool')
optdepends=('fuse2: mount via fstab' 'mergerfs-tools-git: manage data in a pool')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
#source=("$pkgname-$pkgver.tar.gz::$url/releases/download/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('cdb855c797da16ae668a2f71f76830151c377b38dee698c63db092ca1635d95e')

prepare() {
  sed -i 's|^\(VERSION=\).*|\1"'$pkgver'"|' $pkgname-$pkgver/tools/update-version
}

build() {
  make -C $pkgname-$pkgver
}

package() {
  install -Dm644 $pkgname-$pkgver/LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  make -C $pkgname-$pkgver DESTDIR="$pkgdir" PREFIX=/usr SBINDIR=/usr/bin install
}
