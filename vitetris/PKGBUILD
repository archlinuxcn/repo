# Maintainer: Jaroslav Lichtblau <dragonlord@aur.archlinux.org>
# Contributor: flu
# Contributor: Kevin MacMartin <prurigro at gmail dot com>

pkgname=vitetris
pkgver=0.57
pkgrel=2
pkgdesc="A terminal-based Tetris clone with 2-player mode"
arch=('i686' 'x86_64')
url="http://victornils.net/tetris"
license=('BSD')
depends=('ncurses')
makedepends=('patch')
options=('!makeflags')
install=$pkgname.install
source=(http://victornils.net/tetris/${pkgname}-${pkgver}.tar.gz
        $pkgname-makefile.patch
        $pkgname.tmpfiles.conf)
md5sums=('07d02ee03e2edd66a8741729e237f21f'
         '23be30294af1dbc43c594a8b737091c8'
         'c4c6a6d4250c0aa3bbf3c4a7d911fa1c')

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
