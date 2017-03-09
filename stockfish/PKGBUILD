# Maintainer: user6553591 <Message on Reddit>
# Contributor: P. Badredin <p dot badredin at gmail dot com>
# Contributor: Justin Blanchard <UncombedCoconut at gmail dot com>
# Contributor: Auguste Pop < auguste [at] gmail [dot] com >

pkgname=stockfish
pkgver=8
pkgrel=2
epoch=1
pkgdesc="A strong chess engine written by Tord Romstad, Marco Costalba, Joona Kiiski"
arch=('i686' 'x86_64')
url="https://stockfishchess.org/"
license=('GPL3')
depends=('glibc')
install=${pkgname}.install
_pkgfilename=${pkgname}-${pkgver}-src
source=("https://${pkgname}.s3.amazonaws.com/${_pkgfilename}.zip")
sha512sums=('4dcc8c6e975367e96d5b4e76c241094e1bade53fd19fa29320a5df10177ff5ae04844ca7ae9f9cfe929aa1341d898aabbbe523bbdab4c5beef75ca8332ce50c1')

build()
{
    cd "$srcdir/${_pkgfilename}/src"

    if [[ "$CARCH" == "i686" ]];
    then
        _arch=x86-32
    elif grep popcnt /proc/cpuinfo 2>&1
    then
        _arch=x86-64-modern
    else
        _arch=x86-64
    fi
    make profile-build ARCH=$_arch
}

package()
{
    cd "$srcdir/${_pkgfilename}/src"
    make PREFIX="$pkgdir/usr" install
}
