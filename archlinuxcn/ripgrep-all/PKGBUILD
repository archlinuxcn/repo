# Maintainer: phiresky <phireskyde+aur@gmail.com>
# Maintainer: Julien Nicoulaud <julien DOT nicoulaud AT gmail DOT com>

pkgname=ripgrep-all
pkgver=0.9.2
pkgrel=2
pkgdesc="rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc."
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
url="https://github.com/phiresky/ripgrep-all"
license=('AGPL3')
depends=(ripgrep ffmpeg pandoc poppler tesseract imagemagick)
makedepends=('rust' 'cargo')
conflicts=("${pkgname}-git" "${pkgname}-bin" "rga" "rga-git" "rga-bin")
source=("https://github.com/phiresky/ripgrep-all/archive/${pkgver}.tar.gz")
sha512sums=('ea91feae191b0dc6654572c3c7ace08ea452d3e838fdb5c3f6691a32d510f3340aa64171caf4f67db867e027317e04ffccc1aa6edc95c0ec8942d6e4d8ea0208')

build() {
  cd "${srcdir}/ripgrep-all-${pkgver}"
  cargo build --release --locked
}

check() {
  cd "${srcdir}/ripgrep-all-${pkgver}"
  cargo test --release --locked
}

package() {
  cd "${srcdir}/ripgrep-all-${pkgver}"
  install -Dm 755 "target/release/rga" "${pkgdir}/usr/bin/rga"
  install -Dm 755 "target/release/rga-preproc" "${pkgdir}/usr/bin/rga-preproc"
}
