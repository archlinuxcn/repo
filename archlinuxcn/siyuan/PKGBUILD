# Maintainer: zxp19821005 <zxp19821005 at 163 dot com>
# Contributor: Xiaozhu1337 <nihaoaheheda@gmail.com>
pkgname=siyuan
pkgver=3.1.30
_electronversion=35
_nodeversion=22
pkgrel=1
pkgdesc="A privacy-first, self-hosted, fully open source personal knowledge management software, written in typescript and golang.(Use system-wide electron)"
arch=(
    'aarch64'
    'x86_64'
)
url="https://b3log.org/siyuan"
_ghurl="https://github.com/siyuan-note/siyuan"
license=('AGPL-3.0-only')
conflicts=(
    "${pkgname}"
    "${pkgname}-note"
)
provides=("${pkgname}")
depends=(
    "electron${_electronversion}"
)
makedepends=(
    'gendesk'
    'curl'
    'nvm'
    'npm'
    'go'
    'pnpm'
    'git'
)
source=(
    "${pkgname}-${pkgver}::git+${_ghurl}#tag=v${pkgver}"
    "${pkgname}.sh"
)
sha256sums=('38c7e5e8c9367cb945352ce343a11e3c1a017f35aa1eebf597be4e29d39fd9ed'
            '291f50480f5a61bc9c68db7d44cd0412071128706baa868a9cb854f8779a1980')
_ensure_local_nvm() {
    local NVM_DIR="${srcdir}/.nvm"
    source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
    nvm install "${_nodeversion}"
    nvm use "${_nodeversion}"
}
prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}/app"
    sed -i -e "
        s/@electronversion@/${_electronversion}/g
        s/@appname@/${pkgname}/g
        s/@runname@/app/g
        s/@cfgdirname@/SiYuan-Electron/g
        s/@options@/env ELECTRON_OZONE_PLATFORM_HINT=auto/g
    " "${srcdir}/${pkgname}.sh"
    _ensure_local_nvm
    gendesk -q -f -n --pkgname="${pkgname}" --pkgdesc="${pkgdesc}" --categories="Office" --name="${pkgname}" --exec="${pkgname} %U"
    sed -i "2i\Name[zh_CN]=思源笔记" "${srcdir}/${pkgname}-${pkgver}/app/${pkgname}.desktop"
    export CGO_ENABLED=1
    export GO111MODULE=on
    export GOOS=linux
    export GOCACHE="${srcdir}/go-build"
    export GOMODCACHE="${srcdir}/go/pkg/mod"
    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    export SYSTEM_ELECTRON_VERSION="$(electron${_electronversion} -v | sed 's/v//g')"
    HOME="${srcdir}/.electron-gyp"
    {
        echo -e '\n'
        #echo 'build_from_source=true'
        echo 'link-workspace-packages=true'
        echo 'fetch-retry-maxtimeout=10000'
        echo "cache-dir="${srcdir}"/.pnpm_cache"
        echo "store-dir="${srcdir}"/.pnpm_store"
    } >> .npmrc
    if [[ "$(curl -s ipinfo.io/country)" == *"CN"* ]]; then
        {
            echo 'registry=https://registry.npmmirror.com'
            echo 'electron_mirror=https://registry.npmmirror.com/-/binary/electron/'
            echo 'electron_builder_binaries_mirror=https://registry.npmmirror.com/-/binary/electron-builder-binaries/'
        } >> .npmrc
        export GOPROXY="https://goproxy.cn,direct"
    fi
    sed -i -e "
        /build:mobile/d
        s/\"electron\": \"\([^\"]*\)\"/\"electron\": \"${SYSTEM_ELECTRON_VERSION}\"/g
    " package.json
    NODE_ENV=development    pnpm install --no-frozen-lockfile
}
build() {
    cd "${srcdir}/${pkgname}-${pkgver}/app"
    NODE_ENV=production     pnpm run build
    cd "${srcdir}/${pkgname}-${pkgver}/kernel"
    go build --tags fts5 -o "../app/kernel-linux/SiYuan-Kernel" -v -ldflags "-s -w -X github.com/siyuan-note/siyuan/kernel/util.Mode=prod"
    cd "${srcdir}/${pkgname}-${pkgver}/app"
    local electronDist="/usr/lib/electron${_electronversion}"
    case "${CARCH}" in
        aarch64)
            _CFG_FILE=electron-builder-linux-arm64.yml
            ;;
        x86_64)
            _CFG_FILE=electron-builder-linux.yml
            ;;
    esac
    NODE_ENV=production pnpm -c exec "electron-builder --linux dir -c.electronDist=${electronDist} --config=${_CFG_FILE} "
}
package() {
    install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/app/build/linux-"*/resources/pandoc.zip -t "${pkgdir}/usr/lib/${pkgname}"
    cp -Pr --no-preserve=ownership "${srcdir}/${pkgname}-${pkgver}/app/build/linux-"*/resources/{app,appearance,changelogs,guide,kernel,stage} "${pkgdir}/usr/lib/${pkgname}"
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/app/src/assets/icon.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/app/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications"
}