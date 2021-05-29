pkgname=pandoc-bin
pkgver=2.14
pkgrel=1
pkgdesc="Pandoc - executable only, without 750MB Haskell depends/makedepends"
url="http://pandoc.org"
license=("GPL")
arch=('x86_64')
conflicts=("pandoc")
provides=("pandoc")
replaces=('pandoc-static' 'pandoc-lite')
optdepends=(
  'texlive-core: for pdf output'
)

source=(
  "$pkgname-bin-$pkgver.tar.gz::https://github.com/jgm/pandoc/releases/download/${pkgver}/pandoc-${pkgver}-linux-amd64.tar.gz"

  # The binary release doesn't have the datafiles, so we need to yoink those out of the source tarball, too.
  "$pkgname-source-$pkgver.tar.gz::https://github.com/jgm/pandoc/archive/${pkgver}.tar.gz"
)
sha256sums=('e24cca7d241d907d690428a296861cbcbdaf4686ef887ac65581a930b2e6038c'
            '696398fafb2be8a0437749cb35450b6e0fcf79849f832573a13e23b636564653')

package() {
  cd "${srcdir}/pandoc-${pkgver}"

  # To avoid having to download over a gigabyte of haskell makedepends (400-ish for ghc, plus 750 in libs), we
  # just yoink the binary from static compiled binary distributed by pandoc:
  mkdir -p "${pkgdir}/usr/share/pandoc"
  cp -R bin share "${pkgdir}/usr"

  # We're still missing all the datafiles and so on. We get those from the source tarball...
  cp -R data "${pkgdir}/usr/share/pandoc/"
  cp COPYRIGHT MANUAL.txt "${pkgdir}/usr/share/pandoc/"
}
