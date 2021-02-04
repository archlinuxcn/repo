pkgname=kmozillahelper
pkgver=5.0.6
pkgrel=1
epoch=1
pkgdesc="Mozilla KDE Integration."
url="https://github.com/openSUSE/kmozillahelper"
arch=("i686" "x86_64")
license=('MIT')
depends=("kio" "knotifications" "kwindowsystem" "ki18n")
makedepends=("cmake" "extra-cmake-modules")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/openSUSE/kmozillahelper/archive/v${pkgver}.tar.gz")
md5sums=('382142073322f942f4d332fffb77ef25')

build() {
	mkdir -p "$srcdir/$pkgname-build"
	cd "$srcdir/$pkgname-build"

	cmake -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_TESTING=OFF -DCMAKE_BUILD_TYPE=Release "$srcdir/${pkgname}-${pkgver}"
	make
}

package() {
	cd "$srcdir/$pkgname-build"
	make DESTDIR="$pkgdir" install
    install -Dm644 "$srcdir/$pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
