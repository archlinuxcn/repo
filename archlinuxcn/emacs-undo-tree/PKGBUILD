# Maintainer: Jon Eyolfson <jon@eyl.io>
# Contributor: listx <linusarver <at> gmail <dot> com>
pkgname=emacs-undo-tree
pkgver=0.8.1
pkgrel=1
pkgdesc="Replace Emacs' undo system with an intuitive tree-based system."
arch=('any')
url="https://www.dr-qubit.org/undo-tree.html"
depends=('emacs' 'emacs-queue')
makedepends=('git')
license=('GPL')
provides=('emacs-undo-tree')
conflicts=('emacs-undo-tree')
install=$pkgname.install
source=("$pkgname"::"git+https://gitlab.com/tsc25/undo-tree#tag=release/$pkgver")
sha256sums=('SKIP')

build() {
  cd "${srcdir}/${pkgname}"
  emacs -batch -f batch-byte-compile undo-tree.el
}

package() {
  cd "${srcdir}/${pkgname}"
  install -d $pkgdir/usr/share/emacs/site-lisp/undo-tree
  install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/undo-tree"
}
