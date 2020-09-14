# Maintainer: Joseph R. Quinn <quinn period joseph r at protonmail dot com>
# Contributor: Brett Gilio <owner@brettgilio.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Mort Yao <soi@mort.ninja>
# Contributor: Balló György <ballogyor+arch at gmail dot com>

pkgname=fsharp
pkgver=10.2.3
pkgrel=3
pkgdesc="The F# Compiler, Core Library & Tools (F# Software Foundation Repository)"
arch=('any')
url="http://fsharp.org/"
license=('MIT')
depends=('mono' 'msbuild')
conflicts=('fsharp-git' 'fsharp-mono-bin')
source=("$pkgname-$pkgver.tar.gz::https://github.com/fsharp/fsharp/archive/$pkgver.tar.gz")
sha256sums=('527e4bad7a6d71668e905608c82db7c6eda44d9fd2ed9ce3c758e291e024cc4d')

build() {
  cd "$pkgname-$pkgver"
  make prefix=/usr
}

package() {
  cd "$pkgname-$pkgver"
  make prefix=/usr DESTDIR="$pkgdir" install
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/fsharp/LICENSE"
}
