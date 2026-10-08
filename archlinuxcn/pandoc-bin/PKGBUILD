pkgname=pandoc-bin
pkgver=3.12.1
pkgrel=1
pkgdesc="Conversion between documentation formats"
url="https://pandoc.org"
license=("GPL-2.0-or-later")
arch=('x86_64' 'aarch64')
conflicts=("pandoc-cli")
provides=("pandoc=$pkgver" "pandoc-cli=$pkgver")
options=(!debug !strip)
optdepends=(
  'pandoc-crossref: for numbering figures, equations, tables and cross-references to them with pandoc-crossref filter'
  'texlive-context: for pdf output using context engine'
  'groff: for pdf output using pdfroff engine'
  'python-weasyprint: for pdf output using weasyprint engine'
  'typst: for pdf output using typst engine'
  'tectonic: for pdf output using tectonic engine'
  'texlive-fontsrecommended: for pdf output using latex or xelatex engines'
  'texlive-latex: for pdf output using pdflatex engine'
  'texlive-xetex: for pdf output using xelatex engine'
)

# The binary release doesn't have the datafiles, so we need to yoink those out of the source tarball, too.
source=("$pkgname-$pkgver.tar.gz::https://github.com/jgm/pandoc/archive/${pkgver}.tar.gz")
source_x86_64=("https://github.com/jgm/pandoc/releases/download/${pkgver}/pandoc-${pkgver}-linux-amd64.tar.gz")
source_aarch64=("https://github.com/jgm/pandoc/releases/download/${pkgver}/pandoc-${pkgver}-linux-arm64.tar.gz")

sha256sums=('cf9b3725b90e471aa70c99ac3b351adcb6e40cd904d36fcbb0f70d712e135686')
sha256sums_x86_64=('d0c90410e90204c9ca83b8539fac5c7aed01fd537207e4585849f8abc5df20b8')
sha256sums_aarch64=('445d96fd08801fe636cab1158b4f017ee320ac3b7446328b4fe2f902117b19b9')

package() {
  cd "${srcdir}/pandoc-${pkgver}"

  mkdir -p "${pkgdir}/usr/share/pandoc"
  cp -R bin share "${pkgdir}/usr"
  cp -R data citeproc "${pkgdir}/usr/share/pandoc/"
  cp COPYRIGHT MANUAL.txt "${pkgdir}/usr/share/pandoc/"

  bin/pandoc --completion=bash | \
    install -Dm644 /dev/stdin "$pkgdir"/usr/share/bash-completion/completions/pandoc
  bin/pandoc --completion=zsh | \
    install -Dm644 /dev/stdin "$pkgdir"/usr/share/zsh/site-functions/_pandoc
  bin/pandoc --completion=fish | \
    install -Dm644 /dev/stdin "$pkgdir"/usr/share/fish/vendor_completions.d/pandoc.fish
}

# vim: set ts=2 sw=2 et
