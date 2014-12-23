# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: maz-1 <loveayawaka@gmail.com>

_pkgname=ndiswrapper
pkgname=${_pkgname}-dkms
pkgver=1.59
pkgrel=5
pkgdesc="Module for NDIS (Windows Network Drivers) drivers supplied by vendors.Use with DKMS"
arch=('i686' 'x86_64')
url="http://sourceforge.net/projects/ndiswrapper/"
license=('GPL')
depends=('dkms')
optdepends=('ndisgtk: GTK+ based frontend for ndiswrapper.')
provides=('ndiswrapper')
conflicts=('ndiswrapper')
install=install
source=("http://download.sourceforge.net/ndiswrapper/${_pkgname}-${pkgver}.tar.gz"
       "https://raw.githubusercontent.com/Schwartz/ndiswrapper-patch/master/ndiswrapper-1.59.patch"
       "dkms.conf")
md5sums=('e26a7213468ccd6b0bb4c211c7aadeaa'
         '8bc2bec85cfbd1a04d4038757fbc7829'
         'd8c1c66ef19e6222e66274c0cdfb481a')

build() {
	cd "$srcdir/${_pkgname}-${pkgver}"
	patch -p1 -i ../ndiswrapper-1.59.patch
	make -C utils
}

package() {
	cd "$srcdir/${_pkgname}-${pkgver}"
	mkdir -p ${pkgdir}/usr/src
	cp -RL ./driver ${pkgdir}/usr/src/${_pkgname}-${pkgver}
	cp $srcdir/dkms.conf ${pkgdir}/usr/src/${_pkgname}-${pkgver}
	make -C utils sbindir=/usr/bin usrsbindir=/usr/bin DESTDIR=${pkgdir} install
	
}
