# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=1.1.0
pkgrel=1
pkgdesc="Successor of ghcide & haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('93976e622ec27f96c1ee56293f7fba3e1dc86af4dd762c5c54582bc5b5bb72b6'
            'ef39563144ced4ba26a53d02ac1ba9d4f26ff932c1305c5b75cec1aec419f5be'
            '0dea95c02cff74b827bb5d126553b3d22a7ad066c17870771bfc3dc7df02baef'
            '23d1a9e28280b5153e92cb1f6cc0f0be7b83ca94c7a8815bb4d28aae81d86536'
            '6f6736efee87f1bb28a3d87433a44e2076c183c8efac67b674e6dcf18226a445'
            '84db2ec0827b0bb528c967f5c5715d43aeeba2704e42170169e2959578ce515c'
            'c7b4d0fcec3ee6f697a578b791e6c6caf5e6b816dd310e65ee9d8acbb46af9a9'
            'c47ddfd35ef8becebe7f5c0f2c04fa597c76753999c26d91dad8918f342d16c8'
            'bb01c0e9d0a10e007c05ed7f621ee0d1f30cab9a9b8b72fd9a2e3d63b2162995')
_prefix="${pkgname%-bin}-Linux"
_ghc_versions=('8.6.4' '8.6.5' '8.8.2' '8.8.3' '8.8.4' '8.10.2' '8.10.3' '8.10.4')

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
 
