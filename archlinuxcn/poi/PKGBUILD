# Maintainer: Jianfeng Zhang <swordfeng123@gmail.com>

pkgname=poi
_pkgname=poi
pkgver=10.6.0.beta.3.0.g3c3a1b4f
pkgrel=1
pkgdesc="Scalable KanColle browser and tool"
arch=('any')
url="https://github.com/poooi/poi/"
license=('MIT')
depends=('electron' 'nodejs')
makedepends=('git' 'nodejs' 'imagemagick' 'zlib' 'unzip' 'gulp' 'npm' 'python2')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("git+https://github.com/poooi/poi.git"
        "${_pkgname}.desktop"
        "${_pkgname}.sh")
sha256sums=('SKIP'
            '24f89c538a189a5db96be3e3228aba6e4e7d332c5a368b15dacb6e97ee6f7586'
            '6d7f8d85eff0262cd21a506900352894c925821e26b79923664b2c2a3ab0097a')
options=('!strip') # nothing to strip


prepare() {
    cd ${srcdir}/${pkgname}
    git checkout -f $(git describe --tags $(git rev-list --tags --max-count=1))
}

pkgver() {
    cd "${srcdir}/${_pkgname}"
    git describe --tags --long | sed 's/^v//;s/-/./g'
}

build() {
    cd "${srcdir}/${_pkgname}"
    git clean -xdf
    npm install
    gulp build
}

package() {
    mkdir -p "${pkgdir}/usr/share"
    cp -r "${srcdir}/${_pkgname}/app_compiled" "${pkgdir}/usr/share/poi"
    # workaround for strange behavior of babel
    mkdir -p "${pkgdir}/usr/share/poi/node_modules/.cache/@babel/register"

    cd "${srcdir}"
    install -Dm644 "${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"

    for s in 16 24 32 48 64 96 128 512; do
        mkdir -p "${pkgdir}/usr/share/icons/hicolor/${s}x${s}/apps"
        convert "${_pkgname}/assets/icons/poi.png" -resize ${s}x${s} "${pkgdir}/usr/share/icons/hicolor/${s}x${s}/apps/${_pkgname}.png"
    done

    mkdir -p "${pkgdir}/usr/share/licenses/${_pkgname}"
    ln -s "../../${_pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"

    mkdir -p "${pkgdir}/usr/bin"
    cp "${_pkgname}.sh" "${pkgdir}/usr/bin/${_pkgname}"
    chmod 0755 "${pkgdir}/usr/bin/${_pkgname}"
}
