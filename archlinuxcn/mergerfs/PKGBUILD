# Maintainer: willemw <willemw12@gmail.com>
# Contributor: Oliver Rümpelein <arch@pheerai.de>

pkgname=mergerfs
pkgver=2.28.3
pkgrel=1
pkgdesc="FUSE based union filesystem"
arch=('x86_64')
url="https://github.com/trapexit/mergerfs"
license=('custom:ISC')
makedepends=('git')    # 'pandoc'
source=("https://github.com/trapexit/mergerfs/archive/$pkgver.tar.gz")
#source=("https://github.com/trapexit/mergerfs/releases/download/$pkgver/mergerfs-$pkgver.tar.gz")
md5sums=('c4c92cb9aa6c0ceab84c886eb57b2afc')

prepare() {
  cd $pkgname-$pkgver
  sed -i 's|^VERSION=.*|VERSION="'$pkgver'"|' tools/update-version
}

build() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" PREFIX="/usr" SBINDIR="/usr/bin"
}

package() {
  cd $pkgname-$pkgver
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  make DESTDIR="$pkgdir" PREFIX="/usr" SBINDIR="/usr/bin" install
}

