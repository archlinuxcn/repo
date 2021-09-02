# Maintainer:  Joost Bremmer <toost.b@gmail.com>
# Contributor: oozyslug <oozyslug at gmail dot com>

pkgname=neovim-plug
pkgver=0.10.0
pkgrel=3
pkgdesc="A Neovim plugin manager"
arch=('any')
url="http://github.com/junegunn/${pkgname#neo}"
license=('MIT')
depends=('neovim')
groups=('neovim-plugins')
source=("${url}/archive/$pkgver.tar.gz"
        "$pkgname.init.vim")

sha512sums=('403ff120014f667f8955fe7d4f065c4a519d0f641c24321b90c50912cc97a6e3711a8ad92abc95031e71ee8bc00985ec13f43a7fdd43fe62dd2a9958a9f59b25'
            'fb943ed92e20277bed6ff29da973cd96ba05c89dbde438d1bf7821cd810151a08101a67338381fac5ce0df8716c71313f30aa8202b1a75054a9d343f873a9414')
install=neovim-plug.install

package() {
  install -Dm 644 ${pkgname#neo}-${pkgver}/plug.vim ${pkgdir}/usr/share/nvim/runtime/autoload/plug.vim
  install -Dm 644 "$pkgname.init.vim" ${pkgdir}/usr/share/doc/neovim-plug/init.vim.sample
  # no LICENSE file offered.
}
# vim: set ts=2 sw=2 et:
