# Author: neodarz <neodarz@neodarz.net>

_pkgname=icu
pkgname=${_pkgname}60
pkgver=60.2
pkgrel=1
pkgdesc="International Components for Unicode library"
arch=('i686' 'x86_64')
url="http://www.icu-project.org/"
license=('custom:"icu"')
depends=('gcc-libs>=4.7.1-5')
source=(https://vorboss.dl.sourceforge.net/project/${_pkgname}/ICU4C/${pkgver}/${_pkgname}4c-${pkgver//./_}-src.tgz)
sha256sums=('f073ea8f35b926d70bb33e6577508aa642a8b316a803f11be20af384811db418')

prepare() {
    # fix xlocale.h problems (FS#55246)
    cd ${srcdir}/${_pkgname}/source
    sed -i 's/xlocale/locale/' i18n/digitlst.cpp
}

build() {
  cd ${srcdir}/${_pkgname}/source
  ./configure --prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man
  make -j5
}

package() {
  cd ${srcdir}/${_pkgname}/source
  make -j5 DESTDIR=${pkgdir} install
  rm -r "${pkgdir}"/usr/{bin,include,sbin,share,lib/*so,lib/icu/{Makefile.inc,current,pkgdata.inc}}
  rm -r "${pkgdir}/usr/lib/pkgconfig"

  # Install license
  install -Dm644 ${srcdir}/${_pkgname}/license.html ${pkgdir}/usr/share/licenses/${pkgname}/license.html
}
