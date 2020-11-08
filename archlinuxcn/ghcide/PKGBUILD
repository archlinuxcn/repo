# Maintainer: berberman <hatsue@typed.icu>
# Contributor: amesgen <amesgen AT amesgen DOT de>
# Contributor: Rodrigo Gryzinski <rogryza@gmail.com>

pkgname=ghcide
pkgver=0.5.0
pkgrel=1
pkgdesc="A library for building Haskell IDE tooling"
arch=('x86_64')
url="https://github.com/haskell/${pkgname}"
license=('Apache')
makedepends=('stack')
depends=('gmp' 'zlib')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('7e12cd80bcd15bf08c55ac994aa8d1f6ba1ec8f9f20f1740d3717250eec98d5e')

_ghc_versions=('8.8' '8.10' '8.10.1')

prepare() {
  cd "${pkgname}-${pkgver}" 
  rename k8 k8. stack8*.yaml
  rename 101 10.1 stack8.101.yaml
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
