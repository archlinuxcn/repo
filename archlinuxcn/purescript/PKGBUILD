pkgname=purescript
pkgver=0.13.8
pkgrel=1
pkgdesc="A small strongly, statically typed programming language with expressive types, inspired by Haskell and compiling to JavaScript."
arch=('x86_64')
url="https://hackage.haskell.org/package/purescript"
license=('custom:BSD3')
makedepends=('stack')
source=(${pkgname}-${pkgver}.tar.gz::"https://hackage.haskell.org/package/${pkgname}-${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('701fac49de867ec01252b067185e8bbd1b72e4b96997044bac3cca91e3f8096a')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  stack build
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  stack --local-bin-path "${pkgdir}/usr/bin/" install
}
