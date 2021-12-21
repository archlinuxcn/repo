# Maintainer: Vonpupp <vonpupp@gmail.com>

pkgname="unagi"
pkgver=0.3.4
pkgrel=3
pkgdesc="Compositing manager for implementing effects with regular window managers."
arch=('i686' 'x86_64')
url="http://projects.mini-dweeb.org/projects/unagi"
license=('GPL3')
depends=("confuse" "libxdg-basedir" "xcb-util-keysyms" "xcb-util-renderutil" "xcb-util-wm" "xcb-util-image" "libev")
makedepends=("pkgconfig" "xorgproto")
source=("http://projects.mini-dweeb.org/attachments/download/114/$pkgname-$pkgver.tar.gz")
md5sums=('1f9373a69a1318d5a09f6144dfcf54a2')

build() {
  cd "$pkgname-$pkgver"
  mkdir m4
  ./autogen.sh
  ./configure --prefix=/usr --sysconfdir=/etc
  # Fight unused direct deps
  sed -i -e "s/ -shared / $LDFLAGS\0 /g" libtool
  make
}
package() {
  #cd "$srcdir/$_gitname-build"
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" includedir="/usr/include/unagi" install

  # Remove libtool files.
  find $pkgdir -name "*.la" | xargs rm
}
