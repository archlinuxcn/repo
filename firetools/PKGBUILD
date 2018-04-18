# Maintainer : Daniel Bermond < yahoo-com: danielbermond >
# Contributor: ajs124 < aur AT ajs124 DOT de > 

pkgname=firetools
pkgver=0.9.52
pkgrel=1
pkgdesc='GUI tools for firejail'
arch=('i686' 'x86_64')
url='https://firejail.wordpress.com/'
license=('GPL')
depends=('firejail' 'qt5-base' 'qt5-svg')
source=("http://sourceforge.net/projects/firejail/files/firetools/${pkgname}-${pkgver}.tar.xz")
#source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/netblue30/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('df4a7d3817154c1f607b9ea4896a6bf90ca84e4e8de6e83208f15b36e54d79a9')

build() {
    cd "${pkgname}-${pkgver}"
    
    ./configure --prefix='/usr'
    
    make
}

package() {
    cd "${pkgname}-${pkgver}"
    
    make DESTDIR="$pkgdir" install
}
