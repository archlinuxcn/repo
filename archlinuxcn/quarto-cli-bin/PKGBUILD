# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=quarto-cli-bin
pkgver=0.9.245
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

sha256sums=('7e6e3bca5b7f3f38bc0b5eaf1d165f2802e0e7bc2a33788ed2d7f4ce12f90882')

