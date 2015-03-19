# Contributor: Timothy Redaelli <timothy.redaelli@gmail.com>
# Contributor: Rorschach <r0rschach@lavabit.com>

pkgname=vidalia
pkgver=0.2.21
pkgrel=4
pkgdesc="Controller GUI for Tor"
url="https://www.torproject.org/vidalia"
arch=('i686' 'x86_64')
license=('GPL')
depends=('geoip' 'qt4' 'tor')
makedepends=('cmake')
install=vidalia.install
source=(https://dist.torproject.org/vidalia/$pkgname-$pkgver.tar.gz{,.asc} vidalia.install)
sha256sums=('c4008e7e7781dddf4a8670a435da6496dc9309dbdbc6125ac6d2cc871bdc1be7'
            'SKIP'
            'c20e899df28939abd84fd3ec0e2e62058e85da0a42e123af732cdaabb7da177e')
validpgpkeys=('8738A680B84B3031A630F2DB416F061063FEE659')

build() {
  cd "$srcdir"
  mkdir build
  cd build
  cmake -D CMAKE_INSTALL_PREFIX=/usr -DUSE_GEOIP=1 ../$pkgname-$pkgver
  make
}

package() {
  cd "$srcdir/build"
  make DESTDIR="$pkgdir/" install
  install -Dm644 ../$pkgname-$pkgver/doc/vidalia.1 "$pkgdir"/usr/share/man/man1/vidalia.1 || return 1
}