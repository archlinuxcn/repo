# Maintainer: Poscat <poscat@mail.poscat.moe>
# Contributor: Alex Whitt <alex.joseph.whitt@gmail.com>

pkgname=emacs-projectile
pkgver=2.0.0
pkgrel=11
pkgdesc="Project Interaction Library for Emacs"
arch=(any)
url="https://github.com/bbatsov/projectile"
license=('GPL3')
depends=('emacs' 'emacs-pkg-info')
source=("https://github.com/bbatsov/projectile/archive/v${pkgver}.tar.gz")
sha256sums=('4996f72ee8520983bee9b79c9a69ccca9bdd989fce07d66b854eb1bedc86fa3a')

build() {
  cd "${srcdir}/projectile-${pkgver}"
  emacs -q --no-splash -batch -L . -f batch-byte-compile *.el
}

package() {
  cd "${srcdir}/projectile-${pkgver}"
  mkdir -p "${pkgdir}/usr/share/emacs/site-lisp/projectile/"
  install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/projectile/"
}
