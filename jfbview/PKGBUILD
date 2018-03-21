# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Chuan Ji <ji@chu4n.com>

pkgname=jfbview
pkgver=0.5.5
pkgrel=1
pkgdesc="a PDF and image viewer for the Linux framebuffer"
arch=('i686' 'x86_64')
url="http://seasonofcode.com/pages/jfbview.html"
license=('Apache')
depends=('libmupdf' 'imlib2' 'openjpeg2' 'jbig2dec')
conflicts=('jfbpdf')
replaces=('jfbpdf')
source=("https://github.com/jichu4n/JFBView/archive/${pkgver}.tar.gz")
sha512sums=('ee42bacac85daa532e694c9da5c4a900b6d06f11090a3210f8f6da841569d57ecbbbb65dd26a11edcb0598096973cfd67c21f9ad344d15f42733deae53836183')

_pkgname='JFBView'
_binname='jfbview'

build(){
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make
}

package(){
  cd "${srcdir}/${_pkgname}-${pkgver}"
  install -Dm755 "./${_binname}" "${pkgdir}/usr/bin/${_binname}"
  install -Dm755 "./jpdfcat" "${pkgdir}/usr/bin/jpdfcat"
  install -Dm755 "./jpdfgrep" "${pkgdir}/usr/bin/jpdfgrep"
  install -Dm644 "./README" "$pkgdir/usr/share/doc/${_binname}/README"
  cat "./${_binname}.1" | gzip > "./${_binname}.1.gz"
  install -Dm644 "./${_binname}.1.gz" "$pkgdir/usr/share/man/man1/${_binname}.1.gz"
}

# vim:set ts=2 sw=2 et:
