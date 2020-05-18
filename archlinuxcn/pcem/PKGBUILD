# Maintainer: Aaron Paden <aaronbpaden@gmail.com>
# Contributor: Natalia Portillo <claunia@clania.com>
pkgname=pcem
pkgver=16
pkgrel=4
pkgdesc="Emulator for various IBM PC computers and clones."
url="http://pcem-emulator.co.uk/"
arch=('x86_64' 'i686')
license=('GPL2')
depends=('wxgtk2' 'openal' 'sdl2' 'alsa-lib')
source=("http://pcem-emulator.co.uk/files/PCemV${pkgver}Linux.tar.gz"
  use-fcommon.patch)

prepare() {
  cd "${srcdir}"
  # fix build with gcc 10
  patch -p0 <"${srcdir}/use-fcommon.patch"
}
build() {
  cd "${srcdir}"
  autoreconf
  ./configure --enable-alsa --enable-release-build --enable-networking --prefix=/usr
  make
}

package() {
  cd "${srcdir}"
  make DESTDIR="${pkgdir}" install
  install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}

# vim:set ts=2 sw=2 et:
sha256sums=('45ae9321ee25375f0e685a49d84e8a5acba8ed33ccf597299edcf287cb3c8499'
            'a020184887520f58e74a8ebb990fb677af4d40dd87a5602f2336945824c7cea9')
