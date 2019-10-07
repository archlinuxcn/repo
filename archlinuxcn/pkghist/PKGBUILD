# Maintainer: herzrasen <dennis.mellert@gmail.com>
pkgname=pkghist
pkgver=0.4.0
pkgrel=1
pkgdesc="Query your pacman logs"
arch=('x86_64')
url="https://github.com/herzrasen/pkghist"
license=('MIT')
makedepends=(
  'git'
  'rust'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/herzrasen/pkghist/archive/v${pkgver}.tar.gz")
sha1sums=('d436262d971c7b5b2967db2b81fa5aff7585ed66')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  cargo build --release
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -Dm755 target/release/${pkgname} "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 completions/_${pkgname} "${pkgdir}/usr/share/zsh/site-functions/_${pkgname}"
  install -Dm644 completions/${pkgname}.bash "${pkgdir}/usr/share/bash-completion/completions/${pkgname}"
  install -Dm644 completions/${pkgname}.fish "${pkgdir}/usr/share/fish/vendor_completions.d/${pkgname}.fish"
}

