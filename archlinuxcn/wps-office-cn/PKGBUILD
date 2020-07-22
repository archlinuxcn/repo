# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Ouyang Jun <ouyangjun1999@gmail.com>
# Contributor: Jove Yu <yushijun110 [at] gmail.com>
# Contributor: Ariel AxionL <axionl at aosc dot io>

pkgbase=wps-office-cn
pkgname=('wps-office-cn' 'wps-office-mime-cn' 'wps-office-mui-zh-cn')
pkgver=11.1.0.9615
pkgrel=1
pkgdesc="Kingsoft Office (WPS Office) CN version - an office productivity suite"
arch=('x86_64' 'aarch64')
license=('custom')
url="https://linux.wps.cn"
options=('!emptydirs')
source_x86_64=("https://wdl1.cache.wps.cn/wps/download/ep/Linux2019/${pkgver##*.}/wps-office_${pkgver}_amd64.deb")
source_aarch64=("https://wdl1.cache.wps.cn/wps/download/ep/Linux2019/${pkgver##*.}/wps-office_${pkgver}_arm64.deb")
sha1sums_x86_64=('244473ac738e88c3392f280cddea5bc211335431')
sha1sums_aarch64=('b7c8a7dc0fd43dd157560ee79615d50ca577e06a')

prepare() {
    bsdtar -xpf data.tar.xz

    cd "${srcdir}/usr/bin"
    sed -i 's|/opt/kingsoft/wps-office|/usr/lib|' *

    cd "${srcdir}/usr/share/icons/hicolor"
    for _file in ./*; do
        if [ -e ${_file}/mimetypes/wps-office2019-etmain.png ]; then
            mkdir -p ${_file}/apps
            cp -p ${_file}/mimetypes/wps-office2019* ${_file}/apps
        fi
    done
}

package_wps-office-cn() {
    depends=('fontconfig' 'xorg-mkfontdir' 'libxrender' 'gtk2' 'desktop-file-utils' 'shared-mime-info' 'xdg-utils' 'glu' 'openssl-1.0' 'sdl2' 'libpulse' 'hicolor-icon-theme' 'libxss' 'sqlite' 'libtool')
    optdepends=('cups: for printing support'
                'libjpeg-turbo: JPEG image codec support'
                'pango: for complex (right-to-left) text support'
                'curl: An URL retrieval utility and library'
                'ttf-wps-fonts: Symbol fonts required by wps-office'
                'ttf-ms-fonts: Microsft Fonts recommended for wps-office'
                'wps-office-fonts: FZ TTF fonts provided by wps community'
                'wps-office-mime-cn: Use mime files provided by Kingsoft'
                'wps-office-mui-zh-cn: zh_CN support for WPS Office')
    install=${pkgname}.install
    conflicts=('kingsoft-office' 'wps-office')
    provides=('wps-office')
    cd "${srcdir}/opt/kingsoft/wps-office/"

    install -d "${pkgdir}/usr/lib"
    cp -r office6 "${pkgdir}/usr/lib"
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" office6/mui/default/*.txt
    rm -r "${pkgdir}/usr/lib/office6/mui/en_US/resource/help"
    rm -r "${pkgdir}/usr/lib/office6/mui/zh_CN"

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

    install -Dm644 -t "${pkgdir}/usr/share/fonts/wps-office" fonts/wps-office/*

    install -Dm644 -t "${pkgdir}/etc/xdg/menus/applications-merged" "${srcdir}/etc/xdg/menus/applications-merged/wps-office.menu"
}

package_wps-office-mui-zh-cn() {
    pkgdesc="Chinese (Simplified) mui package for WPS Office"
    cd "${srcdir}/opt/kingsoft/wps-office/office6/mui"

    install -d "${pkgdir}/usr/lib/office6/mui/en_US/resource"
    cp -r en_US/resource/help "${pkgdir}/usr/lib/office6/mui/en_US/resource"
    cp -r zh_CN "${pkgdir}/usr/lib/office6/mui"

    cd "${srcdir}/opt/kingsoft/wps-office/"
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" office6/mui/default/*.txt
}

package_wps-office-mime-cn() {
    pkgdesc="Mime files provided by Kingsoft Office (WPS Office) cn version"
    depends=('shared-mime-info')
    conflicts=('wps-office-mime')
    provides=('wps-office-mime')
    cd "${srcdir}/usr/share"

    install -d "${pkgdir}/usr/share/mime"
    cp -r mime/* "${pkgdir}/usr/share/mime"

    cd "${srcdir}/opt/kingsoft/wps-office/"
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" office6/mui/default/*.txt
}
