# Maintainer: Oliver Jaksch <arch-aur@com-in.de>

pkgname=anydesk
pkgver=2.9.5
pkgrel=1
pkgdesc="'AnyDesk Free' is an All-In-One Software for Remote Support"
arch=('i686' 'x86_64')
url="http://anydesk.de/"
license=('custom:Freeware')
depends=('binutils' 'make' 'fakeroot' 'gtkglext')
optdepends=('libpulse')

source_i686=(http://download.anydesk.com/linux/${pkgname}_${pkgver}-1_i386.deb)
source_x86_64=(http://download.anydesk.com/linux/${pkgname}_${pkgver}-1_amd64.deb)

sha256sums_i686=('4f367a5cefbd394df95943a314b0f91fb48923faf70e715bee7a58877cf6ad9c')
sha256sums_x86_64=('2594e5fd8172817295af89a86b6a6ac49721fddc2095f0136564ff33ef8ad42d')

package() {
    cd "${pkgdir}"
    tar xf "${srcdir}/data.tar.gz"
    #
    # If you want to keep the autostart mode, comment next line
    rm -rf etc/
}
