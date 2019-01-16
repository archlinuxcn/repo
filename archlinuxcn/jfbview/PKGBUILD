# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Chuan Ji <ji@chu4n.com>

pkgname=jfbview
pkgver=0.5.6
pkgrel=1
pkgdesc="a PDF and image viewer for the Linux framebuffer"
arch=('i686' 'x86_64')
url="https://github.com/jichu4n/jfbview"
license=('Apache')
depends=('libmupdf' 'imlib2' 'openjpeg2' 'jbig2dec')
conflicts=('jfbpdf')
replaces=('jfbpdf')
source=("https://github.com/jichu4n/jfbview/archive/${pkgver}.tar.gz")
sha512sums=('8c669b8afac015ca25ec1637aa342378cffae2bda4a825dbdd7289f9228bad668260fda4cf1e6e5db4f0556833f06e53b91016a9f51b218936f267b4d34dc90d')

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
