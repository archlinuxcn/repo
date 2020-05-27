# Maintainer: Peter Smit <peter@smitmail.eu>

_pkgname=onedrive
pkgname=$_pkgname-abraunegg
pkgver=2.4.2
pkgrel=1
epoch=
pkgdesc="Free OneDrive client written in D - abraunegg's fork. Follows the releases on https://github.com/abraunegg/onedrive/releases"
arch=('i686' 'x86_64' 'armv7h')
url="https://github.com/abraunegg/onedrive"
license=('GPL')
conflicts=('onedrive' 'onedrive-abraunegg-git' 'onedrive-bin' 'onedrive-git' 'onedrive-fork-git')
source=("https://github.com/abraunegg/onedrive/archive/v$pkgver.tar.gz")
provides=("onedrive=$pkgver")
depends=('curl' 'libnotify' 'sqlite' 'd-runtime')
makedepends=('d-compiler')

build() {
	cd "$_pkgname-$pkgver"
        ./configure --sysconfdir=/etc --prefix=/usr --enable-notifications --enable-completions
        make
}

package() {
	cd "$_pkgname-$pkgver"
	make DESTDIR=$pkgdir PREFIX=/usr install
}
md5sums=('27a8b58a5a67c8922c7bc5a16ddcbb4c')
