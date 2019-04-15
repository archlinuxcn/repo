# Maintainer: Ouyang Jun <ouyangjun1999@gmail.com>
# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jove Yu <yushijun110 [at] gmail.com>
# Contributor: Ariel AxionL <axionl at aosc dot io>

pkgname=wps-office
pkgver=11.1.0.8372
#_pkgver=8372
pkgrel=2
_pkgrel=1
pkgdesc="Kingsoft Office (WPS Office) is an office productivity suite"
arch=('i686' 'x86_64')
license=("custom")
url="http://wps-community.org/"
depends=('fontconfig' 'xorg-mkfontdir' 'libxrender' 'gtk2' 'desktop-file-utils' 'shared-mime-info' 'xdg-utils' 'glu' 'openssl-1.0' 'sdl2' 'libpulse' 'hicolor-icon-theme')
optdepends=('cups: for printing support'
            'libjpeg-turbo: JPEG image codec support'
            'pango: for complex (right-to-left) text support'
            'curl: An URL retrieval utility and library'
            'ttf-wps-fonts: Symbol fonts required by wps-office')
conflicts=('kingsoft-office')
options=('!emptydirs')
install=${pkgname}.install
[[ "$CARCH" = "i686" ]] && _archext=x86 || _archext=x86_64
source_i686=("http://kdl.cc.ksosoft.com/wps-community/download/${pkgver##*.}/wps-office-${pkgver}-${_pkgrel}.i686.rpm"
            'add_no_kdialog_variable.patch')
source_x86_64=("http://kdl.cc.ksosoft.com/wps-community/download/${pkgver##*.}/wps-office-${pkgver}-${_pkgrel}.x86_64.rpm"
               'add_no_kdialog_variable.patch')
sha1sums_i686=('9deb3908d8edad310258de0e31bcafdb5ff6bc5c'
               'dd8b5283ee17a88a3eb0531976abccd6e5e08c48')
sha1sums_x86_64=('d3abdfe94a579083c8bd5e0c817de877e7531e48'
                 'dd8b5283ee17a88a3eb0531976abccd6e5e08c48')

prepare() {
    cd "${srcdir}/usr/bin"
    sed -i 's|/opt/kingsoft/wps-office|/usr/lib|' wps wpp et
#   sed -i 's|/office6/${gApp}  ${gOptExt}|/office6/${gApp} -style gtk+ ${gOptExt}|' wps
#   sed -i 's|/office6/${gApp} ${gOptExt}|/office6/${gApp} -style gtk+ ${gOptExt}|' wpp et

    cd "${srcdir}"
    patch -Np1 -i "${srcdir}/add_no_kdialog_variable.patch"
}

package() {
    #cd wps-office_${pkgver}_$_archext
    cd "${srcdir}/opt/kingsoft/wps-office/"

    install -d "${pkgdir}/usr/lib"
    cp -r office6 "${pkgdir}/usr/lib"
    chmod -x "${pkgdir}/usr/lib/office6/wpsoffice"
    install -Dm644 office6/mui/default/EULA.txt "${pkgdir}/usr/share/licenses/$pkgname/EULA.txt"

    install -d "${pkgdir}/usr/bin"
    cd "${srcdir}/usr/bin"
    install -m755 wps wpp et "${pkgdir}/usr/bin"

    cd "${srcdir}"/usr/share

    install -d "${pkgdir}/usr/share/applications"
    cp -r applications/* "${pkgdir}/usr/share/applications"

    install -d "${pkgdir}/usr/share/icons"
    cp -r icons/* "${pkgdir}/usr/share/icons"

    install -d "${pkgdir}/usr/share/mime"
    cp -r mime/* "${pkgdir}/usr/share/mime"
    #cp -r "$srcdir/usr/share" "${pkgdir}/usr/"

    #install -d "${pkgdir}/usr/share/fonts/wps-office"
    #cp -r fonts/* "${pkgdir}/usr/share/fonts/wps-office"

    install -Dm644 -t "${pkgdir}/etc/xdg/menus/applications-merged" "${srcdir}/etc/xdg/menus/applications-merged/wps-office.menu"
}
