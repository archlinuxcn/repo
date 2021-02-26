# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=1.0.0
pkgrel=1
pkgdesc="Integration point for ghcide and haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('95c0233437a185258e7c04750535dd6c3ffba04c7bce20805d03b3e7907b4aa8'
            'd034115897475ab090a9093e887c0ed826804bfefd34b1289598637b9ab411f2'
            'd2c0e2435f9c07b5eac9c88a683ba489fa57d0b60d85b9c0681d2cb0d9df7b44'
            'a652eb1a197ad22a9543e40498f74727d2148c81404e18fc01dd17ed06ebeca8'
            '11f6aa40ba10192ee5fc0c1387804fe62b220e501ca7bb979a146b6ad7ff5d07'
            '1a55e43c49a158bd8d6ac440009fc28d9e37f492ab21cbcb63b29f3027b999a3'
            '20324e484c253922e7bd910aee6351b86fb11e8b4d7813f65c086413d05f1605'
            '0f0bd997dda3e6b13d1ff0a44da4d966cf3f3a9ce794576665a5d28facbfa244'
            '454a15e3b3c26f7dc51f2e8b7f8977947b1e42aafe0d657909c618dceebda2f3')
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
 
