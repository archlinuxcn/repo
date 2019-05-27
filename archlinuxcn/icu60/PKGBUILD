# Author: neodarz <neodarz@neodarz.net>

_pkgname=icu
pkgname=${_pkgname}60
pkgver=60.3
pkgrel=1
pkgdesc="International Components for Unicode library"
arch=('i686' 'x86_64')
url="http://www.icu-project.org/"
license=('custom:"icu"')
depends=('gcc-libs>=4.7.1-5')
source=(https://github.com/unicode-org/icu/releases/download/release-${pkgver//./-}/${_pkgname}4c-${pkgver//./_}-src.tgz)
sha512sums=('b91c9989459e301b63091a9b767bdc69621afa3c1a1b9ad57dd0b34d5436e49de096ba1945008ce7b147fe3be70e5f959a77a786feec843decbc505e97a49eaf')

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
