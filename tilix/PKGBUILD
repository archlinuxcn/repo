# Maintainer: Carl George < arch at cgtx dot us >

pkgname="tilix"
pkgver=1.7.3
pkgrel=2
pkgdesc="A tiling terminal emulator for Linux using GTK+ 3"
arch=('x86_64' 'i686')
url="https://github.com/gnunn1/tilix"
license=('MPL')
depends=('libx11' 'gtkd' 'vte3' 'dconf' 'gsettings-desktop-schemas')
makedepends=('ldc' 'po4a')
optdepends=('python2-nautilus: for "Open Tilix Here" support in nautilus'\
            'vte3-notification: for desktop notifications support'\
            'vte3-tilix: for notifications, triggers and badges support'
            'libsecret: for the password manager')
provides=('terminix')
conflicts=('terminix')
replaces=('terminix')
source=("$url/archive/$pkgver/$pkgname-$pkgver.tar.gz"
        "$url/commit/1de71cc0f77d1da9ee03425d3444c424150bc101.patch")
sha256sums=('c05cac4073267e576671f69613f644c4b52769253edd473a48f406b7f10d954c'
            'bb38279ff6ddaa16aa0cb794a9a531293659a6e84f8c13cc3954fad1733022bb')

prepare() {
    cd "$pkgname-$pkgver"
	# Cherry-pick fix for gtkd 3.7.1
	patch -p1 -i "../1de71cc0f77d1da9ee03425d3444c424150bc101.patch"
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
