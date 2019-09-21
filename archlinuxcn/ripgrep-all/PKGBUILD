# Maintainer: phiresky <phireskyde+aur@gmail.com>
# Maintainer: Julien Nicoulaud <julien DOT nicoulaud AT gmail DOT com>

pkgname=ripgrep-all
pkgver=0.9.3
pkgrel=1
pkgdesc="rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc."
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
url="https://github.com/phiresky/ripgrep-all"
license=('AGPL3')
depends=(ripgrep ffmpeg pandoc poppler tesseract imagemagick)
makedepends=('rust' 'cargo')
conflicts=("${pkgname}-git" "${pkgname}-bin" "rga" "rga-git" "rga-bin")
source=("https://github.com/phiresky/ripgrep-all/archive/${pkgver}.tar.gz")
sha512sums=('fc898130e9c5c3666e14bb7f7f1cc5c069a614eea2aa58e84e2267ea1cfcbab8a9272b56f997b7418088950fd5f119c9af050677d28c5a2287b7671dee0d629e')

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

