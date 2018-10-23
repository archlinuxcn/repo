# Maintainer: Maxim Andersson <thesilentboatman@gmail.com>

pkgname=tealdeer
pkgver=1.1.0
pkgrel=1
pkgdesc="An implementation of tldr in Rust"
arch=('i686' 'x86_64')
url="https://github.com/dbrgn/tealdeer"
license=('MIT' 'Apache')
makedepends=('rust' 'cargo')
provides=('tldr')
conflicts=('tldr' 'nodejs-tldr' 'nodejs-tldr-git' 'tldr-cpp-client' 'tldr-git' 'tldr-python-client')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dbrgn/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('647990936af527e9738e8befb432fdf8dd40e7b2ab0066afc652330fddd3dd0e')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  cargo build --release
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  install -D target/release/tldr -t "${pkgdir}/usr/bin"
  install -Dm644 bash_tealdeer "${pkgdir}/usr/share/bash-completion/completions/tldr"
}

# vim:set ts=2 sw=2 et:
