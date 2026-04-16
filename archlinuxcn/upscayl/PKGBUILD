# Maintainer: DeepChirp <deepchirp@archlinuxcn.org>
# Contributor: zxp19821005 <zxp19821005 at 163 dot com>
pkgname=upscayl
_pkgname=Upscayl
pkgver=2.15.0
pkgrel=6
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
            'd047f2ea25b9e93772e450cac1b5e5221ead0f63eb8c42ec3094e2f24e3dad14')

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

    pushd node_modules

    # pure frontend UI libraries that already bundled by Next.js
    rm -rf @floating-ui
    rm -rf @radix-ui
    rm -rf class-variance-authority
    rm -rf classnames
    rm -rf clsx
    rm -rf cmdk
    rm -rf jotai
    rm -rf lucide-react
    rm -rf react-compare-slider
    rm -rf react-resizable-panels
    rm -rf react-select
    rm -rf react-tooltip
    rm -rf tailwind-merge
    rm -rf tailwind-scrollbar
    rm -rf tailwindcss-animate
    rm -rf theme-change

    # Markdown and text parsing ecosystem
    rm -rf mdast*
    rm -rf micromark*
    rm -rf react-markdown
    rm -rf remark*
    rm -rf unist*

    # linting, type-checking and dev tools
    rm -rf @eslint-community
    rm -rf @next/eslint-plugin-next
    rm -rf @rushstack/eslint-patch
    rm -rf @typescript-eslint
    rm -rf eslint-config-next

    # telemetry, cloud services and RPC components
    rm -rf @firebase
    rm -rf @grpc
    rm -rf firebase
    rm -rf posthog-js
    rm -rf protobufjs

    find -name '*.map' -type f -print -delete
    find -name '*.ts' -type f -print -delete
    find -name '*.yml' -type f -print -delete
    find -name '*.md' -type f -print -delete
    find -name test.js -type f -print -delete
    find -name Makefile -type f -print -delete

    find -type d -name 'docs' -prune -exec rm -rf {} +
    find -type d -name 'test-utils' -prune -exec rm -rf {} +
    find -type d -name '__tests__' -prune -exec rm -rf {} +

    find . -type d -empty -print -delete

    popd

    # macOS specific artifacts
    rm -f export/build/icon.icns

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
