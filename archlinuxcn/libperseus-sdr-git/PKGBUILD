# Maintainer: xiretza <xiretza+aur@xiretza.xyz>
_pkgname=libperseus-sdr
pkgname=$_pkgname-git
pkgver=r94.c2c95da
pkgrel=2
pkgdesc="Perseus Software Defined Radio Control Library for Linux"
arch=(x86_64)
url="https://github.com/Microtelecom/libperseus-sdr"
license=('LGPL')
depends=('libusb')
makedepends=('git' 'vim')
provides=("${pkgname%-git}" 'libperseus-sdr.so')
conflicts=("${pkgname%-git}")
source=("git+$url.git"
        "0001-makefile-install-udev-rules-to-correct-location.patch"
)
sha256sums=('SKIP'
            '49e3b82912c68e279b9edb96ebbaa705b575d7cc13940611ec29342d45b1f09b')

pkgver() {
	cd "$_pkgname"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
	cd "$_pkgname"
	patch -p1 < "$srcdir/0001-makefile-install-udev-rules-to-correct-location.patch"
}

build() {
	cd "$_pkgname"
	autoreconf -i
	./configure --prefix=/usr
	make
}

package() {
	cd "$_pkgname"
	make DESTDIR="$pkgdir/" install
}
