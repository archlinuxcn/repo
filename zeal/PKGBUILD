# Maintainer: Oleg Shparber <trollixx+aur@gmail.com>
# Maintainer: Thomas Weißschuh <thomas t-8ch de>

pkgname=zeal
epoch=1
pkgver=0.3.0
pkgrel=2
pkgdesc='An offline API documentation browser'
arch=('i686' 'x86_64')
url='https://zealdocs.org/'
license=('GPL3')
depends=('qt5-webkit' 'hicolor-icon-theme' 'desktop-file-utils' 'libarchive'
         'qt5-x11extras')
makedepends=()
conflicts=(zeal-git)
source=("zeal-${pkgver}.tar.gz::https://github.com/zealdocs/zeal/archive/v${pkgver}.tar.gz")
sha256sums=('d723c6bc3cb08398d10e7c204929853c9d40d57431a5a16752630b258ae96dc1')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	QT_SELECT=5 qmake CONFIG+=force_debug_info
	make
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make INSTALL_ROOT="$pkgdir" install
}
