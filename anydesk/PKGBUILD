# Maintainer: Oliver Jaksch <arch-aur@com-in.de>

pkgname=anydesk
pkgver=4.0.0
pkgrel=1
pkgdesc="'AnyDesk Free' is an All-In-One Software for Remote Support"
arch=('i686' 'x86_64')
url="https://anydesk.de"
license=('custom:Freeware')
depends=('fakeroot' 'python-shiboken2' 'gtkglext' 'libglvnd' 'gtk2' 'libx11' 'glibc' 'glib2' 'gdk-pixbuf2' 'libxcb' 'cairo' 'pango' 'libxi' 'libxrandr' 'libxtst' 'libxext' 'libxfixes' 'libxdamage' 'gcc-libs')
optdepends=('libpulse')
conflicts=('anydesk-test')

source_i686=(http://download.anydesk.com/linux/${pkgname}_${pkgver}-1_i386.deb)
source_x86_64=(http://download.anydesk.com/linux/${pkgname}_${pkgver}-1_amd64.deb)

sha256sums_i686=('2f4709ea94fcfdaf1086da365f120b8ebac36322c3d1c3c7596f1d55fd60f1ea')
sha256sums_x86_64=('3300fed89b1257154ac6dcea0335bc24e1dfaa2bbabed53681b335773f0f5c2b')

package() {
    cd "${pkgdir}"
    tar xf "${srcdir}/data.tar.gz"
    #
    msg2 "\e[1;32mAnyDesk now has a systemd file for unattendant access: anydesk.service \e[0m"
    install -D -m 644 "${pkgdir}/usr/share/anydesk/files/systemd/anydesk.service" "${pkgdir}/usr/lib/systemd/system/anydesk.service"
    sed -i "s/PIDFile=\/tm\/ad.pid/PIDFile=\/run\/anydesk.pid/" "${pkgdir}/usr/lib/systemd/system/anydesk.service"
}
