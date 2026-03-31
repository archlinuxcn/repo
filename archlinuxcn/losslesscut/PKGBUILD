# Maintainer: DeepChirp <DeepChirp@outlook.com>
# Contributor: zxp19821005 <zxp19821005 at 163 dot com>
pkgname=losslesscut
_pkgname=LosslessCut
_appname="no.mifi.${pkgname}"
_reponame=lossless-cut
pkgver=3.68.0
_electronversion=38
_nodeversion=22
pkgrel=4
pkgdesc="The swiss army knife of lossless video/audio editing.Using system-wide ffmpeg.(Use system-wide electron)"
arch=('x86_64')
url="https://github.com/mifi/${_reponame}"
license=('GPL-2.0-only')
conflicts=(
    "${pkgname}-git"
    "${pkgname}-bin"
)
provides=(
    "${pkgname}"
)
depends=(
    "electron${_electronversion}"
    'ffmpeg'
)
makedepends=(
    'nvm'
    'npm'
    'yarn'
    'jq'
)
source=(
    "${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
    "${pkgname}.sh"
)
sha256sums=('b4b2e0d4ba06de0243dfa3be5ec964b28f6c694c412487143b9c68d54b94fbb0'
            '31ad33b633744f5361abd964be306cea53ae1050e760c787115f7eca60045ae6')
_ensure_local_nvm() {
    local NVM_DIR="${srcdir}/.nvm"
    source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
    nvm install "${_nodeversion}"
    nvm use "${_nodeversion}"
}
_get_electron_version() {
    _elec_ver=$(jq -r '.devDependencies["electron"] // .dependencies["electron"]' "package.json" | tr -d '^')
    _main_ver=$(echo "${_elec_ver}" | cut -d. -f1)
    echo -e "The electron version is: \033[1;31m${_main_ver}\033[0m"
}
prepare() {
    cd "${srcdir}/${_reponame}-${pkgver}"
    _get_electron_version
    sed -i -e "
        s/@electronversion@/${_electronversion}/g
        s/@appname@/${pkgname}/g
        s/@runname@/app.asar/g
        s/@cfgdirname@/${_pkgname}/g
        s/@options@//g
    " "${srcdir}/${pkgname}.sh"
    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    export SYSTEM_ELECTRON_VERSION="$(electron${_electronversion} -v | sed 's/v//g')"
    HOME="${srcdir}/.electron-gyp"
    mkdir -p "${srcdir}/.electron-gyp"
    _ensure_local_nvm
    find src -type f -exec sed -i "s/process.resourcesPath/\'\/usr\/lib\/${pkgname}\'/g" {} +
    sed -e "
        s/\/app\/bin\/run.sh/${pkgname}/g;
        s/${_appname}/${pkgname}/g
    " -i "${_appname}.desktop"
    sed -i "s/${_appname}/${pkgname}/g" "${_appname}.appdata.xml"
    sed -i "s/\"electron\": \"[^\"]*\"/\"electron\": \"${SYSTEM_ELECTRON_VERSION}\"/g" package.json
    yarn config set --home enableTelemetry 0
    NODE_ENV=development    yarn add node-gyp
    NODE_ENV=development    yarn install
}
build() {
    cd "${srcdir}/${_reponame}-${pkgver}"
    _ensure_local_nvm
    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    export HOME="${srcdir}/.electron-gyp"
    local electronDist="/usr/lib/electron${_electronversion}"
    NODE_ENV=production     yarn run build
    NODE_ENV=production     yarn electron-builder --linux dir -c.electronDist="${electronDist}"
}
package() {
    install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 "${_reponame}-${pkgver}/dist/linux-unpacked/resources/app.asar" -t "${pkgdir}/usr/lib/${pkgname}"
    cp -r "${_reponame}-${pkgver}/dist/linux-unpacked/resources/locales" "${pkgdir}/usr/lib/${pkgname}/"
    ln -sf "/usr/bin/ffmpeg" "${pkgdir}/usr/lib/${pkgname}/ffmpeg"
    ln -sf "/usr/bin/ffprobe" "${pkgdir}/usr/lib/${pkgname}/ffprobe"
    install -Dm644 "${_reponame}-${pkgver}/icon-build/app-512.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
    install -Dm644 "${_reponame}-${pkgver}/${_appname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
    install -Dm644 "${_reponame}-${pkgver}/${_appname}.appdata.xml" "${pkgdir}/usr/share/metainfo/${pkgname}.appdata.xml"
}
