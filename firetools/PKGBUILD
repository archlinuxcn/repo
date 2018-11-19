# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: ajs124 < aur AT ajs124 DOT de > 

pkgname=firetools
pkgver=0.9.52
pkgrel=4
pkgdesc='Graphical user interface of Firejail'
arch=('i686' 'x86_64')
url='https://firejail.wordpress.com/'
license=('GPL')
depends=('gcc-libs' 'firejail' 'qt5-base')
source=("https://sourceforge.net/projects/firejail/files/firetools/${pkgname}-${pkgver}.tar.xz"{,.asc})
#source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/netblue30/firetools/archive/${pkgver}.tar.gz")
sha256sums=('df4a7d3817154c1f607b9ea4896a6bf90ca84e4e8de6e83208f15b36e54d79a9'
            'SKIP')
validpgpkeys=('F951164995F5C4006A73411E2CCB36ADFC5849A7') # netblue (firejail key)

build() {
    cd "${pkgname}-${pkgver}"
    
    ./configure --prefix='/usr'
    
    make
}

package() {
    cd "${pkgname}-${pkgver}"
    
    make DESTDIR="$pkgdir" install
}
