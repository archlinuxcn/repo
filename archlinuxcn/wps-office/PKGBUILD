# Maintainer: Ouyang Jun <ouyangjun1999@gmail.com>
# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jove Yu <yushijun110 [at] gmail.com>
# Contributor: Ariel AxionL <axionl at aosc dot io>

pkgbase=wps-office
pkgname=('wps-office' 'wps-office-mime')
pkgver=11.1.0.9604
#_pkgver=8372
pkgrel=1
#_pkgrel=1
pkgdesc="Kingsoft Office (WPS Office) - an office productivity suite"
arch=('x86_64')
license=('custom')
url="http://wps-community.org/"
options=('!emptydirs')
#[[ "$CARCH" = "i686" ]] && _archext=x86 || _archext=x86_64
#source_i686=("http://kdl.cc.ksosoft.com/wps-community/download/${pkgver##*.}/wps-office_${pkgver}_i386.deb"
#            'add_no_kdialog_variable.patch')
#source=("http://kdl.cc.ksosoft.com/wps-community/download/${pkgver##*.}/wps-office_${pkgver}_amd64.deb"
source=("http://wdl1.pcfg.cache.wpscdn.com/wpsdl/wpsoffice/download/linux/${pkgver##*.}/wps-office_${pkgver}.XA_amd64.deb")
#sha1sums_i686=('60b1c9e33ee6fc1edcefe40dc9ec529d4a668825'
#               'dd8b5283ee17a88a3eb0531976abccd6e5e08c48')
sha1sums=('f7d905898a6777d4c3caf6ffe1e33aa43cd6b549')

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
#   patch -Np1 -i "${srcdir}/fix_desktop_exec.patch"
}

package_wps-office() {
    depends=('fontconfig' 'xorg-mkfontdir' 'libxrender' 'gtk2' 'desktop-file-utils' 'shared-mime-info' 'xdg-utils' 'glu' 'openssl-1.0' 'sdl2' 'libpulse' 'hicolor-icon-theme' 'libxss' 'sqlite' 'libtool')
    optdepends=('cups: for printing support'
                'libjpeg-turbo: JPEG image codec support'
                'pango: for complex (right-to-left) text support'
                'curl: An URL retrieval utility and library'
                'ttf-wps-fonts: Symbol fonts required by wps-office'
                'ttf-ms-fonts: Microsft Fonts recommended for wps-office'
                'wps-office-fonts: FZ TTF fonts provided by wps community'
                'wps-office-mime: Use mime files provided by Kingsoft'
                'wps-office-mui-zh-cn: zh_CN support for WPS Office')
    install=${pkgname}.install
    conflicts=('kingsoft-office')
#   cd wps-office_${pkgver}_$_archext
    cd "${srcdir}/opt/kingsoft/wps-office/"

    install -d "${pkgdir}/usr/lib"
    cp -r office6 "${pkgdir}/usr/lib"
#   chmod -x "${pkgdir}/usr/lib/office6/wpsoffice"
#   ln -rTsf "${pkgdir}/usr/lib/office6"/{libcef.so,addons/cef/libcef.so}
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" office6/mui/default/*.txt

    install -d "${pkgdir}/usr/bin"
    cd "${srcdir}/usr/bin"
    install -m755 * "${pkgdir}/usr/bin"

    cd "${srcdir}/usr/share"

    install -d "${pkgdir}/usr/share/applications"
    cp -r applications/* "${pkgdir}/usr/share/applications"
#   rm "${pkgdir}/usr/share/applications/appurl.desktop"

    install -d "${pkgdir}/usr/share/desktop-directories"
    cp -r desktop-directories/* "${pkgdir}/usr/share/desktop-directories"

    install -d "${pkgdir}/usr/share/icons"
    cp -r icons/* "${pkgdir}/usr/share/icons"

#   cp -r "$srcdir/usr/share" "${pkgdir}/usr/"

    install -Dm644 -t "${pkgdir}/usr/share/fonts/wps-office" fonts/wps-office/*

    install -Dm644 -t "${pkgdir}/etc/xdg/menus/applications-merged" "${srcdir}/etc/xdg/menus/applications-merged/wps-office.menu"
}

package_wps-office-mime() {
    pkgdesc="Mime files provided by Kingsoft Office (WPS Office)"
    depends=('shared-mime-info')
    cd "${srcdir}/usr/share"

    install -d "${pkgdir}/usr/share/mime"
    cp -r mime/* "${pkgdir}/usr/share/mime"

    cd "${srcdir}/opt/kingsoft/wps-office/"
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" office6/mui/default/*.txt
}
