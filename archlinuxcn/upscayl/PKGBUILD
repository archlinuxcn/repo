# Maintainer: DeepChirp <DeepChirp@outlook.com>
# Contributor: zxp19821005 <zxp19821005 at 163 dot com>
pkgname=upscayl
_pkgname=Upscayl
pkgver=2.15.0
pkgrel=2
_electronversion=39
_nodeversion=20
pkgdesc="Free and Open Source AI Image Upscaler.(Use system-wide electron)"
arch=('x86_64')
url='https://upscayl.org/'
_ghurl='https://github.com/upscayl/upscayl'
license=('AGPL-3.0-only')
conflicts=("${pkgname}-git" "${pkgname}-bin" "${pkgname}-appimage" "${pkgname}-rpm-bin" "${pkgname}-ncnn" "${pkgname}-ncnn-bin")
provides=("${pkgname}")
depends=(
    "electron${_electronversion}"
    "libvips"
    "openjpeg2"
    "nodejs"
    "vulkan-driver"
)
makedepends=(
    'git'
    'npm'
    'nvm'
    'elfutils'
    'curl'
    'gcc'
    'gendesk'
)
optdepends=(
    'vulkan-intel: Open-source Vulkan driver for Intel GPUs'
    'vulkan-radeon: Open-source Vulkan driver for AMD GPUs'
    'vulkan-nouveau: Open-source Vulkan driver for Nvidia GPUs'
)
source=(
    "${pkgname}-${pkgver}.tar.gz::${_ghurl}/archive/refs/tags/v2.15.0.tar.gz"
    "${pkgname}.sh"
)
sha256sums=('566a7882fb95a8722c00f00a248139e2426fa299ae7cae4fe3f0c35280f5e21e'
            '291f50480f5a61bc9c68db7d44cd0412071128706baa868a9cb854f8779a1980')
_ensure_local_nvm() {
    local NVM_DIR="${srcdir}/.nvm"
    source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
    nvm install "${_nodeversion}"
    nvm use "${_nodeversion}"
}
prepare() {
    sed -e "
        s/@electronversion@/${_electronversion}/g
        s/@appname@/${pkgname}/g
        s/@runname@/app.asar/g
        s/@cfgdirname@/${_pkgname}/g
        s/@options@/env ELECTRON_OZONE_PLATFORM_HINT=auto/g
    " -i "${srcdir}/${pkgname}.sh"
    _ensure_local_nvm
    gendesk -q -f -n --pkgname="${pkgname}" --pkgdesc="${pkgdesc}" --categories="Graphics" --name="${_pkgname}" --exec="${pkgname} %U"
    cd "${srcdir}/${pkgname}-${pkgver}"
    electronDist="/usr/lib/electron${_electronversion}"
    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    export SYSTEM_ELECTRON_VERSION="$(electron${_electronversion} -v | sed 's/v//g')"
    HOME="${srcdir}/.electron-gyp"
    {
        echo -e '\n'
        #echo 'build_from_source=true'
        echo "cache=${srcdir}/.npm_cache"
    } >> .npmrc
    sed -i "s/org.${pkgname}.${_pkgname}/${pkgname}/g" flatpak/"org.${pkgname}.${_pkgname}".metainfo.xml
    NODE_ENV=development    npm install
}
build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    NODE_ENV=production     npm run tsc
    NODE_ENV=production     npm run build
    NODE_ENV=production     npm exec -c "electron-builder --linux dir -c.electronDist=${electronDist}"
}
package(){
    install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
    install -Dm755 -d "${pkgdir}/usr/lib/${pkgname}"
    cp -Pr --no-preserve=ownership "${srcdir}/${pkgname}-${pkgver}/dist/linux-"*/resources/* "${pkgdir}/usr/lib/${pkgname}"
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/build/icon.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
    install -Dm644 "${srcdir}/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications"
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/flatpak/org.${pkgname}.${_pkgname}.metainfo.xml" "${pkgdir}/usr/share/metainfo/${pkgname}.metainfo.xml"

    # Disable update
    rm -f "${pkgdir}/usr/lib/${pkgname}/app-update.yml"
}
