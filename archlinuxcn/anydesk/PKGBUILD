# Maintainer: Oliver Jaksch <arch-aur@com-in.de>

pkgname=anydesk
pkgver=5.5.1
pkgrel=2
pkgdesc="'AnyDesk Free' is an All-In-One Software for Remote Support"
arch=('i686' 'x86_64')
url="https://anydesk.de"
license=('custom:Freeware')
depends=('fakeroot' 'python-shiboken2' 'gtkglext' 'libglvnd' 'gtk2' 'libx11' 'glibc' 'glib2' 'gdk-pixbuf2' 'libxcb' 'cairo' 'pango' 'libxi' 'libxrandr' 'libxtst' 'libxext' 'libxfixes' 'libxdamage' 'gcc-libs')
optdepends=('libpulse')
conflicts=('anydesk-test')

source_i686=(https://download.anydesk.com/linux/${pkgname}_${pkgver}-1_i386.deb)
source_x86_64=(https://download.anydesk.com/linux/${pkgname}_${pkgver}-1_amd64.deb)
source=('anydesk.sh' 'PKGBUILD.pango' 'pango-1.43.0-2.tar.gz')

sha256sums_i686=('0587765e713c8a6a2e59977f0aaed3b2425753a26656df5a5ed69b9e94f6eac1')
sha256sums_x86_64=('17d1dacde77730a84b5acd2f5dbf588638d7a78655cb8256a689479369330440')
sha256sums=('2368b0011fc52cbb4cf8013436628d25db3a86b35ae9a04868e221656a0f77a3' 'f73e451632a1297acba18feb33a1871d532f65640ea59c10ca59152a80034d44' 'a5c9b0530ef5ddb571be4236a8ba624a78ab048fa9be34d135b269052b0459cf')

package() {
    cd "${pkgdir}"
    tar xf "${srcdir}/data.tar.gz"
    #
    # temporary fix for wrong permissions on subdirs:
    find "${pkgdir}" -type d -exec chmod 755 {} \;
    #
    # temporary fix for issues with pango>=1.44
    install "${pkgdir}/usr/bin/anydesk" "${pkgdir}/usr/bin/anydesk.bin"
    install "${srcdir}/anydesk.sh" "${pkgdir}/usr/bin/anydesk"
    cp -r "${srcdir}/pango-1.43.0-2" "${pkgdir}/usr/share/anydesk/files"
    #
    msg2 "\e[1;32mAnyDesk now has a systemd file for unattendant access: anydesk.service \e[0m"
    install -D -m 644 "${pkgdir}/usr/share/anydesk/files/systemd/anydesk.service" "${pkgdir}/usr/lib/systemd/system/anydesk.service"
    sed -i "s/PIDFile=\/tm\/ad.pid/PIDFile=\/run\/anydesk.pid/" "${pkgdir}/usr/lib/systemd/system/anydesk.service"
}
