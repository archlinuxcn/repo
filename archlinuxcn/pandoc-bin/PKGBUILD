pkgname=pandoc-bin
pkgver=3.8.2.1
pkgrel=1
pkgdesc="Conversion between documentation formats"
url="https://pandoc.org"
license=("GPL-2.0-or-later")
arch=('x86_64' 'aarch64')
conflicts=("pandoc-cli")
provides=("pandoc=$pkgver" "pandoc-cli=$pkgver")
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

sha256sums=('e3948e106026edbcef4e4d63f92554c814c779fa14696e635fb98e1279d4c175')
sha256sums_x86_64=('b362815e21d8ad3629c124aa92baf54558da086ad72374b4f6fdd97b9f3275b0')
sha256sums_aarch64=('852e898c2490fa840ae75a8b6af8a6c9d6d63b77ef170c32ec3a17958464d929')

package() {
  cd "${srcdir}/pandoc-${pkgver}"

  mkdir -p "${pkgdir}/usr/share/pandoc"
  cp -R bin share "${pkgdir}/usr"
  cp -R data citeproc "${pkgdir}/usr/share/pandoc/"
  cp COPYRIGHT MANUAL.txt "${pkgdir}/usr/share/pandoc/"
  bin/pandoc --bash-completion | \
    install -Dm644 /dev/stdin "$pkgdir"/usr/share/bash-completion/completions/pandoc
}

# vim: set ts=2 sw=2 et
