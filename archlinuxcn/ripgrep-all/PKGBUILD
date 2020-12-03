# Maintainer: Chris Lane <aur at chrislane dot com>
# Co-maintainer: phiresky <phireskyde+aur@gmail.com>
# Contributor: Julien Nicoulaud <julien DOT nicoulaud AT gmail DOT com>

pkgname=ripgrep-all
pkgver=0.9.6
pkgrel=1
pkgdesc="rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc."
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
url="https://github.com/phiresky/ripgrep-all"
license=('AGPL3')
depends=('ripgrep')
makedepends=('rust' 'cargo')
optdepends=(
    'ffmpeg: for the ffmpeg adapter'
    'graphicsmagick: for the pdfpages adapter'
    'pandoc: for the pandoc adapter'
    'poppler: for the poppler adapter'
    'tesseract: for the tesseract adapter')
conflicts=("${pkgname}-git" "${pkgname}-bin")
source=("${pkgname}-${pkgver}"::"${url}/archive/v${pkgver}.tar.gz")
sha512sums=('45fc258e8ef44ddd7ce6b4c7dc5c60a439c8e5aafd253ea41621afcc50aaecd300d8792c4cbdc9247a5656d9c3db0a33053de96ca41f0831421ea8ce382ca7de')

build() {
  cd "${srcdir}/ripgrep-all-${pkgver}"
  cargo build --release --locked --target-dir=$PWD/target
}

check() {
  cd "${srcdir}/ripgrep-all-${pkgver}"
  cargo test --release --locked --target-dir=$PWD/target
}

package() {
  cd "${srcdir}/ripgrep-all-${pkgver}"
  install -Dm 755 "target/release/rga" "${pkgdir}/usr/bin/rga"
  install -Dm 755 "target/release/rga-preproc" "${pkgdir}/usr/bin/rga-preproc"
}

# vim:set ts=2 sw=2 et:
