# Maintainer: Sean Anderson <seanga2@gmail.com>
_pkgname=arch-test
pkgname=${_pkgname}-bin
pkgver=0.20
_debrel=1
pkgrel=2
epoch=
pkgdesc="detect architectures supported by your machine/kernel"
arch=('any')
url="https://github.com/kilobyte/arch-test/"
license=('MIT')
groups=()
depends=('bash' 'perl')
makedepends=()
checkdepends=()
optdepends=()
provides=('arch-test')
conflicts=('arch-test')
backup=()
options=(!strip)
install=
changelog=
source=("http://ftp.debian.org/debian/pool/main/a/arch-test/${_pkgname}_$pkgver-${_debrel}_all.deb")
noextract=()
sha256sums=('f8b4659feef23095e3c9f678d5607f34f3db6972ae6619c53ff9b28dc920a72e')
validpgpkeys=()

prepare() {
	tar -xf data.tar.xz
}

package() {
	cp -a usr $pkgdir
	mkdir -p $pkgdir/usr/share/licenses/$pkgname
	mv $pkgdir/usr/share/doc/arch-test/copyright $pkgdir/usr/share/licenses/$pkgname
	rm -rf $pkgdir/usr/share/{doc,lintian}
}
