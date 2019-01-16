# Maintainer: Jaroslav Lichtblau <dragonlord@aur.archlinux.org>
# Contributor: flu
# Contributor: Kevin MacMartin <prurigro at gmail dot com>

pkgname=vitetris
pkgver=0.57.2
pkgrel=1
pkgdesc="Virtual terminal *tris clone"
arch=('i686' 'x86_64')
url="http://victornils.net/tetris"
license=('BSD')
depends=('ncurses')
makedepends=('patch')
options=('!makeflags')
install=$pkgname.install
source=($pkgname-$pkgver.tar.gz::https://github.com/vicgeralds/$pkgname/archive/v$pkgver.tar.gz
        $pkgname-makefile.patch
        $pkgname.tmpfiles.conf)
sha256sums=('c023b33f663a7a47418652b520e83cdcf8d395584e30ec4bcb5e2b3563d4372b'
            '2a9e1ea8daf42b833719c2fa1098f9e9c6259b8e077ca387eecd9a2ee54cc8af'
            '898c741a41defccd6b38fe3a5b97fb84d5656b2c9df05c79196ac1bf2151ba7d')

prepare() {
  cd ${pkgname}-${pkgver}
  patch -Np1 -i "${srcdir}"/${pkgname}-makefile.patch

# Change configuration file to a standard one:
  sed -i 's|#define CONFIG_FILENAME ".vitetris"|#define CONFIG_FILENAME ".config/vitetris"|' src/config2.h
}

build() {
  cd ${pkgname}-${pkgver}

  ./configure --prefix="${pkgdir}"/usr --docdir="${pkgdir}"/usr/share/${pkgname} --without-x --with-ncurses
  make
  make gameserver
}

package() {
  install -Dm644 ${pkgname}.tmpfiles.conf "${pkgdir}"/usr/lib/tmpfiles.d/${pkgname}.conf

  cd ${pkgname}-${pkgver}
  make install
  install -Dm755 gameserver "${pkgdir}"/usr/bin/${pkgname}-gameserver

# License
  install -Dm644 licence.txt "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
