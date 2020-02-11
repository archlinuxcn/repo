# Maintainer: herzrasen <dennis.mellert@gmail.com>
pkgname=pkghist
pkgver=0.6.0
pkgrel=1
pkgdesc="Query your pacman logs"
arch=('x86_64')
url="https://github.com/herzrasen/pkghist"
license=('MIT')
makedepends=(
  'git'
  'rust'
)
provides=('pkghist')
conflicts=('pkghist-bin')

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/herzrasen/pkghist/archive/v${pkgver}.tar.gz")
sha1sums=('d264bfd6f7aa491ed32392a73a5ca972db560dc4')

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

