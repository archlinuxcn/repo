# Maintainer: Deon Spengler <deon.spengler@gmail.com>
pkgname="unagi"
pkgver=0.3.4
pkgrel=1
pkgdesc="Compositing manager which aims to be efficient, lightweight and responsive"
arch=('i686' 'x86_64')
url="http://projects.mini-dweeb.org/projects/unagi"
license=('GPL')
depends=("libxcb>=1.8" "xcb-proto>=1.6" "xproto" "confuse" "libxdg-basedir>=1.0.0" "xcb-util-keysyms" "xcb-util-renderutil" "xcb-util-wm" "xcb-util-image" "libev")
makedepends=("pkgconfig")
backup=()
source=("http://projects.mini-dweeb.org/attachments/download/114/${pkgname}-${pkgver}.tar.gz")
md5sums=('1f9373a69a1318d5a09f6144dfcf54a2')

build() {
  cd "$srcdir/$pkgname-$pkgver"

  ./configure --prefix=/usr
  make || return 1
}

package() {
  cd "$srcdir/$pkgname-$pkgver"

  make DESTDIR="$pkgdir/" includedir="/usr/include/unagi" install

  # Remove libtool files.
  find $pkgdir -name "*.la" | xargs rm
}
