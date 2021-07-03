# Contributor: Alex Whitt <alex.joseph.whitt@gmail.com>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

_pkgsrcname=queue
_pkgdestdirname=queue
pkgver=0.2
pkgrel=1
pkgdesc="Queue data structure"
pkgname=emacs-${_pkgdestdirname}
arch=(any)
url="https://elpa.gnu.org/packages/${_pkgsrcname}.html"
license=('GPL3')
depends=('emacs')
source=("https://elpa.gnu.org/packages/${_pkgsrcname}-${pkgver}.el")
sha256sums=('6be60aa5f429e0e3e2c000563356855e3edb7f5378ebf8499ed35aac1141a233')

build() {
  mv ${_pkgsrcname}-${pkgver}.el ${_pkgsrcname}.el
  emacs -q --no-splash -batch -L . -f batch-byte-compile *.el
}

package() {
  mkdir -p "$pkgdir"/usr/share/emacs/site-lisp/${_pkgdestdirname}/
  install -m644 *.el{c,} "$pkgdir"/usr/share/emacs/site-lisp/${_pkgdestdirname}/
}
