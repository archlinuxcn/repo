# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=0.5.1
pkgrel=1
pkgdesc="Integration point for ghcide and haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('4135735351676f6ac9203f444db337694e584fca32d786f756faa0849c2fc194'
            'cee03bc6864a153cbab00a43363f75680676f13525fa75c1ca31c61a8a6227dc'
            'f1fbeab482e69aa637f081920b2d277531bee191d4bd6b1cd1ad5546c7b771e8'
            '83c1ab2c9a9a1c8ea59f2318b0c12d4459836fcaa953d6bf938c0fce2998516d'
            'e99036ef2fc3fba9d484a729d958ccdf8d772e4a512bd2b2ba13065d52242b93'
            '758e798c57c2d5aac60641a103c4d8a76b486ba7eb746f2eef498ef0e11f5782'
            '58d7ee36809bf40183a69589c819aaa256a75d2e7fda4e3a0505e84fc7534274'
            '2092ff195093854ffe79c655ba8ccfd6ebc4782e3d3ad098bff5fc3fb286083c')
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
 
