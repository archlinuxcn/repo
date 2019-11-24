pkgname=haskell-clay
_hkgname=clay
pkgver=0.13.2
pkgrel=2
pkgdesc="CSS preprocessor as embedded Haskell."
url="https://hackage.haskell.org/package/clay"
license=('BSD')
arch=('x86_64' 'i686' 'aarch64')
depends=('ghc-libs')
makedepends=('ghc')
source=(${pkgname}-${pkgver}.tar.gz::"https://hackage.haskell.org/packages/archive/${_hkgname}/${pkgver}/${_hkgname}-${pkgver}.tar.gz")
sha256sums=('d2f8832f9c64fd78313409574f237541bd91316d1f05f5642c8531984ac0bccb')

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
    mkdir -p ${pkgdir}/usr/share/licenses/haskell-clay
    mv "${pkgdir}/usr/share/doc/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/haskell-clay"
    install -D -m744 register.sh   "${pkgdir}/usr/share/haskell/register/${pkgname}.sh"
    install -D -m744 unregister.sh "${pkgdir}/usr/share/haskell/unregister/${pkgname}.sh"
}
