# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=0.5.0
pkgrel=2
pkgdesc="Integration point for ghcide and haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('b0e3e03554f6ef517f13b78477c84fd1952ac9ac94d2608cc1238321f0a544d8'
            '4b59dbb5f82b6ad4ac7243fe1b68bb608b9559e9862f1950a6890653ef69a92d'
            'e681c361f7d2d3391dd7133f8d47dd1695de1a72771875b2ccdd2d0b56767af0'
            '31bc5bd2343fa47d49215097ad288e425b761e202eecae72ac9b6427bcda0e03'
            '5691f3670a3696eea596cc07fcd12a43206b04a0495c229b5b4cc3dde9c6eb98'
            'b1f81613f9a1aa62376d1316a61f3d46fa023a14b2536ed9d1f46036ad73c820'
            '92d81ca53ea6a1fdb6915809d95b936bef4bacbb062529907931fb21e7315425'
            '4afce25f30391bd5fcadae06f7ff0bdede8a8a576cf59d44d68f8aace8b03fd4')
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
 
