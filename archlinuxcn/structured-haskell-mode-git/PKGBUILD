pkgname=structured-haskell-mode-git
pkgver=r444.7f9df73
pkgrel=3
pkgdesc="Structured editing minor mode for Haskell in Emacs"
url="https://hackage.haskell.org/package/structured-haskell-mode"
license=('BSD')
arch=('x86_64' 'i686' 'aarch64')
depends=('ghc-libs' 'haskell-src-exts' 'haskell-descriptive')
provides=('structured-haskell-mode')
conflicts=('structured-haskell-mode')
makedepends=('ghc' 'git' 'emacs')
source=("${pkgname}::git://github.com/projectional-haskell/structured-haskell-mode")
sha256sums=('SKIP')

pkgver() {
  cd "${srcdir}/${pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd ${pkgname}
    runghc Setup.hs configure -O --enable-shared --enable-executable-dynamic --disable-library-vanilla \
    --prefix=/usr --docdir="/usr/share/doc/${pkgname}" \
    --dynlibdir=/usr/lib --libsubdir=\$compiler/site-local/\$pkgid
    runghc Setup.hs build
    cd elisp
    make
}

package() {
    cd ${pkgname}
    runghc Setup.hs copy --destdir="${pkgdir}"
    mkdir -p ${pkgdir}/usr/share/licenses/${pkgname}
    mv "${pkgdir}/usr/share/doc/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}"
    mkdir -p ${pkgdir}/usr/share/emacs/site-lisp/structured-haskell-mode
    cp elisp/*.{el,elc} ${pkgdir}/usr/share/emacs/site-lisp/structured-haskell-mode
}
