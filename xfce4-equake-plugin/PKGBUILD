# Maintainer : Maximilien Noal <noal dot maximilien at gmail dot com> [AUR: xcomcmdr]

pkgname=xfce4-equake-plugin
pkgver=1.3.5
pkgrel=2
pkgdesc="monitors earthquakes in the Xfce panel and displays an update \
  when a new one occurs"
arch=('i686' 'x86_64')
url='http://www.e-quake.org'
license='GPL3'
depends=('libxfce4util' 'libxfce4ui' 'xfce4-panel' 'xfconf')
source="http://archive.xfce.org/src/panel-plugins/${pkgname}/1.3/${pkgname}-${pkgver}.tar.bz2"
md5sums='7c520e2f1cd0cc5e33d8346b12e31c02'

build() {
  tar xvf ${pkgname}-${pkgver}.tar.bz2
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr --sysconfdir=/etc \
              --libexecdir=/usr/lib \
              --localstatedir=/var
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}
