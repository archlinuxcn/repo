# Maintainer: Jianfeng Zhang <swordfeng123@gmail.com>

pkgname=poi
_pkgname=poi
pkgver=7.2.0.beta.2.0.g74812d4
_pkgver='7.2.0-beta.2'
pkgrel=1
pkgdesc="Scalable KanColle browser and tool"
arch=('any')
url="https://github.com/poooi/poi/"
license=('MIT')
depends=('electron' 'sh')
makedepends=('git' 'npm' 'coreutils' 'findutils' 'sed' 'imagemagick' 'tar' 'zlib' 'unzip' 'gulp')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("git+https://github.com/poooi/poi.git#tag=v${_pkgver}"
        "${_pkgname}.desktop"
        "${_pkgname}.sh")
sha1sums=('SKIP'
          '0578634a64fbb2de2fd35555471a761231a3dc94'
          '321cecdb8f68fb087dfcaa1233ae5ce784095029')

pkgver() {
    cd "${srcdir}/${_pkgname}"
    git describe --tags --long | sed 's/^v//;s/-/./g'
}

build() {
    cd "${srcdir}/${_pkgname}"
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
