# Maintainer: CUI Hao <cuihao.leo@gmail.com>
# Contributor: dosenpils <dosenpils at donotdevelopmyapp dot com>
# Contributor: Alfredo Palhares <alfredo at palhares dot me>
# Contributor: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Matteo Parolari
# Contributor: gardar <aur@gardar.net>

pkgbase=joplin
pkgname=('joplin' 'joplin-desktop')
pkgdesc="A note taking and to-do application with synchronization capabilities"
pkgver=3.7.21
groups=('joplin')
pkgrel=1
_electronVersion=42
depends=("electron${_electronVersion}" "nodejs>=22" "libvips")
optdepends=('libappindicator-gtk3: for tray icon')
arch=('x86_64' 'aarch64')
makedepends=('npm' 'git' 'rsync' 'python-setuptools' 'libxcrypt-compat' 'corepack')
url="https://joplinapp.org/"
license=("AGPL-3.0-or-later")
source=(
    "joplin-desktop.sh"
    "joplin-desktop.desktop"
    "joplin-${pkgver}.tar.gz::https://github.com/laurent22/joplin/archive/v${pkgver}.tar.gz"
)
sha256sums=('3f87fe0167806c86495fab78483cce83d60262bc2289e5ff24a9a9039e8454b2'
            'fb9a5185e3b523a5f52b0eeec6def781782ad0e6b64e5db13300396b835a55b4'
            'd868a2f9a48937c514b6b39486e88f473b4477085035f75d22542800c1fdd083')

_setup_env() {
    export YARN_CACHE_FOLDER="${srcdir}/yarn-cache"
    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    #export npm_config_build_from_source=true
    export npm_config_yes=true
    export SHARP_IGNORE_GLOBAL_LIBVIPS=1
}

prepare() {
    _setup_env

    # Create the yarn cache folder
    mkdir -p "${YARN_CACHE_FOLDER}"

    cd "${srcdir}/joplin-${pkgver}"
}

build() {
    _setup_env

    cd "${srcdir}/joplin-${pkgver}"

    # Delete unused components
    rm -r packages/{app-mobile,app-clipper,server,doc-builder}
    # Fix: Build error due to removal of app-mobile
    sed -i '/app-mobile\//d' packages/tools/gulp/tasks/buildScriptIndexes.js
    # Fix: joplin-plugin-freehand-drawing complains "not in a git directory"
    git init
    # Fix: "Open secondary app instance" not working with system electron
    sed -i "s#bridge().electronApp().electronApp().getPath('exe')#'/usr/bin/joplin-desktop'#" \
        packages/app-desktop/bridge.ts
    sed -i '/const nextArg/a if (arg === "/usr/lib/joplin-desktop/app.asar") { argv.splice(0, 2); continue; }' \
        packages/lib/utils/processStartFlags.ts

    corepack install
    npx yarn install

    # Replace npm dependencies with local ones
    cd "packages"
    sed -i -E 's_"@joplin/([^"]+)": .*_"@joplin/\1": "file://'$PWD'/\1",_g' */package.json

    # Pack the app-cli package
    cd "${srcdir}/joplin-${pkgver}/packages/app-cli"
    npx gulp build
    # Fix: MODULE_NOT_FOUND error in tests after commit 25a93ff
    ln -s ../build app/build

    # Pack the app-desktop electron package
    cd "${srcdir}/joplin-${pkgver}/packages/app-desktop"
    npx gulp before-dist
    electronRoot=/usr/lib/electron${_electronVersion}/
    electronVersion="$(<${electronRoot}/version)"
    arch_args="--x64"
    if [[ $CARCH == "aarch64" ]]; then
        arch_args="--arm64"
    fi
    npx electron-builder \
      --linux "$arch_args" --dir=dist/ \
      -c.electronDist="${electronRoot}" \
      -c.electronVersion="${electronVersion}"
}

check() {
    _setup_env

    cd "${srcdir}/joplin-${pkgver}"

    env ELECTRON_OVERRIDE_DIST_PATH=/usr/lib/electron${_electronVersion}/ \
        TZ=UTC \
        npx yarn workspaces foreach -Rptiv --from 'joplin' --from '@joplin/app-desktop' run test
}

package_joplin() {
    pkgdesc="A note taking and to-do application with synchronization capabilities - CLI App"
    depends=('nodejs')
    optdepends=( )

    _setup_env

    # Install the package
    cd "${srcdir}/joplin-${pkgver}/packages/app-cli/build"
    npm pack
    npm install -g --install-links --prefix "${pkgdir}/usr" \
        --allow-scripts=keytar,sharp,sqlite3 \
        *.tgz

    # Fix permissions set by npm
    chown -R root:root "${pkgdir}"
}

package_joplin-desktop() {
    pkgdesc="A note taking and to-do application with synchronization capabilities - Desktop"
    depends=("electron${_electronVersion}" "nodejs" "libvips")
    optdepends=('libappindicator-gtk3: for tray icon')

    _setup_env

    cd "${srcdir}/joplin-${pkgver}/packages/app-desktop"
    mkdir -p "${pkgdir}/usr/lib"
    if [[ "$CARCH" == "aarch64" ]]; then
        cp -vr dist/linux-arm64-unpacked/resources "${pkgdir}/usr/lib/${pkgname}"
    else
        cp -vr dist/linux-unpacked/resources "${pkgdir}/usr/lib/${pkgname}"
    fi

    # Install icons
    while read -r size; do
        mkdir -p "${pkgdir}/usr/share/icons/hicolor/${size}/apps/"
        cp "${pkgdir}/usr/lib/${pkgname}/build/icons/${size}.png" \
           "${pkgdir}/usr/share/icons/hicolor/${size}/apps/${pkgname}.png"
    done < <(ls build/icons | grep -Po '^(\d+)x\1+(?=\.png)')

    install -vDm644 "${srcdir}/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications"
    install -vDm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
    sed -i "s|@electronversion@|${_electronVersion}|" "${pkgdir}/usr/bin/${pkgname}"
}
