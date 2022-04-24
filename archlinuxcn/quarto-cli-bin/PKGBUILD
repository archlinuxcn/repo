# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=quarto-cli-bin
pkgver=0.9.305
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

sha256sums=('224ecdd6c2be36cb2cf2f5aa1637b419379376fbc1db766467098ece4d05fe42')

