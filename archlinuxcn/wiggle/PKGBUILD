# Maintainer: Simon Legner <Simon.Legner@gmail.com>
pkgname=wiggle
pkgver=1.3
pkgrel=1
pkgdesc="A program for applying patches that patch cannot apply because of conflicting changes"
arch=('i686' 'x86_64')
depends=('ncurses')
url="https://github.com/neilbrown/wiggle"
license=('GPL2')
source=($pkgname-$pkgver.tar.gz::https://github.com/neilbrown/$pkgname/archive/v$pkgver.tar.gz)

build() {
  cd "$srcdir/$pkgname-$pkgver"
  # Building with -Wall -Werror fails. Respect CFLAGS from /etc/makepkg.conf
  sed -i -r 's/^CFLAGS=.*/CFLAGS+=-I. /' Makefile
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
}

sha256sums=('ff92cf0133c1f4dce33563e263cb30e7ddb6f4abdf86d427b1ec1490bec25afa')
