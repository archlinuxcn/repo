# Maintainer: Oliver Jaksch <arch-aur@com-in.de>

pkgname=anydesk
pkgver=2.9.3
pkgrel=1
pkgdesc="'AnyDesk Free' is an All-In-One Software for Remote Support"
arch=('i686' 'x86_64')
url="http://anydesk.de/"
license=('custom:Freeware')
depends=('binutils' 'make' 'fakeroot' 'gtkglext')
optdepends=('libpulse')

source_i686=(http://download.anydesk.com/linux/${pkgname}_${pkgver}-1_i386.deb)
source_x86_64=(http://download.anydesk.com/linux/${pkgname}_${pkgver}-1_amd64.deb)

sha256sums_i686=('adac792de77fe9a9bc104358a58537dd02df554cbbd6bb4490725e9614c8259b')
sha256sums_x86_64=('694ca76fb0698f80d211ccd5b120510955b1d9f8deba0bb84edb668fa885ddea')

package() {
    cd "${pkgdir}"
    tar xf "${srcdir}/data.tar.gz"
    #
    # If you want to keep the autostart mode, comment next line
    rm -rf etc/
}
