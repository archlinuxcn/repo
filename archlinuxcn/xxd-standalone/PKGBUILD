# Maintainer: Fabio 'Lolix' Loli <lolix@disroot.org>
# Contributor: Daniel Greve <greve.daniel.l@gmail.com>

pkgname=xxd-standalone
pkgver=8.0.1658
pkgrel=1
pkgdesc="Hexdump utility from vim"
arch=(x86_64 i686 arm armv6h armv7h aarch64)
url='http://www.vim.org'
license=(GPL2 "custom: MIT-X11") # https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=776191
provides=(xxd)
conflicts=(xxd)
depends=(glibc)
source=("xxd-${pkgver}.c::https://raw.githubusercontent.com/vim/vim/v${pkgver}/src/xxd/xxd.c"
        "https://raw.githubusercontent.com/vim/vim/v${pkgver}/runtime/doc/xxd.1"
        "$pkgname-Makefile::https://raw.githubusercontent.com/vim/vim/master/src/xxd/Makefile"
        "https://raw.githubusercontent.com/FabioLolix/AUR-artifacts/master/xxd-LICENSE")
md5sums=('304e675b808e350c63f412a145eb3e68'
         '87467fa59b7efa85002baa2d78d2c0bb'
         'd551525508580302c1c22a9ec0c0fb84'
         '533619562b1da5fd32458517fc740af8')
# check versions at https://github.com/vim/vim/tree/master/src/xxd

prepare() {
  mv xxd-${pkgver}.c xxd.c
}

build() {
  make -f $pkgname-Makefile
}

package() {
  install -Dm755 xxd "${pkgdir}/usr/bin/xxd"
  install -Dm644 xxd.1 "${pkgdir}/usr/share/man/man1/xxd.1"
  install -Dm644 xxd-LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
