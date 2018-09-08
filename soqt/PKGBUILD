# Maintainer: Florian Pritz <bluewind@xinu.at>
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: mickele
# Contributor: marcus fritzsch <fritschy@googlemail.com>

pkgname=soqt
pkgver=1.5.0
pkgrel=8
pkgdesc='A library which provides the glue between Coin and Qt'
arch=('i686' 'x86_64')
url='http://www.coin3d.org/lib/soqt/'
license=('GPL')
depends=('coin' 'qt4')
makedepends=('doxygen')
source=("https://bitbucket.org/Coin3D/coin/downloads/SoQt-${pkgver}.tar.gz")
sha256sums=('f6a34b4c19e536c00f21aead298cdd274a7a0b03a31826fbe38fc96f3d82ab91')

build() {
	cd "${srcdir}/SoQt-${pkgver}/"

	# fix prefix in soqt-config
	sed -i '/^prefix/c prefix="/usr/"' src/Inventor/Qt/common/sogui-config.in

	./configure --prefix=/usr \
		--enable-optimization \
		--enable-man \
		--enable-exceptions \
		--disable-debug \
		--disable-maintainer-mode \
		--disable-dependency-tracking \
		--enable-shared \
		--disable-static \
		--with-qt=/usr

	make
}

package() {
	cd "${srcdir}/SoQt-${pkgver}/"

	make DESTDIR=${pkgdir} install

	rm -f "$pkgdir/usr/share/man/man3/_build"*
}

