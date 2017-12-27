# Maintainer: Jianfeng Zhang <swordfeng123@gmail.com>

pkgname=poi
_pkgname=poi
pkgver=8.1.0.beta.0.0.g8206b623
pkgrel=1
pkgdesc="Scalable KanColle browser and tool"
arch=('any')
url="https://github.com/poooi/poi/"
license=('MIT')
depends=('electron' 'sh')
makedepends=('git' 'nodejs' 'yarn' 'coreutils' 'findutils' 'sed' 'imagemagick' 'tar' 'zlib' 'unzip' 'gulp' 'npm' 'python2')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("git+https://github.com/poooi/poi.git"
        "${_pkgname}.desktop"
        "${_pkgname}.sh")
sha256sums=('SKIP'
          '24f89c538a189a5db96be3e3228aba6e4e7d332c5a368b15dacb6e97ee6f7586'
          '1d49f43801fcc28d1a2a75407422a6445314fbf815e004382fc2cb5b956ac530')
options=('!strip') # nothing to strip


prepare() {
    cd ${srcdir}/${pkgname}
    git checkout -f $(git describe --tags $(git rev-list --tags --max-count=1))
}

pkgver() {
    cd "${srcdir}/${_pkgname}"
    git describe --tags --long | sed 's/^v//;s/-/./g'
}

compile() {
    local filename
    filename="$1"
    echo "[Compile] ${filename}"
    node -e "console.log(require('babel-core').transformFileSync(process.argv[1], require('./babel.config.js')).code)" "$filename" > "${filename%.es}.js" \
    && rm "$filename"
}

build() {
    cd "${srcdir}/${_pkgname}"
    git clean -xdf
    #sed -i 's/^.*"electron-prebuilt".*$//;s/^.*"electron-builder".*$//;s/^.*"electron-builder-squirrel-windows".*$//;s/^.*"electron".*$//' package.json
    yarn install
    yarn add eachr # workaround
    # prevent infinite loop...
    timeout 5m gulp deploy
    export -f compile
    find . -type f -name '*.es' -exec bash -c 'compile "$0"' {} \;
    yarn install --production
}

package() {
    cd "${srcdir}"

    for path in app.js assets babel.config.js i18n index.html index.js lib LICENSE node_modules package.json PepperFlash views; do
        find "${_pkgname}/${path}" -type f -exec install -Dm644 {} "${pkgdir}/usr/share/{}" \;
    done

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
