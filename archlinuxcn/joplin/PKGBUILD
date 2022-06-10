pkgbase=joplin
pkgname=('joplin' 'joplin-desktop')
pkgver=2.8.8
groups=('joplin')
pkgrel=1
_electronVersion=17
depends=("electron${_electronVersion}" "nodejs")
optdepends=('libappindicator-gtk3: for tray icon')
arch=('x86_64')
makedepends=('npm' 'git' 'rsync' 'yarn' 'python2')
url="https://joplinapp.org/"
license=('MIT')
source=(
    "joplin-desktop.sh"
    "joplin-desktop.desktop"
    "joplin-${pkgver}.tar.gz::https://github.com/laurent22/joplin/archive/v${pkgver}.tar.gz"
)
sha256sums=(
    'SKIP'
    'SKIP'
    'b6e0a3a5d59882de37494c0b3b1d28df407e86d06e81bc8201cb912e2711949b'
)

_setup_env() {
    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    export npm_config_build_from_source=true
    export npm_config_python=/usr/bin/python2
}

prepare() {
    cd "${srcdir}/joplin-${pkgver}"

    # Disable useless dependencies
    sed -i '/"7zip-bin-.*": ".*"/d' package.json packages/*/package.json
    sed -i '/"husky": ".*"/d' package.json packages/*/package.json

    # Delete unused components
    rm -r "packages/app-mobile" "packages/app-clipper" "packages/server"
}

build() {
    cd "${srcdir}/joplin-${pkgver}"
    _setup_env
    yarn install
}

package_joplin() {
    pkgdesc="A note taking and to-do application with synchronization capabilities - CLI App"
    depends=('nodejs')

    cd "${srcdir}/joplin-${pkgver}/packages"
    _setup_env

    package_files=()

    for package in fork-htmlparser2 fork-sax fork-uslug htmlpack renderer turndown turndown-plugin-gfm lib; do
        ( cd "${package}" && npm pack )
        package_files+=("$(realpath "${package}/"*.tgz)")
    done

    cd app-cli && npx gulp build && cd build && npm pack && cd ../..
    package_files+=("$(realpath "app-cli/build/"*.tgz)")

    npm install -g --prefix "${pkgdir}/usr" "${package_files[@]}"

    # Fix permissions set by npm
    chown -R root:root "${pkgdir}"
}

package_joplin-desktop() {
    pkgdesc="A note taking and to-do application with synchronization capabilities - Desktop"
    depends=('electron17' 'nodejs')
    optdepends=('libappindicator-gtk3: for tray icon')

    cd "${srcdir}/joplin-${pkgver}/packages/app-desktop"

    electronRoot=/usr/lib/electron${_electronVersion}/
    electronVersion="$(<${electronRoot}/version)"

    npx electron-builder \
      --linux --x64 --dir=dist/ \
      -c.electronDist="${electronRoot}" \
      -c.electronVersion="${electronVersion}"

    install -vDm644 dist/linux-unpacked/resources/app.asar -t "${pkgdir}/usr/lib/${pkgname}"
    cp -vr build -t "${pkgdir}/usr/lib/${pkgname}"
    cp -vr dist/linux-unpacked/resources/app.asar.unpacked -t "${pkgdir}/usr/lib/${pkgname}"

    while read -r size; do
        mkdir -p "${pkgdir}/usr/share/icons/hicolor/${size}/apps/"
        cp "${pkgdir}/usr/lib/${pkgname}/build/icons/${size}.png" \
           "${pkgdir}/usr/share/icons/hicolor/${size}/apps/${pkgname}.png"
    done < <(ls build/icons | grep -Po '^(\d+)x\1+(?=\.png)')

    install -vDm644 "${srcdir}/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications"
    install -vDm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
    sed -i "s|@electronversion@|${_electronVersion}|" "${pkgdir}/usr/bin/${pkgname}"
}
