# Maintainer: Meow

pkgname=rstudio-desktop-bin
pkgver=2023.12.1.402
_pkgver=2023.12.1-402
pkgrel=1
pkgdesc="An integrated development environment (IDE) for R (binary from RStudio official repository)"
arch=('x86_64')
license=('GPL')
url="http://www.rstudio.org/"
depends=('r>=3.3.0' 'hicolor-icon-theme' 'shared-mime-info' 'openssl' 'openssl-1.1' 'nss' 'at-spi2-core' 'gtk3' 'alsa-lib' 'libedit' 'postgresql-libs' 'sqlite')
makedepends=()
optdepends=('clang: C/C++ and Rcpp support')
conflicts=('rstudio-desktop' 'rstudio-desktop-git' 'rstudio-desktop-preview-bin')
provides=("rstudio-desktop=${pkgver}")
options=(!strip)

sha256sums_x86_64=(
81f221be29eb39efe65be48490c3cd090ddaf8991ea7a089baa0cdd326109e02 
)

source_x86_64=("https://download1.rstudio.org/electron/focal/amd64/rstudio-${_pkgver}-amd64.deb")

install="$pkgname".install

package() {

  shopt -s extglob

  msg "Converting debian package..."

  cd "$srcdir"
  tar Jxpf data.tar.xz -C "$pkgdir"

}
# vim:ft=sh tabstop=2 expandtab
