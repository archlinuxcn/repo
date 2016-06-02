# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Chuan Ji <ji@chu4n.com>

pkgname=jfbview
pkgver=0.5.2
pkgrel=1
pkgdesc="a PDF and image viewer for the Linux framebuffer"
arch=('i686' 'x86_64')
url="http://seasonofcode.com/pages/jfbview.html"
license=('Apache')
depends=('libmupdf' 'imlib2' 'openjpeg2' 'jbig2dec')
conflicts=('jfbpdf')
replaces=('jfbpdf')
source=("https://github.com/jichu4n/JFBView/archive/${pkgver}.tar.gz")
sha512sums=('7b21245ac37bcc75fb9d49eaf0e733ffe0aebbe203ebe782e1c79deefe102fec38fd1bc43b6cbc510cd0ac4fd45482472f76e0c2fdcdf7cbf31bbb69d5a77b85')

_pkgname='JFBView'
_binname='jfbview'

build(){
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make
}

package(){
  cd "${srcdir}/${_pkgname}-${pkgver}"
  install -Dm755 "./${_binname}" "${pkgdir}/usr/bin/${_binname}"
  install -Dm644 "./README" "$pkgdir/usr/share/doc/${_binname}/README"
  cat "./${_binname}.1" | gzip > "./${_binname}.1.gz"
  install -Dm644 "./${_binname}.1.gz" "$pkgdir/usr/share/man/man1/${_binname}.1.gz"
}

# vim:set ts=2 sw=2 et:
