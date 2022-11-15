# Maintainer: taotieren <admin@taotieren.com>

pkgbase=smiley-sans-git
pkgname=({ttf,otf,woff2}-$pkgbase)
pkgver=1.0.0.r1.g7980755
pkgrel=1
pkgdesc='得意黑 Smiley Sans 开发版'
url="https://github.com/atelier-anchor/smiley-sans"
depends=(fontconfig)
makedepends=(git python-brotli python-fontmake python-fonttools)
license=("OFL-1.1")
arch=(any)
source=("${pkgbase%-git}::git+${url}.git")
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgbase%-git}"
    git describe --long --tags | sed 's/^v//g;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "${srcdir}/${pkgbase%-git}"
    rm -rf "${srcdir}/${pkgbase%-git}/build"
    sh  "${srcdir}/${pkgbase%-git}/build.sh"
}

package_ttf-smiley-sans-git() {
    pkgdesc+=" (ttf)"
    conflicts=(${pkgname%-git})

    cd "${srcdir}/${pkgbase%-git}/build"

    install -Dm644 -t "${pkgdir}/usr/share/fonts/${pkgbase%-git}" *.ttf
    install -Dm644 "${srcdir}/${pkgbase%-git}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname%-git}/LICENSE"
}

package_otf-smiley-sans-git() {
    pkgdesc+=" (otf)"
    conflicts=(${pkgname%-git})

    cd "${srcdir}/${pkgbase%-git}/build"

    install -Dm644 -t "${pkgdir}/usr/share/fonts/${pkgbase%-git}" *.otf
    install -Dm644 "${srcdir}/${pkgbase%-git}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname%-git}/LICENSE"
}

package_woff2-smiley-sans-git() {
    pkgdesc+=" (woff2)"
    conflicts=(${pkgname%-git})

    cd "${srcdir}/${pkgbase%-git}/build"

    install -Dm644 -t "${pkgdir}/usr/share/fonts/${pkgbase%-git}" *.woff2
    install -Dm644 "${srcdir}/${pkgbase%-git}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname%-git}/LICENSE"
}
