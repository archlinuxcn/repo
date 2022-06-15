# Maintainer: Peter Smit <peter@smitmail.eu>

_pkgname=onedrive
pkgname=$_pkgname-abraunegg
pkgver=2.4.19
pkgrel=1
epoch=
pkgdesc="Free OneDrive client written in D - abraunegg's fork. Follows the releases on https://github.com/abraunegg/onedrive/releases"
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url="https://github.com/abraunegg/onedrive"
license=('GPL')
conflicts=('onedrive' 'onedrive-abraunegg-git' 'onedrive-bin' 'onedrive-git' 'onedrive-fork-git')
source=("https://github.com/abraunegg/onedrive/archive/v$pkgver.tar.gz")
provides=("onedrive=$pkgver")
depends=('curl' 'libnotify' 'sqlite' 'd-runtime')
makedepends=('d-compiler')

build() {
	cd "$_pkgname-$pkgver"
        ./configure --sysconfdir=/etc --prefix=/usr --with-systemdsystemunitdir=/usr/lib/systemd/system --with-systemduserunitdir=/usr/lib/systemd/user --enable-notifications --enable-completions --with-zsh-completion-dir=/usr/share/zsh/site-functions --with-fish-completion-dir=/usr/share/fish/vendor_completions.d --with-bash-completion-dir=/usr/share/bash-completion/completions
        make
}

package() {
	cd "$_pkgname-$pkgver"
	make DESTDIR=$pkgdir PREFIX=/usr install
}
md5sums=('bc799a322cfa7f79a5b57fcafae0b419')
