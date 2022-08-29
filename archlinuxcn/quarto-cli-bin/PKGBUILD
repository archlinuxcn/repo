# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=quarto-cli-bin
pkgver=1.1.163
pkgrel=1
pkgdesc="An open-source scientific and technical publishing system built on Pandoc  (binary from official repo)"
arch=('x86_64')
license=('GPL')
url="http://quarto.org/"
depends=('bash')
makedepends=()
provides=("quarto")
options=(!strip)
source=(https://github.com/quarto-dev/quarto-cli/releases/download/v${pkgver}/quarto-${pkgver}-linux-amd64.deb)

package() {
    tar xf data.tar.gz -C "${pkgdir}"

    install -d -m755 "${pkgdir}/usr/bin"
    ln -s /opt/quarto/bin/quarto "${pkgdir}/usr/bin"
}

sha256sums=('e4fc7f25dfbfec1e00f7c4f166c6ea51062b9a74667c9eb079c4ec8e5f1eb8cc')

