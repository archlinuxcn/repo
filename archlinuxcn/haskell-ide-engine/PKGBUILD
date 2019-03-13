# Maintainer: Philippe Hürlimann <p@hurlimann.org>
pkgname=haskell-ide-engine
pkgver=0.6.0.0
pkgrel=1
pkgdesc="The engine for haskell ide-integration. Not an IDE"
arch=('x86_64')
url="https://github.com/haskell/haskell-ide-engine"
license=('custom:BSD3')
makedepends=('git' 'stack' 'cabal-install' 'happy')
source=("${pkgname}-${pkgver}::git://github.com/haskell/${pkgname}.git#tag=${pkgver}")
noextract=()
md5sums=('SKIP')

# supported are '8.2.1' '8.2.2' '8.4.2' '8.4.3' '8.4.4' '8.6.1' '8.6.2' '8.6.3'
# activated by default are the ones also used in a stackage snapshot
# removing versions you do not use will greatly reduce the compilation time of this package
_enabled_ghc_versions=('8.2.2' '8.4.3' '8.4.4' '8.6.3')

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    git submodule update --init
}

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    for ver in "${_enabled_ghc_versions[@]}"; do
        stack --stack-yaml=stack-${ver}.yaml build
    done
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    for ver in "${_enabled_ghc_versions[@]}"; do
        stack --stack-yaml=stack-${ver}.yaml --local-bin-path "${pkgdir}/usr/bin/" install \
        && mv "${pkgdir}/usr/bin/hie" "${pkgdir}/usr/bin/hie-${ver}"
    done
}
