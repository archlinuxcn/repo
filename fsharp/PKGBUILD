# Contributor: Brett Gilio <owner@brettgilio.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Mort Yao <soi@mort.ninja>
# Contributor: Balló György <ballogyor+arch at gmail dot com>

pkgname=fsharp
pkgver=4.5.0
pkgrel=3
pkgdesc="The F# Compiler, Core Library & Tools (F# Software Foundation Repository)"
arch=('any')
url="http://fsharp.org/"
license=('MIT')
depends=('mono' 'msbuild-stable')
source=("$pkgname-$pkgver.tar.gz::https://github.com/fsharp/fsharp/archive/$pkgver.tar.gz")
sha256sums=('71be24bd4bac47fcad3f9e544c17f23fea9ebce3b47082720804f3f9f1b08f16')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  prefix=/usr
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make prefix="/usr" DESTDIR="$pkgdir" install
}
