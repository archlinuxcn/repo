# Contributor: Timothy Redaelli <timothy.redaelli@gmail.com>
# Contributor: Rorschach <r0rschach@lavabit.com>
# Contributor: Mikhail Felixoid Shiryaev <mr.felixoid na gmail.com>

pkgname=vidalia
pkgver=0.2.21
pkgrel=5
pkgdesc="Controller GUI for Tor"
url="https://www.torproject.org/vidalia"
arch=('i686' 'x86_64')
license=('GPL')
depends=('geoip' 'qt4' 'tor')
makedepends=('cmake')
install=vidalia.install
source=(https://dist.torproject.org/vidalia/$pkgname-$pkgver.tar.gz{,.asc} vidalia.install TorSettings.h.patch)
sha256sums=('c4008e7e7781dddf4a8670a435da6496dc9309dbdbc6125ac6d2cc871bdc1be7'
            'SKIP'
            'c20e899df28939abd84fd3ec0e2e62058e85da0a42e123af732cdaabb7da177e'
            '3162d613ede727088fcb48d26b09ebb5246e103d74b0ca95834ce30a0cbe6ffb')
validpgpkeys=('8738A680B84B3031A630F2DB416F061063FEE659')

build() {
  patch -i TorSettings.h.patch ${pkgname}-${pkgver}/src/vidalia/config/TorSettings.h
  cd "$srcdir"
  mkdir -p build
  cd build
  cmake -D CMAKE_INSTALL_PREFIX=/usr -DUSE_GEOIP=1 ../$pkgname-$pkgver
  make
}

package() {
  cd "$srcdir/build"
  make DESTDIR="$pkgdir/" install
  install -Dm644 ../$pkgname-$pkgver/doc/vidalia.1 "$pkgdir"/usr/share/man/man1/vidalia.1 || return 1
}
