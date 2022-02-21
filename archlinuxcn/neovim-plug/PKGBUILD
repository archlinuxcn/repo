# Maintainer:  Joost Bremmer <toost.b@gmail.com>
# Contributor: oozyslug <oozyslug at gmail dot com>

pkgname=neovim-plug
pkgver=0.11.0
pkgrel=3
pkgdesc="A Neovim plugin manager"
arch=('any')
url="http://github.com/junegunn/${pkgname#neo}"
license=('MIT')
depends=('neovim')
groups=('neovim-plugins')
source=("${url}/archive/$pkgver.tar.gz"
        "$pkgname.init.vim")

sha512sums=('79ff462790dad8e517a60f698d18e7038bc14f3f018c75a45d840d6f47c9987ee12cd84b44acb3b2fbc0d0e10ce9449aad51656c67d8b3ba675225e3c58459a2'
            'fb943ed92e20277bed6ff29da973cd96ba05c89dbde438d1bf7821cd810151a08101a67338381fac5ce0df8716c71313f30aa8202b1a75054a9d343f873a9414')
install=neovim-plug.install

package() {
  install -Dm 644 ${pkgname#neo}-${pkgver}/plug.vim ${pkgdir}/usr/share/nvim/runtime/autoload/plug.vim
  install -Dm 644 "$pkgname.init.vim" ${pkgdir}/usr/share/doc/neovim-plug/init.vim.sample
  # no LICENSE file offered.
}
# vim: set ts=2 sw=2 et:
