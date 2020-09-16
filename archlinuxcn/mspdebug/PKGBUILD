# Maintainer:  Lukas K. <lukas@carrotIndustries.net>

pkgname=mspdebug
pkgver=0.25
pkgrel=2
pkgdesc="A free debugger and firmware downloader for the MSP430/CC430 MCU family"
arch=('i686' 'x86_64')
url="http://dlbeer.co.nz/mspdebug/"
license=('GPL')
depends=('libusb' 'readline' 'libusb-compat')
conflicts=('mspdebug-git')
source=(https://github.com/dlbeer/$pkgname/archive/v$pkgver.tar.gz)

md5sums=('94f62469dbb6c16e04d54d71e3acf678')

build() {
	cd $srcdir/${pkgname}-${pkgver}
	make clean
	make ${MAKEFLAGS}  PREFIX=/usr
}

package() {
	cd $srcdir/${pkgname}-${pkgver}
	make PREFIX=$pkgdir/usr install
}
