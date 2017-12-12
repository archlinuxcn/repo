# Maintainer: GreaterFire <GreaterFire at protonmail dot com>
pkgname=trojan
pkgver=0.5.0
pkgrel=1
pkgdesc="An unidentifiable mechanism that helps you bypass GFW."
arch=('x86_64' 'i686' 'armv6h' 'armv7h' 'arm' 'aarch64')
url="https://github.com/trojan-gfw/trojan"
license=('GPL')
depends=('openssl' 'ca-certificates')
makedepends=('cmake' 'boost' 'openssl')
source=("https://github.com/trojan-gfw/$pkgname/archive/v$pkgver.tar.gz")
backup=('etc/trojan.json' 'etc/systemd/system/trojan.service')
md5sums=('9ac40e8a2986f8b12e7f863a8ec01fdb')
build() {
	cd "$pkgname-$pkgver"
	cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
	make
}
package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
