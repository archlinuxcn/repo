# Maintainer: Daniel Greve <greve.daniel.l@gmail.com>

pkgname=xxd-standalone
pkgver=8.0.0055
pkgrel=1
pkgdesc='Hexdump utility from vim'
arch=('i686' 'x86_64')
url='http://www.vim.org'
license=('MIT' 'GPL2')
provides=('xxd')
conflicts=('vim' 'gvim')
depends=('glibc')
source=("https://raw.githubusercontent.com/vim/vim/v${pkgver}/src/xxd/xxd.c"
        "https://raw.githubusercontent.com/vim/vim/v${pkgver}/runtime/doc/xxd.1"
        'LICENSE')
md5sums=('fbbe3afbc7bdd8f8c6b75f8789292bab'
         '25af84984b44a69ab4f72710a209a00a'
         '533619562b1da5fd32458517fc740af8')

build() {
  ## https://github.com/vim/vim/blob/master/src/xxd/Makefile
  cc -DUNIX -o xxd xxd.c
}

package() {
  install -Dm755 xxd "${pkgdir}/usr/bin/xxd"
  install -Dm644 xxd.1 "${pkgdir}/usr/share/man/man1/xxd.1"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/xxd/LICENSE"
}
