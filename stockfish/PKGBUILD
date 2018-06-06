# Maintainer : Özgür Sarıer <echo b3pndXJzYXJpZXIxMDExNjAxMTE1QGdtYWlsLmNvbQo= | base64 -d>
# Contributor: user6553591 <Message on Reddit>
# Contributor: P. Badredin <p dot badredin at gmail dot com>
# Contributor: Justin Blanchard <UncombedCoconut at gmail dot com>
# Contributor: Auguste Pop < auguste [at] gmail [dot] com >

pkgname=stockfish
pkgver=9
pkgrel=2
epoch=1
pkgdesc="A strong chess engine written by Tord Romstad, Marco Costalba, Joona Kiiski"
arch=('i686' 'x86_64')
url="https://stockfishchess.org/"
license=('GPL3')
depends=('glibc')
source=("https://${pkgname}.s3.amazonaws.com/${pkgname}-${pkgver}-src.zip")
sha512sums=('47b5dfea9e015dd68e33c8b1a131ed83710e4e5d67abe0c278a423f2940b07c7a5d661ce27915257ae3dad83fc2bb8e50d3d28bfa11a7c4cdf396d0378cd80f8')

build() {
    cd "$srcdir/src"

    if [[ "$CARCH" == "i686" ]]; then
	_arch=x86-32
    elif grep popcnt /proc/cpuinfo 2>&1; then
	_arch=x86-64-modern
    else
	_arch=x86-64
    fi
    
    make profile-build ARCH=$_arch
}

package() {
    cd "$srcdir/src"
    make PREFIX="$pkgdir/usr" install
}
