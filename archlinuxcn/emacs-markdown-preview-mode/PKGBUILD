# Maintainer: Poscat <poscat@mail.poscat.moe>

pkgname=emacs-markdown-preview-mode
pkgver=0.9.2
pkgrel=9
pkgdesc="Minor mode to preview markdown output as you save"
arch=('any')
url="https://github.com/ancane/markdown-preview-mode"
license=('GPL3')
depends=('emacs'
         'discount'
         'emacs-markdown-mode'
         'emacs-websocket'
         'emacs-web-server')
makedepends=()
source=("https://github.com/ancane/markdown-preview-mode/archive/v${pkgver}.tar.gz")
install=${pkgname}.install
noextract=()
sha256sums=('7827f570005a4adc801878fc0a9679fbe015239701a6f8ff7eb6761dfbd15950')

build() {
    cd "${srcdir}/markdown-preview-mode-${pkgver}"
    emacs -batch -L . -f batch-byte-compile *.el
}

package() {
    cd "${srcdir}/markdown-preview-mode-${pkgver}"
    install -d "${pkgdir}/usr/share/emacs/site-lisp/markdown-preview-mode"
    install -m644 *.el{c,} "${pkgdir}/usr/share/emacs/site-lisp/markdown-preview-mode/"
    install -m644 *.html "${pkgdir}/usr/share/emacs/site-lisp/markdown-preview-mode/"
}
