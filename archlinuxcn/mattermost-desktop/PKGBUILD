# Maintainer: William Gathoye <william at gathoye dot be>
# Maintainer: Aleksandar Trifunović <akstrfn at gmail dot com>
# Contributor: Jan Was <janek dot jan at gmail dot com>
# Contributor: Bruno Pagani <archange at archlinux dot org>

pkgname=mattermost-desktop
pkgver=4.2.0
pkgrel=1
pkgdesc="Mattermost Desktop application for Linux (Beta)"
arch=('i686' 'x86_64')
url="https://github.com/mattermost/desktop"
license=('Apache')
depends=('electron')
makedepends=('npm' 'git')
source=(
    "${pkgname}-${pkgver}.tar.gz"::"${url}/archive/v${pkgver}.tar.gz"
    "${pkgname}.sh"
    "${pkgname/-/.}"
    "${pkgname%%-*}-package-json.patch"
)
sha512sums=(
    '45a6f1c97569fb503a319cd3766000fb8928bbb7de699751dd3d725876ddc31b72ed057ebda2f25e4369e9d940a687e7eb7fcb5dc8522a0c5857f02d6bf961bf'
    'a36e5c26458a1166595b9858d2f8d40213bf7a177d86eaec1398167fbc87bcae7c3dc9416db0409b4cf4742eb497af139e2a552cdc3f1f9f9ae33f985a8511d8'
    'a8db88c1db7cba497ee2a1db059430d235942052322b26a2ece7a1340a28ae24686630fa89a37fcfa6bf9f277cbf8a7018ce78e7117b247b2b408fa0fb709d84'
    '09605ae4d5b6fe895f1ca9904984393ea7e2a3c08ca519e270d3d26fa0b14ae353c374bfd5917055f7fa3034f33a428e5bcd9b6c70c64dcbdf106a1733de023a'
)

prepare() {
    cd "desktop-${pkgver}"

    # Bump dependencies. Temporary patch. Remove when 4.3 is out.
    patch < "${srcdir}"/mattermost-package-json.patch

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

