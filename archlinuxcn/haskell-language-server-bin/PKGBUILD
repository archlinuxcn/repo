# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=0.7.1
pkgrel=1
pkgdesc="Integration point for ghcide and haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('ffa8b4acc79dc21fd4404e31666906d08f6349d3623496cc3580ba29d6235c86'
            '613312c4a34746f5cf3c12431a8b15118fbd6f921953cf07287b66906cdca96d'
            'b57c127e69657c1ecd79a5683cd1a70ba82400efb40839da89c58bfa8f40bec7'
            '5ce711ea097e0c8504c3e6ad708f832728bb1e5173981c97bcb77404746bacee'
            '7c7504ee287ee4dbfc9c9d032232df9a7dffdcee71de0fa2387de44d77bee8bc'
            'd0870eb03158de15ce76fb70c598b9971bf2c4447e8392c1ebb86dfc9bf479a4'
            '1460dbe9826642f72d39a11f90c0b714b67184a3d4a59d715ce30e565f787e0a'
            'a70c156c6be8b01448b6fc2f6b03859621b3fd40f630c5d7e1c4fb19f95ef785')
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
 
