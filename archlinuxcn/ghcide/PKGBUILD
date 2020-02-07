# Maintainer: amesgen <amesgen AT amesgen DOT de>
# Contributor: Rodrigo Gryzinski <rogryza@gmail.com>

pkgname=ghcide
pkgver=0.1.0
pkgrel=1
pkgdesc="A library for building Haskell IDE tooling"
arch=('x86_64')
url="https://github.com/digital-asset/${pkgname}"
license=('Apache')
depends=('gmp' 'zlib')
makedepends=('stack')
source=("${pkgname}-${pkgver}::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('f161e29b9f22b4f47b6001d523e62538ae70c2ed540f131948be0ce96fac4371')

build() {
  cd "${pkgname}-${pkgver}"
  stack build
}

package() {
  cd "${pkgname}-${pkgver}"
  stack install ghcide:exe:ghcide --local-bin-path "${pkgdir}/usr/bin"
  install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
