# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Chuan Ji <ji@chu4n.com>

pkgname=jfbview
pkgver=0.5.1
pkgrel=1
pkgdesc="a PDF and image viewer for the Linux framebuffer"
arch=('i686' 'x86_64')
url="http://seasonofcode.com/pages/jfbview.html"
license=('Apache')
depends=('mupdf>=1.7' 'imlib2')
makedepends=('git')
conflicts=('jfbpdf')
replaces=('jfbpdf')
source=("https://github.com/jichu4n/JFBView/archive/${pkgver}.tar.gz")
sha512sums=('a48c7a3bd20bba4fbde934ebba2f4966f8b24f4c87becb669ae2d980723806ba08dc15f911623d48ffe5e4f43775abf8b668f114be80a3cd92c81a2ed8a50ad7')

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
