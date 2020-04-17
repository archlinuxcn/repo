# Maintainer: phiresky <phireskyde+aur@gmail.com>
# Maintainer: Julien Nicoulaud <julien DOT nicoulaud AT gmail DOT com>

pkgname=ripgrep-all
pkgver=0.9.5
pkgrel=1
pkgdesc="rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc."
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
url="https://github.com/phiresky/ripgrep-all"
license=('AGPL3')
depends=(ripgrep ffmpeg pandoc poppler tesseract imagemagick)
makedepends=('rust' 'cargo')
conflicts=("${pkgname}-git" "${pkgname}-bin" "rga" "rga-git" "rga-bin")
source=("https://github.com/phiresky/ripgrep-all/archive/v${pkgver}.tar.gz")
sha512sums=('b881503d412b882f03036e748e50fa80ce463cb2d0f670ee76a21853dc3ccf307d680ab0fb8d0a4302f3b6c40ca64d62b2f6fca84fb6323ee1af50d4f6eeae47')

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

