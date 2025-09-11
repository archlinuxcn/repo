# Maintainer: CUI Hao <cuihao.leo@gmail.com>
# Contributor: dosenpils <dosenpils at donotdevelopmyapp dot com>
# Contributor: Alfredo Palhares <alfredo at palhares dot me>
# Contributor: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Matteo Parolari
# Contributor: gardar <aur@gardar.net>

pkgbase=joplin
pkgname=('joplin' 'joplin-desktop')
pkgdesc="A note taking and to-do application with synchronization capabilities"
pkgver=3.4.12
groups=('joplin')
pkgrel=1
_electronVersion=37
depends=("electron${_electronVersion}" "nodejs>20" "libvips")
optdepends=('libappindicator-gtk3: for tray icon')
arch=('x86_64')
makedepends=('npm' 'git' 'rsync' 'python-setuptools' 'libxcrypt-compat')
url="https://joplinapp.org/"
license=("AGPL-3.0-or-later")
source=(
    "joplin-desktop.sh"
    "joplin-desktop.desktop"
    "joplin-${pkgver}.tar.gz::https://github.com/laurent22/joplin/archive/v${pkgver}.tar.gz"
)
sha256sums=('9223cc816f8175ddaf8839f9357d2bd1c4831692504927c98d8e1eefa7df796e'
            'ff2232a2e518de7987af2a6d25524d75c2f7d1b343993b5134a341ae8f815dd5'
            'c00ac2540371543d85b4362fd716ff4748f18a61276d137cad91d318cd30f744')

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

    corepack install
    npx yarn install

    # Replace npm dependencies with local ones
    cd "packages"
    sed -i -E 's_"@joplin/(\w+)": .*_"@joplin/\1": "file://'$PWD'/\1",_g' */package.json

    # Pack the app-cli package
    cd "${srcdir}/joplin-${pkgver}/packages/app-cli"
    npx gulp build

    # Pack the app-desktop electron package
    cd "${srcdir}/joplin-${pkgver}/packages/app-desktop"
    npx gulp before-dist
    electronRoot=/usr/lib/electron${_electronVersion}/
    electronVersion="$(<${electronRoot}/version)"
    npx electron-builder \
      --linux --x64 --dir=dist/ \
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
    npm install -g --install-links --prefix "${pkgdir}/usr" *.tgz

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
    cp -vr dist/linux-unpacked/resources "${pkgdir}/usr/lib/${pkgname}"

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
