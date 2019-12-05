# Maintainer: Poscat <poscat@mail.poscat.moe>

pkgname=emacs-use-package
pkgver=2.4
pkgrel=4
pkgdesc="A use-package declaration for simplifying your .emacs"
url="https://github.com/jwiegley/use-package"
arch=('any')
license=('GPL2')
depends=('emacs')
makedepends=('git')
provides=('emacs-use-package')
source=("https://github.com/jwiegley/use-package/archive/${pkgver}.tar.gz")
sha256sums=('f26f1b35e47612c8b5ccc956cc0288b581a59bcc9cdcb8370123c904d7b17a3a')

build() {
  cd "${srcdir}/use-package-${pkgver}"
  emacs -Q -batch -L . -f batch-byte-compile *.el
}

package() {
  cd "${srcdir}/use-package-${pkgver}"
  install -d "${pkgdir}/usr/share/emacs/site-lisp/use-package"
  install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/use-package/"
}
