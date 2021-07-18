# Contributor: tuxce <tuxce.net@gmail.com>
# Contributor: Skunnyk <skunnyk@alteroot.org>
pkgname=package-query
pkgver=1.12
pkgrel=1
pkgdesc="Query ALPM and AUR"
arch=('i686' 'x86_64' 'mips64el' 'armv6h' 'armv7h' 'arm' 'aarch64' 'pentium4')
url="https://github.com/archlinuxfr/package-query/"
license=('GPL')
depends=('pacman>=6.0' 'yajl>=2.0')
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
md5sums=('3d91612aa47bb30db5e028251089255b')
