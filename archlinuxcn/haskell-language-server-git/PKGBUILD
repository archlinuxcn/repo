# Maintainer: Poscat <poscat@mail.poscat.moe>

pkgname=haskell-language-server-git
pkgver=r63.d1a232f
pkgrel=1
pkgdesc="Integration point for ghcide and haskell-ide-engine."
arch=('x86_64' 'aarch64')
url="https://github.com/haskell/haskell-language-server"
license=('Apache')
makedepends=('stack' 'git')
source=(${pkgname}::git+https://github.com/haskell/haskell-language-server.git)
md5sums=('SKIP')

pkgver() {
  cd "${srcdir}/${pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "${srcdir}/${pkgname}"
  stack build
}

package() {
  cd "${srcdir}/${pkgname}"
  install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  stack --local-bin-path "${pkgdir}/usr/bin/" install
}
