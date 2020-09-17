# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=0.4.0
pkgrel=2
pkgdesc="Integration point for ghcide and haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server-git')
source=()
sha256sums=(
  '630c3bc84a329eda6fff2dd1a0c21c3a5c325afee94b561150fe559042aa1f3a'
  '4a011e622b9435140cb5e5be9a3f2127d934e10c01ff7b71f935733fbce39434'
  'c22baf8a7ac47cf112aa1cd94d2deed4f4d33bc6821ba5b5e6eecb9bfe7ec8e0'
  '017578b3fce60dbd1e6afe99e2c5556d2760d52a0bf39dbdb347d035475327c6'
  '87ecf8ecc7e116aa0b4562462ec361a6b68f8f17b937f4754b01b24c19a2c135'
  'f544db5d83ca8c91d4ef6f9d024a087570e781c552816442b8b0ff2a00eeba51'
  'd37b953824ed79c1d591f3a1df6c7416ee29093be8010e3301da66a4d1d1bf91'
  '551b2147cc8f46d7a6a537daba3aa81095d1b81f66e601cb3d8e46c44cabd008')
_prefix="${pkgname%-bin}-Linux"
_ghc_versions=('8.6.4' '8.6.5' '8.8.2' '8.8.3' '8.8.4' '8.10.1' '8.10.2')

for ver in ${_ghc_versions[@]}; do
  source+=("${_prefix}-${ver}.gz::${url}/releases/download/${pkgver}/${_prefix}-${ver}.gz")
done

# Wrapper is independent from ghc version
source+=("${pkgname%-bin}-wrapper-Linux.gz::${url}/releases/download/${pkgver}/${pkgname%-bin}-wrapper-Linux.gz")

package() {
  cd "${srcdir}"
  for ver in ${_ghc_versions[@]}; do
    install -Dm755 "${_prefix}-${ver}" "${pkgdir}/usr/bin/"${pkgname%-bin}-${ver}""
  done
  install -Dm755 "${pkgname%-bin}-wrapper-Linux" "${pkgdir}/usr/bin/${pkgname%-bin}-wrapper"
}
 
