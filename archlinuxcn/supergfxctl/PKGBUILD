# Maintainer: Gregory Land
# Contributor: Fabian Bornschein <fabiscafe-cat-mailbox-dog-com>

pkgname=supergfxctl
pkgver=5.2.7
pkgrel=1
pkgdesc="A utility for Linux graphics switching on Intel/AMD iGPU + nVidia dGPU laptops"
arch=('x86_64')
url="https://gitlab.com/asus-linux/supergfxctl"
license=('MPL-2.0')
depends=('gcc-libs' 'systemd')
makedepends=('rust')
provides=('supergfxctl')
conflicts=('supergfxctl-git'
	'optimus-manager')
source=("https://gitlab.com/asus-linux/supergfxctl/-/archive/$pkgver/supergfxctl-$pkgver.tar.gz")
sha512sums=('bd94646d289c9f3398e1bf2a189554ac60d4db2d4d2cefddc0b342e8a128d4682e20268e0b1f9b168441136ada0b6fadb097a5a35d1023a77528dbf0540de3af')
options=(!debug)
_gitdir=${pkgname%"-git"}

build() {
	cd "$pkgname-$pkgver"
	make build
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir" install
}
