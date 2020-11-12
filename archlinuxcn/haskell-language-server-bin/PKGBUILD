# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=0.6.0
pkgrel=1
pkgdesc="Integration point for ghcide and haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('e1023398039676a7cc1f59ae31b6d4d4744bd33c675f464d8c42b130319e4771'
            '92ea990266a96311a4675b6411f98b05f42eb49a4330e9a38f2485b1635e7ce3'
            '75781fe814f09fe1868ae670fff2f191ca8372f7b764237920cdefe22849568f'
            '07952450de682b99839f15f75a592fd8d754ca15022e1a1206de51e3f859878e'
            'b1302bb80ada393c107b2ae0f17ed396e4ecf6a251624245f17b1782bd22390b'
            '336868cb66db0c1f1af10d835a190ff951c5838bd90969b8703c83a33b20233a'
            '1aab106d6bb45d34d89a227911df8c95598ff214a9edda59155019fbb9672f01'
            'fb847d221a85e2c69bbed78fb2ee190c066d6b8e42017f1a9235989521b78a18')
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
 
