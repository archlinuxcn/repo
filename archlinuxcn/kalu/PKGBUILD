# Maintainer: jjacky
pkgname=kalu
pkgver=4.3.0
pkgrel=1
pkgdesc="Upgrade notifier w/ AUR support, watched (AUR) packages, news"
arch=('i686' 'x86_64')
url="https://jjacky.com/kalu"
license=('GPL3+')
depends=('dbus' 'polkit' 'gtk3' 'pacman>=5.1' 'pacman<5.2' 'curl' 'libnotify'
         'notification-daemon')
makedepends=('perl' 'groff')
source=(https://jjacky.com/$pkgname/$pkgname-$pkgver.tar.xz)
install=kalu.install
sha1sums=('4e9fc8b311077d3720af8619de04c917c01acbfb')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
  chmod 750 "$pkgdir/usr/share/polkit-1/rules.d"
  chown 0:102 "$pkgdir/usr/share/polkit-1/rules.d"
}

# vim:set ts=2 sw=2 et:
