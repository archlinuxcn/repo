# Maintainer: Oliver Jaksch <arch-aur@com-in.de>

pkgname=anydesk
pkgver=2.9.4
pkgrel=1
pkgdesc="'AnyDesk Free' is an All-In-One Software for Remote Support"
arch=('i686' 'x86_64')
url="http://anydesk.de/"
license=('custom:Freeware')
depends=('binutils' 'make' 'fakeroot' 'gtkglext')
optdepends=('libpulse')

source_i686=(http://download.anydesk.com/linux/${pkgname}_${pkgver}-1_i386.deb)
source_x86_64=(http://download.anydesk.com/linux/${pkgname}_${pkgver}-1_amd64.deb)

sha256sums_i686=('0792809448bece3d3be8972a9685ea139af0b49886f6bee7da830fccf2feef1e')
sha256sums_x86_64=('394014cbc1d9ff1a9674f9fd43df4335f92a856880d2911557bd261750c0c5e4')

package() {
    cd "${pkgdir}"
    tar xf "${srcdir}/data.tar.gz"
    #
    # If you want to keep the autostart mode, comment next line
    rm -rf etc/
}
