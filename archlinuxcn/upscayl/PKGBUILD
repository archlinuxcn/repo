# Maintainer: DeepChirp <deepchirp@archlinuxcn.org>
# Contributor: zxp19821005 <zxp19821005 at 163 dot com>
pkgname=upscayl
_pkgname=Upscayl
pkgver=2.15.0
pkgrel=5
_electronversion=39
pkgdesc="A free and open source AI Image Upscaler App"
arch=('x86_64')
url='https://upscayl.org/'
_ghurl='https://github.com/upscayl/upscayl'
license=('AGPL-3.0-only')
conflicts=("${pkgname}-git" "${pkgname}-bin" "${pkgname}-appimage" "${pkgname}-rpm-bin" "${pkgname}-ncnn" "${pkgname}-ncnn-bin")
provides=("${pkgname}")
options=('!debug')
depends=("electron${_electronversion}" 'libvips' 'libgomp' 'openjpeg2' 'vulkan-driver' 'vulkan-icd-loader' 'bash' 'hicolor-icon-theme')
makedepends=('npm' 'nodejs-lts-iron' 'patchelf' 'imagemagick' 'librsvg')
source=(
    "${pkgname}-${pkgver}.tar.gz::${_ghurl}/archive/refs/tags/v${pkgver}.tar.gz"
    "fix-wayland-wmclass.patch"
    "${pkgname}.sh"
    "${pkgname}.desktop"
)
sha256sums=('566a7882fb95a8722c00f00a248139e2426fa299ae7cae4fe3f0c35280f5e21e'
            '361a644aef5aed1f5820f26917db04de9ac111bf828894048a99040822472b38'
            '291f50480f5a61bc9c68db7d44cd0412071128706baa868a9cb854f8779a1980'
            'efa6be3613767cf6c19931b97bb439b97ca7b475491b61770cf40fbd7ca88674')

prepare() {
    sed -e "
        s/@electronversion@/${_electronversion}/g
        s/@appname@/${pkgname}/g
        s/@runname@/app.asar/g
        s/@cfgdirname@/${_pkgname}/g
        s/@options@/env ELECTRON_OZONE_PLATFORM_HINT=auto/g
    " -i "${srcdir}/${pkgname}.sh"

    cd "${srcdir}/${pkgname}-${pkgver}"

    # Fix the window title bar icon
    patch -Np1 -i "${srcdir}/fix-wayland-wmclass.patch"

	export npm_config_cache="$srcdir/npm_cache"
    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    export SYSTEM_ELECTRON_VERSION="$(electron${_electronversion} -v | sed 's/v//g')"

    sed -i "s/org.${pkgname}.${_pkgname}/${pkgname}/g" flatpak/"org.${pkgname}.${_pkgname}".metainfo.xml
    NODE_ENV=development    npm ci
}

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    export npm_config_cache="$srcdir/npm_cache"
    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    export SYSTEM_ELECTRON_VERSION="$(electron${_electronversion} -v | sed 's/v//g')"
    electronDist="/usr/lib/electron${_electronversion}"

    NODE_ENV=production     npm run tsc
    NODE_ENV=production     npm run build

    # pure frontend UI libraries that already bundled by Next.js
    rm -rf node_modules/@floating-ui
    rm -rf node_modules/@radix-ui
    rm -rf node_modules/class-variance-authority
    rm -rf node_modules/classnames
    rm -rf node_modules/clsx
    rm -rf node_modules/cmdk
    rm -rf node_modules/jotai
    rm -rf node_modules/lucide-react
    rm -rf node_modules/react-compare-slider
    rm -rf node_modules/react-resizable-panels
    rm -rf node_modules/react-select
    rm -rf node_modules/react-tooltip
    rm -rf node_modules/tailwind-merge
    rm -rf node_modules/tailwind-scrollbar
    rm -rf node_modules/tailwindcss-animate
    rm -rf node_modules/theme-change

    # Markdown and text parsing ecosystem
    rm -rf node_modules/mdast*
    rm -rf node_modules/micromark*
    rm -rf node_modules/react-markdown
    rm -rf node_modules/remark*
    rm -rf node_modules/unist*

    # linting, type-checking and dev tools
    rm -rf node_modules/@eslint-community
    rm -rf node_modules/@next/eslint-plugin-next
    rm -rf node_modules/@rushstack/eslint-patch
    rm -rf node_modules/@typescript-eslint
    rm -rf node_modules/eslint-config-next

    # telemetry, cloud services and RPC components
    rm -rf node_modules/@firebase
    rm -rf node_modules/@grpc
    rm -rf node_modules/firebase
    rm -rf node_modules/posthog-js
    rm -rf node_modules/protobufjs

    # macOS specific artifacts
    rm -f export/build/icon.icns

    find node_modules -name '*.map' -type f -print -delete
	find node_modules -name '*.ts' -type f -print -delete
	find node_modules -name Makefile -type f -print -delete
	find node_modules -name '*.yml' -type f -print -delete
	find node_modules -name '*.md' -type f -print -delete

	find node_modules -type d -name 'docs' -prune -exec rm -rf {} +
	find node_modules -type d -name 'test-utils' -prune -exec rm -rf {} +
	find node_modules -type d -name '__tests__' -prune -exec rm -rf {} +

	find . -type d -empty -print -delete

    NODE_ENV=production     npm exec -c "electron-builder --linux dir -c.electronDist=${electronDist} -c.electronVersion=${SYSTEM_ELECTRON_VERSION}"

    for res in 16 32 48 64 128 256 512 1024; do
        mkdir -p "icons-build/${res}x${res}"
        magick -background none "renderer/public/logo.svg" -resize "${res}x${res}" "icons-build/${res}x${res}/${pkgname}.png"
    done
}

package(){
    cd "${srcdir}/${pkgname}-${pkgver}"

    install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
    install -Dm755 -d "${pkgdir}/usr/lib/${pkgname}"
    cp -Pr --no-preserve=ownership "dist/linux-"*/resources/* "${pkgdir}/usr/lib/${pkgname}"
    patchelf --remove-rpath "${pkgdir}/usr/lib/${pkgname}/bin/upscayl-bin"

    install -vDm644 "renderer/public/logo.svg" "${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg"
    for res in 16 32 48 64 128 256 512 1024; do
        install -Dm644 "icons-build/${res}x${res}/${pkgname}.png" \
            "${pkgdir}/usr/share/icons/hicolor/${res}x${res}/apps/${pkgname}.png"
    done
    rm -f "${pkgdir}/usr/lib/${pkgname}/128x128.png"
    rm -f "${pkgdir}/usr/lib/${pkgname}/512x512.png"

    install -Dm644 "${srcdir}/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications"
    install -Dm644 "flatpak/org.${pkgname}.${_pkgname}.metainfo.xml" "${pkgdir}/usr/share/metainfo/${pkgname}.metainfo.xml"

    # Disable update
    rm -f "${pkgdir}/usr/lib/${pkgname}/app-update.yml"
}
