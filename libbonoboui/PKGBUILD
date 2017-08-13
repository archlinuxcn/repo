# $Id$
# Maintainer: PhotonX <photon89@googlemail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=libbonoboui
pkgver=2.24.5
pkgrel=3
pkgdesc="User Interface library for Bonobo"
arch=('i686' 'x86_64')
license=('GPL' 'LGPL')
depends=('libgnomecanvas' 'libgnome')
makedepends=('intltool' 'pkg-config')
options=('!emptydirs')
url="http://www.gnome.org"
source=(https://download.gnome.org/sources/${pkgname}/2.24/${pkgname}-${pkgver}.tar.bz2)
sha256sums=('fab5f2ac6c842d949861c07cb520afe5bee3dce55805151ce9cd01be0ec46fcd')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var --disable-static
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  rm -f "${pkgdir}/usr/share/applications/bonobo-browser.desktop"
}
