# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=0.9.0
pkgrel=1
pkgdesc="Integration point for ghcide and haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('7e38c60a975f7970bd825f7320d780eeb068ade0c9426380c6e6ddcde999b287'
            'e0bf91f2b1c55dedcb76648eede05556097204dbc17e72b7756c098409dfb222'
            '905a1edb2345465c12878527f9f35ffd0d8cff1265eb3c914969015d6fdb8b8c'
            'd622d8ce07406254ca470733cc9a270acb2c965362b8eb33152aa4b9adff4330'
            '7d2dd3ab23cd2c293354fa4fb921019c3998f64a69972d577562668488007fd7'
            '892f596510aa38de44140f123f4cd85e0a3680ba5b49d807a7967692e06a5810'
            'ad2c21f19b0a32f882e8446d53186d7357794ca1a71708b63a3a50ad219f703b'
            'e9db4226fdd8b2963e55bd0965666d3272b10bbc73ce4f54a4d571abdfb73791'
            'a87e588bc9b1dbc039e38c00b9b9f23ecad6f0e99ae30a01642e2125de371fb4')
_prefix="${pkgname%-bin}-Linux"
_ghc_versions=('8.6.4' '8.6.5' '8.8.2' '8.8.3' '8.8.4' '8.10.1' '8.10.2' '8.10.3')

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
 
