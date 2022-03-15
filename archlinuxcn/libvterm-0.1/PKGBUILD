# Maintainer: xiretza <xiretza+aur@xiretza.xyz>

_pkgname=libvterm
pkgname=$_pkgname-0.1
pkgver=0.1.4
pkgrel=1
pkgdesc="An abstract C99 library which implements a VT220 or xterm-like terminal emulator"
arch=(x86_64)
url="https://www.leonerd.org.uk/code/libvterm/"
license=('MIT')
depends=('glibc')
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=("https://www.leonerd.org.uk/code/libvterm/$_pkgname-$pkgver.tar.gz")
noextract=()
sha256sums=('bc70349e95559c667672fc8c55b9527d9db9ada0fb80a3beda533418d782d3dd')
validpgpkeys=()

build() {
	cd "$_pkgname-$pkgver"
	make PREFIX=/usr
}

check() {
	cd "$_pkgname-$pkgver"
	make -k test
}

package() {
	cd "$_pkgname-$pkgver"
	make PREFIX=/usr DESTDIR="$pkgdir/" install
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
