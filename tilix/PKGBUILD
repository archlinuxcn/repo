# Maintainer: Carl George < arch at cgtx dot us >

pkgname="tilix"
pkgver=1.7.3
pkgrel=1
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
source=("$url/archive/$pkgver/$pkgname-$pkgver.tar.gz")
#        "$url/commit/3a9efb7209a6df73117b1756b1f394f1143949a6.patch")
sha256sums=('c05cac4073267e576671f69613f644c4b52769253edd473a48f406b7f10d954c')
#            'de7c01148bdcf41502e048c0afe7f0da00ddebed6c5259f94d180df4db5b1552')

prepare() {
    cd "$pkgname-$pkgver"
	# Cherry-pick fix for gtkd 3.7.1
	#patch -p1 -i "../3a9efb7209a6df73117b1756b1f394f1143949a6.patch"
    ./autogen.sh
}

build() {
    cd "$pkgname-$pkgver"
    ./configure --prefix=/usr PO4A_TRANS=/usr/bin/vendor_perl/po4a-translate
    make DC='ldmd' DCFLAGS='-O -inline -release -version=StdLoggerDisableTrace'
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
