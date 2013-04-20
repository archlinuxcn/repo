# Maintainer: L42y <423300@gmail.com>
_pkg=pinpoint
pkgname=$_pkg-git
pkgver=0.1.4.40_g9df3bf6
pkgrel=1
pkgdesc="a tool for making hackers do excellent presentations"
arch=('i686' 'x86_64')
url="https://live.gnome.org/Pinpoint"
license=('LGPL')
depends=('clutter' 'gdk-pixbuf2' 'clutter-gst' 'glproto' 'dri2proto')
makedepends=('git')
provides=('pinpoint')
conflicts=('pinpoint')
install=pinpoint.install
_gitname="pinpoint"
_gitroot="http://git.gnome.org/browse/$_gitname"
source=("git+$_gitroot")
md5sums=(SKIP)

pkgver() {
  cd "$srcdir/$_gitname"
  git describe --tags | sed 's/-/./;s/-/_/g'
}

build() {
  cd "$srcdir/$_gitname"

  sed -i -e 's/AM_CONFIG_HEADER(/AC_CONFIG_HEADERS(/' configure.ac
  ./autogen.sh --prefix=/usr
  make
}

package() {
  cd "$srcdir/$_gitname"

  make DESTDIR="$pkgdir/" install

  install -m755 -d "$pkgdir/usr/share/doc/$_pkg"
  install -m644 bg.jpg bowls.jpg linus.jpg "$pkgdir/usr/share/doc/$_pkg"
  install -m755 introduction.pin "$pkgdir/usr/share/doc/$_pkg"

} 
