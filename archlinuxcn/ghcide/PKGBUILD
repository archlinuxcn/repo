# Maintainer: berberman <hatsue@typed.icu>
# Contributor: amesgen <amesgen AT amesgen DOT de>
# Contributor: Rodrigo Gryzinski <rogryza@gmail.com>

pkgname=ghcide
pkgver=0.2.0
pkgrel=1
pkgdesc="A library for building Haskell IDE tooling"
arch=('x86_64')
url="https://github.com/digital-asset/${pkgname}"
license=('Apache')
makedepends=('stack')
depends=('gmp' 'zlib')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('9a0b8c6158dcfe5654d948db1848235b86b7b958b66cb983308416c717d97cba')

_ghc_versions=('8.4' '8.8' '8.10')

prepare() {
  cd "${pkgname}-${pkgver}" 
  rename k8 k8. stack8*.yaml
}

build() {
  cd "${pkgname}-${pkgver}" 
  stack --stack-yaml=stack.yaml build
  for ver in ${_ghc_versions[@]}; do
    stack --stack-yaml=stack${ver}.yaml build
  done
}

package() {
  cd "${pkgname}-${pkgver}"
  for ver in ${_ghc_versions[@]}; do
    stack --stack-yaml=stack${ver}.yaml --local-bin-path "${pkgdir}/usr/bin/" install ghcide:exe:ghcide
    mv "${pkgdir}/usr/bin/ghcide" "${pkgdir}/usr/bin/ghcide-${ver}"
  done
  stack --stack-yaml=stack.yaml --local-bin-path "${pkgdir}/usr/bin/" install ghcide:exe:ghcide
  install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
