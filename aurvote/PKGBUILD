# Maintainer: Javier Tia <javier dot tia at gmail dot com>

pkgname=aurvote
pkgver=1.9
pkgrel=3
pkgdesc="Tool to vote for favorite AUR packages"
url="https://github.com/archlinuxfr/aurvote"
license=('GPL')
arch=('any')
depends=('curl')
conflicts=('aurvote-git')
replaces=('aurvote-git')
source=("${url}/archive/${pkgver}.tar.gz")
sha256sums=('bd888c25b376e97bfad1c8f2fd0eefb4db0821ff422356d985009ba287425da7')

package() {
  cd ${srcdir}/${pkgname}-${pkgver}
  install -Dm 755 aurvote "${pkgdir}/usr/bin/aurvote"
  install -Dm 644 zsh-completion "${pkgdir}/usr/share/zsh/site-functions/_aurvote"
}

# vim:set ft=sh ts=2 sw=2 et:
