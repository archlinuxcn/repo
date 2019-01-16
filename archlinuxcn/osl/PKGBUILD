# Maintainer: Harenome Ranaivoarivony-Razanajato
#             <ranaivoarivony-razanajato@hareno.me>

pkgname=osl
pkgver=0.9.2
pkgrel=2
pkgdesc="OpenScop Library"
arch=('i686' 'x86_64')
url="http://icps.u-strasbg.fr/people/bastoul/public_html/development/openscop/index.html"
license=('BSD')
depends=("gmp")
provides=("osl")
source=(https://github.com/periscop/openscop/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.gz)
md5sums=('21b88885dd315da02b3b054c2ce1032e')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr --with-gmp=system
  make
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make check
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}/" install
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
