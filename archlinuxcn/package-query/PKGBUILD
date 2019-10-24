# Contributor: tuxce <tuxce.net@gmail.com>
# Contributor: Skunnyk <skunnyk@archlinux.fr>
pkgname=package-query
pkgver=1.10
pkgrel=1
pkgdesc="Query ALPM and AUR"
arch=('i686' 'x86_64' 'mips64el' 'armv6h' 'armv7h' 'arm' 'aarch64')
url="https://github.com/archlinuxfr/package-query/"
license=('GPL')
depends=('pacman>=5.2' 'yajl>=2.0')
source=(https://github.com/archlinuxfr/$pkgname/releases/download/$pkgver/$pkgname-$pkgver.tar.gz)

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
md5sums=('19b11ca4e5d05fa39775bd395602174e')
