# Maintainer: Aaron Paden <aaronbpaden@gmail.com>
# Contributor: Natalia Portillo <claunia@clania.com>
pkgname=pcem
pkgver=15
pkgrel=1
pkgdesc="Emulator for various IBM PC computers and clones."
url="http://pcem-emulator.co.uk/"
arch=('x86_64' 'i686')
license=('GPL2')
depends=('wxgtk2' 'openal' 'sdl2')
source=("http://pcem-emulator.co.uk/files/PCemV${pkgver}Linux.tar.gz")

build() {
  cd "${srcdir}"
  ./configure --enable-release-build --enable-networking --prefix=/usr
  make
}

package() {
  cd "${srcdir}"
  make DESTDIR="${pkgdir}" install
  install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}

# vim:set ts=2 sw=2 et:
sha256sums=('b501d3fc2b11bb6127d23fbbcd2de14aabf53460db52daf5d664a80c6f5c85f0')
