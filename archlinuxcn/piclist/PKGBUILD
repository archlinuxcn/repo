# Maintainer: DeepChirp <deepchirp@archlinuxcn.org>

pkgname=piclist
_pkgname=PicList
pkgver=3.6.1
pkgrel=1
_electronversion=39
pkgdesc="A powerful cloud storage and image hosting management tool"
arch=('x86_64')
url='https://piclist.cn/'
_ghurl='https://github.com/Kuingsmile/PicList'
license=('MIT')
depends=("electron${_electronversion}" 'bash' 'hicolor-icon-theme')
makedepends=('nodejs-lts-jod' 'pnpm' 'npm' 'git')
source=("${pkgname}-${pkgver}.tar.gz::${_ghurl}/archive/refs/tags/v${pkgver}.tar.gz"
        "${pkgname}.desktop"
        "${pkgname}.sh")
sha256sums=('72cce0fb49280ffccc83ea667ee252b18ea2d5507302e016b0299c856c10f513'
            '96792576ff904881c2d58e6b7a4aa06aff9d7fa07e950d603c45edda7c4b4de2'
            '4b1dc5f32f0295bd672ea0ff12ac63c98256e1e654d864401fb4f1a6d4b3d8f6')

prepare() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    sed -e "
        s/@electronversion@/${_electronversion}/g
        s/@appname@/${pkgname}/g
        s/@runname@/app.asar/g
        s/@cfgdirname@/${pkgname}/g
        s/@options@/--ozone-platform-hint=auto/g
    " -i "${srcdir}/${pkgname}.sh"

    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    export NODE_ENV=development
    export SYSTEM_ELECTRON_VERSION="$(electron${_electronversion} -v | sed 's/v//g')"
    export PNPM_HOME="${srcdir}/.pnpm"
    pnpm config set store-dir "${srcdir}/.pnpm-store"

    pnpm install --shamefully-hoist

    # Workaround for ESM compatibility
    find node_modules -path '*/signal-exit/index.js' -exec sed -i '$a module.exports.onExit = module.exports;' {} +
    find node_modules -path '*/brace-expansion/index.js' -exec sed -i '$a module.exports.expand = module.exports;' {} +
}

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    export NODE_ENV=production
    export PNPM_HOME="${srcdir}/.pnpm"
    electronDist="/usr/lib/electron${_electronversion}"

    pnpm run build:app

    pushd node_modules

    rm -rf @img/*linux-arm64* @img/*darwin* @img/*win32* @img/*musl*
    rm -rf @resvg/*linux-arm64* @resvg/*darwin* @resvg/*win32*

    find -name '*.map' -type f -print -delete
    find -name '*.ts' -type f -print -delete
	find -name '*.cts' -type f -print -delete
    find -name '*.mts' -type f -print -delete
    find -name '*.yml' ! -name '.yarn-state.yml' -type f -print -delete
    find -name '*.md' -type f -print -delete
    find -name test.js -type f -print -delete
    find -name Makefile -type f -print -delete

    find -type d -name 'test' -prune -exec rm -rf {} +

    find . -type d -empty -print -delete

    popd

    pnpm exec electron-builder --linux dir -c.electronDist="${electronDist}" -c.electronVersion="${SYSTEM_ELECTRON_VERSION}"
}

package(){
    install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"

    install -Dm755 -d "${pkgdir}/usr/lib/${pkgname}"
    cp -Pr --no-preserve=ownership "${srcdir}/${_pkgname}-${pkgver}/dist_electron/linux-unpacked/resources/"* "${pkgdir}/usr/lib/${pkgname}"
    rm -rf "${pkgdir}/usr/lib/${pkgname}/plugin-runtime/npm"
    ln -sf "/usr/lib/node_modules/npm" "${pkgdir}/usr/lib/${pkgname}/plugin-runtime/npm"

    for res in 256 512; do
        install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/build/icons/${res}x${res}.png" \
            "${pkgdir}/usr/share/icons/hicolor/${res}x${res}/apps/${pkgname}.png"
    done

    install -Dm644 "${srcdir}/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications"

    install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
