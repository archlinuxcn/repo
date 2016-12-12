# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Chuan Ji <ji@chu4n.com>

pkgname=jfbview
pkgver=0.5.3
pkgrel=1
pkgdesc="a PDF and image viewer for the Linux framebuffer"
arch=('i686' 'x86_64')
url="http://seasonofcode.com/pages/jfbview.html"
license=('Apache')
depends=('libmupdf' 'imlib2' 'openjpeg2' 'jbig2dec')
conflicts=('jfbpdf')
replaces=('jfbpdf')
source=("https://github.com/jichu4n/JFBView/archive/${pkgver}.tar.gz")
sha512sums=('873c4d717e573ea0bd22a9e620ac7e369aeef34fac9a97af2b8ac13a24f291d997a646bc9397c380a280b61875930e1ecc5d4e3240bab4ebf45ac02a3000c486')

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
