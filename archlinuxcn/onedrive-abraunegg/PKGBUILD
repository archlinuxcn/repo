# Contributor: Peter Smit <peter@smitmail.eu>
# Maintainer: Matrix <thysupremematrix@tuta.io>
_pkgname=onedrive
pkgname=$_pkgname-abraunegg
pkgver=2.4.24
pkgrel=2
pkgdesc="Free OneDrive client written in D - abraunegg's fork. Follows the releases on https://github.com/abraunegg/onedrive/releases"
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url="https://github.com/abraunegg/onedrive"
license=('GPL')
conflicts=('onedrive' 'onedrive-abraunegg-git' 'onedrive-bin' 'onedrive-git' 'onedrive-fork-git')
source=("https://github.com/abraunegg/onedrive/archive/v$pkgver.tar.gz")
provides=("onedrive=$pkgver")
depends=('libnotify' 'sqlite' 'd-runtime')
makedepends=('d-compiler')
md5sums=('543b14d7881936cf2efe08a3e8a8919d')

build() {
	# Fix "W: ELF file ('usr/bin/onedrive') lacks FULL RELRO, check LDFLAGS."
        # https://bbs.archlinux.org/viewtopic.php?id=280157
        export DCFLAGS='-L-zrelro -L-znow'

	cd "$_pkgname-$pkgver"
        ./configure --sysconfdir=/etc \
                    --prefix=/usr \
                    --with-systemdsystemunitdir=/usr/lib/systemd/system \
                    --with-systemduserunitdir=/usr/lib/systemd/user \
                    --enable-notifications \
                    --enable-completions \
                    --with-zsh-completion-dir=/usr/share/zsh/site-functions \
                    --with-fish-completion-dir=/usr/share/fish/vendor_completions.d \
                    --with-bash-completion-dir=/usr/share/bash-completion/completions
        make
}

package() {
	cd "$_pkgname-$pkgver"
	make DESTDIR="$pkgdir" PREFIX=/usr install

	# Move documentation to onedrive-abraunegg to avoid conflicts
	mv "${pkgdir}/usr/share/doc/onedrive" "${pkgdir}/usr/share/doc/onedrive-abraunegg"
}
