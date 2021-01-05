# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=0.8.0
pkgrel=1
pkgdesc="Integration point for ghcide and haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('0c8a02598f596defd3abf963c1505a2af16d2363c46dd296fda6dd8682e94490'
            'bdaa6687ef5e44e037ccab91b5e7ab205b11f7cf1aed03dda8f38af0d8f24718'
            'ddb51ccf1de4b30a01d477267a0f8773179d11d913a6cd57cf5b73103ce9c5b7'
            '4930a109f68f8e92ed0168488fa791ea4484a831d572e22e4d842c4d40b71f46'
            'b688eec0952a80fc71c3ecb9778ed376bc1a7e14f0909382996fe2dcd89c3187'
            '569ebebdc6cb4b30944b7f14fbcb198a3f3019b8a4267368fa441e133497e1b6'
            'ad4d0c3638be51174c399d263e5c9f7ce7c9a1747a5825568da646a99ebc631d'
            'eeaa8cea780923da977ef00a08ae007a8fdb75c957b500209bc4d0fff10e72d4')
_prefix="${pkgname%-bin}-Linux"
_ghc_versions=('8.6.4' '8.6.5' '8.8.2' '8.8.3' '8.8.4' '8.10.1' '8.10.2')

for ver in ${_ghc_versions[@]}; do
  source+=("${_prefix}-${ver}-${pkgver}.gz::${url}/releases/download/${pkgver}/${_prefix}-${ver}.gz")
done

# Wrapper is independent from ghc version
source+=("${pkgname%-bin}-wrapper-Linux-${pkgver}.gz::${url}/releases/download/${pkgver}/${pkgname%-bin}-wrapper-Linux.gz")

package() {
  cd "${srcdir}"
  for ver in ${_ghc_versions[@]}; do
    install -Dm755 "${_prefix}-${ver}-${pkgver}" "${pkgdir}/usr/bin/"${pkgname%-bin}-${ver}""
  done
  install -Dm755 "${pkgname%-bin}-wrapper-Linux-${pkgver}" "${pkgdir}/usr/bin/${pkgname%-bin}-wrapper"
}
 
