# Maintainer:
# Contributor: Lukas Jirkovsky <l.jirkovsky@gmail.com>
# Contributor: Geraud Le Falher <daureg@gmail.com>

_pkgname="log4cpp"
pkgname="$_pkgname"
pkgver=1.1.4
pkgrel=3
pkgdesc="A library of C++ classes for flexible logging to files, syslog, IDSA and other destinations"
url="http://log4cpp.sourceforge.net/"
license=('LGPL-2.1-only')
arch=('x86_64')

depends=('libnsl')

_pkgsrc="$_pkgname"
source=("https://downloads.sourceforge.net/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('696113659e426540625274a8b251052cc04306d8ee5c42a0c7639f39ca90c9d6')

build() {
  cd "$_pkgsrc"
  ./configure --prefix=/usr --disable-doxygen --disable-dot --without-idsa
  make
}

package() {
  cd "$_pkgsrc"
  make DESTDIR="$pkgdir" install
}
