# Maintainer: Jon Eyolfson <jon@eyolfson.com>
pkgname=emacs-evil
_emacs_pkgname=evil
pkgver=1.2.13
pkgrel=1
pkgdesc="An extensible vi layer for Emacs"
url="https://www.emacswiki.org/emacs/Evil"
arch=('any')
license=('GPLv2')
depends=('emacs' 'emacs-undo-tree')
source=("https://github.com/emacs-evil/evil/archive/${pkgver}.tar.gz")
sha256sums=('1045be9cd46f77113421a07c7ad6d1af629e152b0698cdc981d5305dbbfec3fc')

build() {
  cd "${srcdir}/evil-${pkgver}"
  make
}

package() {
  cd "${srcdir}/evil-${pkgver}"
  install -d "${pkgdir}/usr/share/emacs/site-lisp/${_emacs_pkgname}"
  install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/${_emacs_pkgname}"
}
