# Contributor: tuxce <tuxce.net@gmail.com>
pkgname=package-query
pkgver=1.6.1
pkgrel=1
pkgdesc="Query ALPM and AUR"
arch=('i686' 'x86_64' 'mips64el' 'armv6h' 'armv7h' 'arm')
url="https://github.com/archlinuxfr/package-query/"
license=('GPL')
depends=('pacman>=4.1' 'pacman<4.3' 'yajl>=2.0')
source=(http://mir.archlinux.fr/~tuxce/releases/$pkgname/$pkgname-$pkgver.tar.gz)
md5sums=('d98e79f5c459e6625b0d609f84b33f17')

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
