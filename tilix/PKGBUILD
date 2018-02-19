# Maintainer: Carl George < arch at cgtx dot us >

pkgname="tilix"
pkgver=1.7.5
pkgrel=2
pkgdesc="A tiling terminal emulator for Linux using GTK+ 3"
arch=('x86_64' 'i686')
url="https://github.com/gnunn1/tilix"
license=('MPL')
depends=('libx11' 'gtkd' 'vte3' 'dconf' 'gsettings-desktop-schemas')
makedepends=('ldc' 'po4a')
optdepends=('python-nautilus: for "Open Tilix Here" support in nautilus'\
            'vte3-notification: for desktop notifications support'\
            'vte3-tilix: for notifications, triggers and badges support'
            'libsecret: for the password manager')
provides=('terminix')
conflicts=('terminix')
replaces=('terminix')
source=("$url/archive/$pkgver/$pkgname-$pkgver.tar.gz")
#        "$url/commit/1de71cc0f77d1da9ee03425d3444c424150bc101.patch")
sha256sums=('324c565e71ae5f975d5488241915c1e12eb27695a1d4b896443fb7ef02dd39c0')
#            'bb38279ff6ddaa16aa0cb794a9a531293659a6e84f8c13cc3954fad1733022bb')

prepare() {
    cd "$pkgname-$pkgver"
	# Cherry-pick
	#patch -p1 -i "../1de71cc0f77d1da9ee03425d3444c424150bc101.patch"
    ./autogen.sh
}

build() {
    cd "$pkgname-$pkgver"
    ./configure --prefix=/usr PO4A_TRANS=/usr/bin/vendor_perl/po4a-translate DC='ldmd' DCFLAGS='-O -inline -release -version=StdLoggerDisableTrace -defaultlib=phobos2-ldc-shared,druntime-ldc-shared'
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
