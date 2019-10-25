# Maintainer: William Gathoye <william + aur at gathoye dot be>
# Maintainer: Aleksandar Trifunović <akstrfn at gmail dot com>
# Contributor: Jan Was <janek dot jan at gmail dot com>
# Contributor: Bruno Pagani <archange at archlinux dot org>

pkgname=mattermost-desktop
pkgver=4.3.1
pkgrel=1
pkgdesc="Mattermost Desktop application for Linux"
arch=('i686' 'x86_64')
url="https://github.com/mattermost/desktop"
license=('Apache')
depends=('electron')
makedepends=('npm' 'git')
source=(
    "${pkgname}-${pkgver}.tar.gz"::"${url}/archive/v${pkgver}.tar.gz"
    "${pkgname}.sh"
    "${pkgname/-/.}"
)
sha512sums=(
    '8e0a0c904db387dad872aca5430e38927d99445cb53f0afe5ccf0fb783ae53684bc40a338ccac3a78cc0bf578488cddf4580dbc76f131864bfc648667da97c05'
    '7cce5fad5a923fbde106d0e67ce42d599a2d21358eca3c339d5c9e0a19a0ac057bbf2db23f5ee3628d625afcd4b128b9b9041ace4f1892a0e1d2bbd0a9c677b9'
    'b8f24df883b71df4177155246fd5858ad785f75be4f7dfc674380674b48a45342b1f5ee217a20708f74ed8d2119d837bae4a3fd48d1b62d60d55644e36411266'
)

prepare() {
    cd "desktop-${pkgver}"

    # Depending on the architecture, in order to accelerate the build process,
    # removes the compilation of ia32 or x64 build.
    if [[ "$CARCH" == x86_64 ]];then
        sed -i 's/--ia32//g' package.json
    else
        sed -i 's/--x64//g' package.json
    fi

    # Reduce build time by removing the creation of a .deb for Debian and
    # AppImage
    sed -i -e '/"deb",/d' electron-builder.json
    sed -i -e '/"appimage"/d' electron-builder.json

    # No need to compress the package. Pay attention at the trailing comma: we
    # are removing it from the JSON to makeit valid again.
    sed -i 's/"tar.gz",/"dir"/' electron-builder.json
}

build() {
    cd "desktop-${pkgver}"
    npm install --cache "${srcdir}/npm-cache"
    npm run build --cache "${srcdir}/npm-cache"
}

package() {
    cd "desktop-${pkgver}"
    npm run package:linux --cache "${srcdir}/npm-cache"

    install -d "${pkgdir}/usr/lib"
    # The star in the unpackaged is needed for i686 or ARM platforms.
    cp -r release/linux*unpacked/resources "${pkgdir}/usr/lib/${pkgname}"

    install -Dm644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm644 resources/linux/icon.svg "${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg"

    cd "${srcdir}"
    install -Dm755 ${pkgname}.sh "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 ${pkgname/-/.} -t "${pkgdir}/usr/share/applications/"
}

