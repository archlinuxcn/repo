# Maintainer: Peter Smit <peter@smitmail.eu>

_pkgname=onedrive
pkgname=$_pkgname-abraunegg
pkgver=2.3.3
pkgrel=1
epoch=
pkgdesc="Free OneDrive client written in D - abraunegg's fork. Follows the releases on https://github.com/abraunegg/onedrive/releases"
arch=('i686' 'x86_64')
url="https://github.com/abraunegg/onedrive"
license=('GPL')
conflicts=('onedrive' 'onedrive-abraunegg-git' 'onedrive-bin' 'onedrive-git' 'onedrive-fork-git')
source=("https://github.com/abraunegg/onedrive/archive/v$pkgver.tar.gz")
provides=("onedrive=$pkgver")
depends=('curl' 'libnotify' 'sqlite')
makedepends=('dmd')

build() {
	cd "$_pkgname-$pkgver"
	make PREFIX=/usr
}

package() {
	cd "$_pkgname-$pkgver"
	echo "$pkgver" > version
	make COMPLETIONS=1 NOTIFICATIONS=1 PREFIX=/usr DESTDIR="$pkgdir" install
}
md5sums=('09bec20042da4cec3f5452899554bcb7')
