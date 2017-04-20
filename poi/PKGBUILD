# Maintainer: Jianfeng Zhang <swordfeng123@gmail.com>

pkgname=poi
_pkgname=poi
pkgver=7.6.0.beta.0.0.g11bd7066
pkgrel=1
pkgdesc="Scalable KanColle browser and tool"
arch=('any')
url="https://github.com/poooi/poi/"
license=('MIT')
depends=('electron' 'sh')
makedepends=('git' 'npm' 'coreutils' 'findutils' 'sed' 'imagemagick' 'tar' 'zlib' 'unzip' 'gulp')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("git+https://github.com/poooi/poi.git"
        "${_pkgname}.desktop"
        "${_pkgname}.sh")
sha256sums=('SKIP'
          '24f89c538a189a5db96be3e3228aba6e4e7d332c5a368b15dacb6e97ee6f7586'
          '1d49f43801fcc28d1a2a75407422a6445314fbf815e004382fc2cb5b956ac530')


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
    sed -i 's/^.*"electron-prebuilt".*$//;s/^.*"electron-builder".*$//;s/^.*"electron".*$//' package.json
    npm install
    # prevent infinite loop...
    timeout 5m npm run deploy
}

package() {
    cd "${srcdir}"

    find "${_pkgname}" -not -path '*/\.*' -type f -exec install -Dm644 {} "${pkgdir}/usr/share/{}" \;

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
