# Maintainer: berberman <hatsue@typed.icu>

pkgname=haskell-language-server-bin
pkgver=1.2.0
pkgrel=1
pkgdesc="Successor of ghcide & haskell-ide-engine. One IDE to rule them all."
arch=('x86_64')
url="https://github.com/haskell/${pkgname%-bin}"
license=('Apache')
depends=()
provides=('haskell-language-server')
conflicts=('haskell-language-server' 'haskell-language-server-git')
source=()
sha256sums=('a9d7ebf8c175353931f8fde79f1298f9012341814231059a8b0fee4a68084c5a'
            '7e2d52983d6e2f365ba4706fec16689f58d86802afb580c0a0d124faea156fe3'
            'c67fa2e8f40d47d071e6eafc30f6b616052eb65617f477b0d2938162b984e71a'
            '1c2ac87ad1ecda53561ae07548897bb217cbd16bf06e2247a5b344edefdaa043'
            'a2917fd83cb78f516d6077331b2e2738ce8b764757f853fcc37da217db8296ce'
            'c9146e5abfc7a8a1aba05feae2b4ef15432ef0b085ae82b2186d0b2ce2b1f8b9'
            'd48c64314ee7168e60ad326db12e1050fb975f2d1f7177cba862d25919b9a3dc'
            '1ef7cba3d5f02765329bfa14df50b41085946c4c61dbb1d1f350c899f5bd7073'
            'd5875ee656c272fa4d0d80da9a8d3c9ca36b4d1816892d075f091ce477ae1b0d'
            'e19a3830268a7b34617bc9b935ebf8e2f50fb6628ee0f8317b83bafdb37b29ec')
_prefix="${pkgname%-bin}-Linux"
_ghc_versions=('8.6.4' '8.6.5' '8.8.2' '8.8.3' '8.8.4' '8.10.2' '8.10.3' '8.10.4' '8.10.5')

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
 
