# Maintainer: berberman <hatsue@typed.icu>
# Contributor: amesgen <amesgen AT amesgen DOT de>
# Contributor: Rodrigo Gryzinski <rogryza@gmail.com>

pkgname=ghcide
pkgver=0.6.0
pkgrel=1
pkgdesc="A library for building Haskell IDE's on top of the GHC API."
arch=('x86_64')
url="https://github.com/haskell/${pkgname}"
license=('Apache')
makedepends=('stack')
depends=('gmp' 'zlib')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('6a26ff4c5cd6ad876600d2c27cc7b8be86217c0cb4a37a2739b6da850702f9de')


build() {
  cd "${pkgname}-${pkgver}" 
  stack build
}

package() {
  cd "${pkgname}-${pkgver}"
  stack --local-bin-path "${pkgdir}/usr/bin/" install ghcide:exe:ghcide
  install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
