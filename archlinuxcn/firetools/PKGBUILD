# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: ajs124 < aur AT ajs124 DOT de > 

pkgname=firetools
pkgver=0.9.58
pkgrel=2
pkgdesc='Graphical user interface of Firejail'
arch=('x86_64')
url='https://firejail.wordpress.com/'
license=('GPL')
depends=('gcc-libs' 'firejail' 'qt5-base')
source=("https://sourceforge.net/projects/firejail/files/firetools/${pkgname}-${pkgver}.tar.xz"{,.asc})
#source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/netblue30/firetools/archive/${pkgver}.tar.gz")
sha256sums=('0122e2a45d8f2e871235d81623a352d89874125ee7e2659a0880fcb7227e09a9'
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
