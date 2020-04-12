# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Chuan Ji <ji@chu4n.com>

pkgname=jfbview
pkgver=0.5.7
pkgrel=1
pkgdesc="a PDF and image viewer for the Linux framebuffer"
arch=('i686' 'x86_64')
url="https://github.com/jichu4n/jfbview"
license=('Apache')
depends=('libmupdf' 'imlib2' 'openjpeg2' 'jbig2dec')
conflicts=('jfbpdf')
replaces=('jfbpdf')
source=("https://github.com/jichu4n/jfbview/archive/${pkgver}.tar.gz")
sha512sums=('56bef21dcf7445c4a8e7e71858fa49470f8f6db637a7c350ec23f8430cf0eab9d4444a891992129f4d69e954ba28f5fa7cb19da2168d442b576cc22365153919')

_pkgname='jfbview'
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
