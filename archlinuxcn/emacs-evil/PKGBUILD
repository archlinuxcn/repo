# Maintainer: Jon Eyolfson <jon@eyolfson.com>
pkgname=emacs-evil
_emacs_pkgname=evil
pkgver=1.14.0
pkgrel=1
pkgdesc="An extensible vi layer for Emacs"
url="https://www.emacswiki.org/emacs/Evil"
arch=('any')
license=('GPLv2')
depends=('emacs' 'emacs-undo-tree')
source=("https://github.com/emacs-evil/evil/archive/${pkgver}.tar.gz")
sha256sums=('5fcf711112597aa6d80f3fac798ed150c956b4c27fa74c8260aab915c6080199')

build() {
  cd "${srcdir}/evil-${pkgver}"
  make
}

package() {
  cd "${srcdir}/evil-${pkgver}"
  install -d "${pkgdir}/usr/share/emacs/site-lisp/${_emacs_pkgname}"
  install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/${_emacs_pkgname}"
}
