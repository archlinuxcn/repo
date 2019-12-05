# Maintainer: Poscat <poscat@mail.poscat.moe>

pkgname=emacs-websocket
pkgver=1.12
pkgrel=4
pkgdesc="A websocket implementation in elisp, for emacs."
arch=('any')
url="https://github.com/ahyatt/emacs-websocket"
license=('GPL2')
depends=('emacs')
makedepends=()
source=("https://github.com/ahyatt/emacs-websocket/archive/${pkgver}.tar.gz")
noextract=()
sha256sums=('be24796ad47335ce91ec3e142d52ee07f00ca79078312a0759bce135e1bf414e')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    emacs -Q -batch -L . -f batch-byte-compile *.el
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -d "${pkgdir}/usr/share/emacs/site-lisp/websocket"
    install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/websocket/"
}
