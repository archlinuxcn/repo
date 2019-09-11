# Maintainer: Ouyang Jun <ouyangjun1999@gmail.com>
# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jove Yu <yushijun110 [at] gmail.com>
# Contributor: Ariel AxionL <axionl at aosc dot io>

pkgname=wps-office
pkgver=11.1.0.8865
#_pkgver=8372
pkgrel=1
#_pkgrel=1
pkgdesc="Kingsoft Office (WPS Office) is an office productivity suite"
arch=('x86_64')
license=('custom')
url="http://wps-community.org/"
depends=('fontconfig' 'xorg-mkfontdir' 'libxrender' 'gtk2' 'desktop-file-utils' 'shared-mime-info' 'xdg-utils' 'glu' 'openssl-1.0' 'sdl2' 'libpulse' 'hicolor-icon-theme' 'libxss')
optdepends=('cups: for printing support'
            'libjpeg-turbo: JPEG image codec support'
            'pango: for complex (right-to-left) text support'
            'curl: An URL retrieval utility and library'
            'ttf-wps-fonts: Symbol fonts required by wps-office'
            'wps-office-fonts: FZ TTF fonts provided by wps community')
conflicts=('kingsoft-office')
options=('!emptydirs')
install=${pkgname}.install
#[[ "$CARCH" = "i686" ]] && _archext=x86 || _archext=x86_64
#source_i686=("http://kdl.cc.ksosoft.com/wps-community/download/${pkgver##*.}/wps-office_${pkgver}_i386.deb"
#            'add_no_kdialog_variable.patch')
source=("http://kdl.cc.ksosoft.com/wps-community/download/${pkgver##*.}/wps-office_${pkgver}_amd64.deb")
#       'add_no_kdialog_variable.patch')
#sha1sums_i686=('60b1c9e33ee6fc1edcefe40dc9ec529d4a668825'
#               'dd8b5283ee17a88a3eb0531976abccd6e5e08c48')
sha1sums=('ee5e2ea5f7480bb7d6e116dd7690990a861c8a37')
#         '49ccf3e3d9c7c9c80294127ce063c56d2b57d7c4')

prepare() {
    bsdtar -xpf data.tar.xz

    cd "${srcdir}/usr/bin"
    sed -i 's|/opt/kingsoft/wps-office|/usr/lib|' *
#   sed -i 's|/office6/${gApp}  ${gOptExt}|/office6/${gApp} -style gtk+ ${gOptExt}|' wps
#   sed -i 's|/office6/${gApp} ${gOptExt}|/office6/${gApp} -style gtk+ ${gOptExt}|' wpp et

    cd "${srcdir}/usr/share/icons/hicolor"

    for _file in ./*; do
        if [ -e ${_file}/mimetypes/wps-office2019-etmain.png ]; then
            mkdir -p ${_file}/apps
            cp -p ${_file}/mimetypes/wps-office2019* ${_file}/apps
        fi
    done

#   cd "${srcdir}"
#   patch -Np1 -i "${srcdir}/add_no_kdialog_variable.patch"
}

package() {
#   cd wps-office_${pkgver}_$_archext
    cd "${srcdir}/opt/kingsoft/wps-office/"

    install -d "${pkgdir}/usr/lib"
    cp -r office6 "${pkgdir}/usr/lib"
#   chmod -x "${pkgdir}/usr/lib/office6/wpsoffice"
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" office6/mui/default/*.txt

    install -d "${pkgdir}/usr/bin"
    cd "${srcdir}/usr/bin"
    install -m755 * "${pkgdir}/usr/bin"

    cd "${srcdir}/usr/share"

    install -d "${pkgdir}/usr/share/applications"
    cp -r applications/* "${pkgdir}/usr/share/applications"

    install -d "${pkgdir}/usr/share/desktop-directories"
    cp -r desktop-directories/* "${pkgdir}/usr/share/desktop-directories"

    install -d "${pkgdir}/usr/share/icons"
    cp -r icons/* "${pkgdir}/usr/share/icons"

    install -d "${pkgdir}/usr/share/mime"
    cp -r mime/* "${pkgdir}/usr/share/mime"
#   cp -r "$srcdir/usr/share" "${pkgdir}/usr/"

#   install -d "${pkgdir}/usr/share/fonts/wps-office"
#   cp -r fonts/* "${pkgdir}/usr/share/fonts/wps-office"

    install -Dm644 -t "${pkgdir}/etc/xdg/menus/applications-merged" "${srcdir}/etc/xdg/menus/applications-merged/wps-office.menu"
}
