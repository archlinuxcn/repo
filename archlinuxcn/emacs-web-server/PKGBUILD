# Maintainer: Poscat <poscat@mail.poscat.moe>

pkgname=emacs-web-server
pkgver=0.1.0
pkgrel=6
pkgdesc="web server running Emacs Lisp handlers."
arch=('any')
url="https://github.com/eschulte/emacs-web-server"
license=('GPL3')
depends=('emacs')
makedepends=()
source=("https://github.com/eschulte/emacs-web-server/archive/version-${pkgver}.tar.gz")
noextract=()
sha256sums=('9983c1f208078dad00d5fb8259b6812b0959acc5917c899be4b6dc344a0622cc')

build() {
    cd "${srcdir}/${pkgname}-version-${pkgver}"
    emacs -Q -batch -L . -f batch-byte-compile *.el
}

package() {
    cd "${srcdir}/${pkgname}-version-${pkgver}"
    mkdir -p "${pkgdir}/usr/share/emacs/site-lisp/web-server/"
    install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/web-server/"
}
