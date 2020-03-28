# Maintainer: Tod Jackson <tod.jackson@gmail.com>
# Contributor: Özgür Sarıer <echo b3pndXJzYXJpZXIxMDExNjAxMTE1QGdtYWlsLmNvbQo= | base64 -d>
# Contributor: user6553591 <Message on Reddit>
# Contributor: P. Badredin <p dot badredin at gmail dot com>
# Contributor: Justin Blanchard <UncombedCoconut at gmail dot com>
# Contributor: Auguste Pop < auguste [at] gmail [dot] com >

pkgname=stockfish
pkgver=11
pkgrel=3
epoch=1
pkgdesc="A strong chess engine written by Tord Romstad, Marco Costalba, Joona Kiiski"
arch=('i686' 'x86_64' 'armv7' 'armv7h')
url="https://stockfishchess.org/"
license=('GPL3')
depends=('glibc')
source=("https://stockfishchess.org/files/$pkgname-$pkgver-linux.zip")
sha512sums=('f1505814d143e319a748ff7a0abe58ca37481aefdfaaab762b3efeff216294201e085b015b614e44369c7a55de1bbf6e18a0183230c02bdd2fd4945719aeca3d')

build() {
    cd "$pkgname-$pkgver-linux/src"
    if [[ "$CARCH" == "i686" ]]; then
        _arch=x86-32
    elif grep bmi2 /proc/cpuinfo 2>&1; then
        _arch=x86-64-bmi2
    elif grep popcnt /proc/cpuinfo 2>&1; then
        _arch=x86-64-modern
    elif [[ "$CARCH" == "armv7h" ]]; then
    _arch=armv7
    else
	_arch=x86-64
    fi
    
    make build ARCH="$_arch" COMP=gcc
}

package() {
    cd "$pkgname-$pkgver-linux/src"
    make PREFIX="$pkgdir/usr" install
}
