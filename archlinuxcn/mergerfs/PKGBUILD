# Maintainer: willemw <willemw12@gmail.com>
# Contributor: Oliver Rümpelein <arch@pheerai.de>

pkgname=mergerfs
pkgver=2.40.0
pkgrel=1
pkgdesc='Featureful union filesystem'
arch=(x86_64)
url=https://github.com/trapexit/mergerfs
license=(custom:ISC)
# Optional makedepends: 'pandoc: build man page'
#optdepends=('fuse2: mount via fstab' 'mergerfs-tools: manage data in a pool')
optdepends=('fuse2: mount via fstab' 'mergerfs-tools-git: manage data in a pool')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
#source=("$pkgname-$pkgver.tar.gz::$url/releases/download/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('dea6a23fe25044a393368fd38d263eb7e731423c34a20ddd6ba4f46688edcbaa')

prepare() {
  sed -i "s|^\(VERSION=\).*|\1$pkgver|" $pkgname-$pkgver/buildtools/update-version
}

build() {
  make -C $pkgname-$pkgver
}

package() {
  install -Dm644 $pkgname-$pkgver/LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  make -C $pkgname-$pkgver DESTDIR="$pkgdir" PREFIX=/usr SBINDIR=/usr/bin install

  chmod 4755 "$pkgdir/usr/bin/mergerfs-fusermount"
}
