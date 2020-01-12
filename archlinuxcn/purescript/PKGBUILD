pkgname=purescript
pkgver=0.13.5
pkgrel=2
pkgdesc="A small strongly, statically typed programming language with expressive types, inspired by Haskell and compiling to JavaScript."
arch=('x86_64')
url="https://hackage.haskell.org/package/purescript"
license=('custom:BSD3')
makedepends=('stack')
source=(${pkgname}-${pkgver}.tar.gz::"https://hackage.haskell.org/package/${pkgname}-${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('44260d0cf86d35eb95e2fc348c986508f9b082f708ab53a3985170e518fd985e')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  stack build
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  stack --local-bin-path "${pkgdir}/usr/bin/" install
}
