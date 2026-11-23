# Maintainer: zhullyb <zhullyb [at] outlook dot com>
# Contributor: weearc <q19981121 [at] 163 dot com>
# Contributor: JimMoen <LnJimMoen [at] outlook dot com>

pkgname=motrix
_pkgname=Motrix
pkgver=2.4.3
pkgrel=1
pkgdesc="A full-featured download manager"
arch=('x86_64')
url="https://github.com/agalwood/Motrix"
license=('MIT')
# Upstream 2.3.0 targets Electron 45, but Arch currently packages Electron 44.
# Switch electron44 and the launcher to electron45 as soon as it reaches the
# repositories, then rebuild and rerun the native ABI and runtime checks.
depends=(
    'electron44'
    'glibc'
    'hicolor-icon-theme'
    'libstdc++'
    'xdg-utils'
)
makedepends=(
    'nodejs'
    'pnpm'
    'python'
    'rust'
    'rust-musl'
)
optdepends=(
    'libayatana-appindicator: system tray integration'
    'libnotify: desktop notifications'
)
provides=('motrix')
conflicts=('motrix-bin' 'motrix-git' 'motrix-beta-bin')
options=('!strip')
source=(
    "${_pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
    'motrix'
    'motrix.desktop'
    'system-electron.patch'
)
sha256sums=('1296192cbdba263fd2d657c3fb19ff7ac22db9689881b76a52a4ebf78fbfcff2'
            '026c1c4ebd4451274c737f21e9636a3c2250e667ef5e9f21913f5b9a7181a67f'
            'ddc5858228ed3b4d6222cc0ec55c48f8caf0215b8f9d0b7ca9eb6ffb6e92f6fb'
            'd67f5b77882cfa5c0d28ebf69a85681efaa445469f2503b891b1def589f7d669')

prepare() {
    patch -Np1 -d "${srcdir}/${_pkgname}-${pkgver}" < system-electron.patch
}

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    export PNPM_HOME="${srcdir}/pnpm-home"
    export PNPM_STORE_DIR="${srcdir}/pnpm-store"
    export CARGO_HOME="${srcdir}/cargo-home"
    export CARGO_TARGET_DIR="${srcdir}/cargo-target"
    export RUSTFLAGS="${RUSTFLAGS:-} --remap-path-prefix=${srcdir}=/usr/src/debug/${pkgname}"
    export MOTRIX_SKIP_ELECTRON_REBUILD=1
    export MOTRIX_SKIP_ENGINE_FETCH=1

    pnpm install --frozen-lockfile
    node node_modules/electron/install.js
    pnpm run fetch:engine --platform linux --arch x64
    pnpm run build:builtin
    pnpm run build:native-host -- --platform linux --arch x64
    pnpm run build:finalize-fs -- --platform linux --arch x64
    pnpm run build:electron
    pnpm run stage:electron -- --platform linux --arch x64
    rm -rf release
    pnpm exec electron-builder --linux dir --x64 --publish never
}

check() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    node scripts/verify-electron-package.mjs \
        --app-dir release/linux-unpacked \
        --platform linux \
        --arch x64 \
        --report "${srcdir}/electron-package-report.json"

    ELECTRON_RUN_AS_NODE=1 /usr/lib/electron44/electron \
        scripts/ensure-native-abi.mjs --probe
    ELECTRON_RUN_AS_NODE=1 /usr/lib/electron44/electron -e \
        "if (!process.versions.electron.startsWith('44.')) process.exit(1)"
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"

    install -d "${pkgdir}/usr/lib/${pkgname}"
    cp -r release/linux-unpacked/resources/. "${pkgdir}/usr/lib/${pkgname}/"
    rm -f \
        "${pkgdir}/usr/lib/${pkgname}/app-update.yml" \
        "${pkgdir}/usr/lib/${pkgname}/package-type"

    install -Dm755 "${srcdir}/motrix" "${pkgdir}/usr/bin/motrix"
    install -Dm644 "${srcdir}/motrix.desktop" \
        "${pkgdir}/usr/share/applications/motrix.desktop"
    install -Dm644 build/256x256.png \
        "${pkgdir}/usr/share/icons/hicolor/512x512/apps/motrix.png"
    install -Dm644 LICENSE \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
