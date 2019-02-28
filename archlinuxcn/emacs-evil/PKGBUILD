# Maintainer: Jon Eyolfson <jon@eyolfson.com>
pkgname=emacs-evil
_emacs_pkgname=evil
pkgver=1.2.14
pkgrel=1
pkgdesc="An extensible vi layer for Emacs"
url="https://www.emacswiki.org/emacs/Evil"
arch=('any')
license=('GPLv2')
depends=('emacs' 'emacs-undo-tree')
source=("https://github.com/emacs-evil/evil/archive/${pkgver}.tar.gz")
sha256sums=('28f311c13f00ee9716626cd62d97f838bc21184c2b844d8ad4dfa084932516fb')

build() {
  cd "${srcdir}/evil-${pkgver}"
  make
}

package() {
  cd "${srcdir}/evil-${pkgver}"
  install -d "${pkgdir}/usr/share/emacs/site-lisp/${_emacs_pkgname}"
  install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/${_emacs_pkgname}"
}
