pkgname=haskell-clay
_hkgname=clay
pkgver=0.13.3
pkgrel=1
pkgdesc="CSS preprocessor as embedded Haskell."
url="https://hackage.haskell.org/package/clay"
license=('BSD')
arch=('x86_64' 'i686' 'aarch64')
depends=('ghc-libs')
makedepends=('ghc')
source=(${pkgname}-${pkgver}.tar.gz::"https://hackage.haskell.org/packages/archive/${_hkgname}/${pkgver}/${_hkgname}-${pkgver}.tar.gz")
sha256sums=('5db3c4c4a40f377b808a1569c5f8aeeea3ecdd2191f4fbbcd0f22b23fdd254a4')

build() {
    cd ${_hkgname}-${pkgver}

    runghc Setup.lhs configure -O --enable-shared --enable-executable-dynamic --disable-library-vanilla \
    --prefix=/usr --docdir="/usr/share/doc/${pkgname}" \
    --dynlibdir=/usr/lib --libsubdir=\$compiler/site-local/\$pkgid
    runghc Setup.lhs build
    runhaskell Setup register --gen-script
    runhaskell Setup unregister --gen-script
    sed -i -r -e "s|ghc-pkg.*update[^ ]* |&'--force' |" register.sh
    sed -i -r -e "s|ghc-pkg.*unregister[^ ]* |&'--force' |" unregister.sh
}

package() {
    cd ${_hkgname}-${pkgver}
    runghc Setup.lhs copy --destdir="${pkgdir}"
    mkdir -p ${pkgdir}/usr/share/licenses/${pkgname}
    mv "${pkgdir}/usr/share/doc/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m744 register.sh   "${pkgdir}/usr/share/haskell/register/${pkgname}.sh"
    install -D -m744 unregister.sh "${pkgdir}/usr/share/haskell/unregister/${pkgname}.sh"
}
