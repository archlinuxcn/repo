# Contributor: tuxce <tuxce.net@gmail.com>
pkgname=package-query
pkgver=1.5
pkgrel=2
pkgdesc="Query ALPM and AUR"
arch=('i686' 'x86_64' 'mips64el' 'armv6h' 'armv7h' 'arm')
url="https://github.com/archlinuxfr/package-query/"
license=('GPL')
depends=('pacman>=4.1' 'pacman<4.3' curl 'yajl>=2.0')
source=(http://mir.archlinux.fr/~tuxce/releases/$pkgname/$pkgname-$pkgver.tar.gz)
md5sums=('3ad043d6aa87c497a1e6f0a5d2543e33')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --localstatedir=/var --prefix=/usr --sysconfdir=/etc --with-aur-url=https://aur.archlinux.org
  make
}

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
