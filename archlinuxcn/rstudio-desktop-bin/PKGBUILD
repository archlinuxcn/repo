# Maintainer: Meow

pkgname=rstudio-desktop-bin
pkgver=2022.12.0.353
_pkgver=2022.12.0-353
pkgrel=1
pkgdesc="An integrated development environment (IDE) for R (binary from RStudio official repository)"
arch=('x86_64')
license=('GPL')
url="http://www.rstudio.org/"
depends=('r>=3.3.0' 'hicolor-icon-theme' 'shared-mime-info' 'openssl'
  'libxkbcommon-x11' 'libedit' 'postgresql-libs' 'sqlite')
makedepends=()
optdepends=('clang: C/C++ and Rcpp support')
conflicts=('rstudio-desktop' 'rstudio-desktop-git' 'rstudio-desktop-preview-bin')
provides=("rstudio-desktop=${pkgver}")
options=(!strip)

sha256sums_x86_64=(
23cae58f8ed1a7d7b96b266287a2fde67871b112339bbb95a203c6e672920083
)

source_x86_64=("https://download1.rstudio.org/electron/bionic/amd64/rstudio-${_pkgver}-amd64.deb")

install="$pkgname".install

package() {

  shopt -s extglob

  msg "Converting debian package..."

  cd "$srcdir"
  tar Jxpf data.tar.xz -C "$pkgdir"

}
# vim:ft=sh tabstop=2 expandtab
