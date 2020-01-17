# Mintainer: Timothy Redaelli <timothy.redaelli@gmail.com>
# Mintainer: Rorschach <r0rschach@lavabit.com>
# Mintainer: Mikhail Felixoid Shiryaev <mr.felixoid na gmail.com>
# Contributor: Kevin Wilms <niemandausduisburg@gmx.net>
# └ patch for version 0.3.1

pkgname=vidalia
pkgver=0.3.1
pkgrel=1
pkgdesc="Controller GUI for Tor"
url="https://www.torproject.org/vidalia"
arch=('i686' 'x86_64')
license=('GPL')
depends=('geoip' 'qt4' 'tor')
makedepends=('cmake')
install=vidalia.install
source=(
  https://archive.torproject.org/tor-package-archive/vidalia/$pkgname-$pkgver.tar.gz
  https://archive.torproject.org/tor-package-archive/vidalia/$pkgname-$pkgver.tar.gz.asc
  vidalia.install
  TorSettings.h.patch
  PluginEngine.cpp.patch
  PluginEngine.h.patch
)
sha256sums=(
  '1523d31ea6a3eaa11d4665eccfcb2dc755a4c6945d9e2d311032a300a9e583d7'
  '77c6166ed095b6836ff09e776dcd265b41fefd47fdf84bbc1de89321cfa66d04'
  'c20e899df28939abd84fd3ec0e2e62058e85da0a42e123af732cdaabb7da177e'
  '78f4db89ff4408d0063ff964250bda7d9faba0e631da1d041cf4e3a4906f0ee5'
  'df0e05e5c2a22c8c067ebf61a5816b540cd0d13346c5f4d36f32893f79191031'
  '54e6f986c2e68ceceb4ddbcaf398cb61bc5daf265032549c56e2e5cb7345a850'
)
validpgpkeys=('553D7C2C626EF16F27F330BC95E3881D9A753A6B')

build() {
  patch -i TorSettings.h.patch ${pkgname}-${pkgver}/src/vidalia/config/TorSettings.h
  patch -i PluginEngine.cpp.patch ${pkgname}-${pkgver}/src/vidalia/plugin/PluginEngine.cpp
  patch -i PluginEngine.h.patch ${pkgname}-${pkgver}/src/vidalia/plugin/PluginEngine.h
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
