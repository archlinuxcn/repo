# Maintainer: Jon Eyolfson <jon@eyl.io>
# Contributor: listx <linusarver <at> gmail <dot> com>
pkgname=emacs-undo-tree
pkgver=0.6.6
pkgrel=2
pkgdesc="Replace Emacs' undo system with an intuitive tree-based system."
arch=('any')
url="http://www.dr-qubit.org/tags/computing-code-emacs.html"
depends=('emacs')
license=('GPL')
provides=('emacs-undo-tree')
conflicts=('emacs-undo-tree')
install=$pkgname.install
source=("$pkgname"::'git+http://www.dr-qubit.org/git/undo-tree.git#tag=release/0.6.6')
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
