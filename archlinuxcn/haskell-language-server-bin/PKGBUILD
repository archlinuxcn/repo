# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=0.7.0
pkgrel=1
pkgdesc="Integration point for ghcide and haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('8d0b079a416450bad83e497536625aed32a60fd7edfe5e2104809403d6b40d48'
            'd458558bcae7b9ffaae04a598c72f9ac1a50c9209cd3c4b3689bd89c9363f712'
            '028e502bc1e18a7dd630b12afc01b9c32154938315516eb2d9430e186a3ffbd1'
            '792151d9d1cecfc98774ed7c6cf9410cfbd7e6699e45e1f4c6f2f49db3f9775d'
            '7659d3d26a8979cb3ae99c5e7651a8034884f3c266dc089df8cd026128a8fe3a'
            '1b1a5c07da788f78df2a71186c4e082372e45c1653099c881406a2aa0bc87a18'
            '9b391e3ba67627e63079707ec05264acdd95394661095b29e4b59c05e9acf1f3'
            '4efe7b6c5505eb820052c7b0ddb5af7eadcad472c1ca84afcf04d6baff85dba6')
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
 
