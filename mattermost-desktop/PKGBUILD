# Maintainer: William Gathoye <william at gathoye dot be>
# Maintainer: Aleksandar Trifunović <akstrfn at gmail dot com>
# Contributor: Jan Was <janek dot jan at gmail dot com>
# Contributor: Bruno Pagani <archange at archlinux dot org>

pkgname=mattermost-desktop
pkgver=4.1.2
pkgrel=2
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
)
sha512sums=(
    'd43f4adab5310a5f37bd2fcf4788af71a81ed4b384013be9a71643629ca15b9f36a2dfd77294673597a750eb8539ca9a96ad892ddb0a92290b2648ed96967c12'
    'a36e5c26458a1166595b9858d2f8d40213bf7a177d86eaec1398167fbc87bcae7c3dc9416db0409b4cf4742eb497af139e2a552cdc3f1f9f9ae33f985a8511d8'
    'a8db88c1db7cba497ee2a1db059430d235942052322b26a2ece7a1340a28ae24686630fa89a37fcfa6bf9f277cbf8a7018ce78e7117b247b2b408fa0fb709d84'
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

    # Reduce build time by removing the creation of a .deb for Debian
    sed -i -e '/"deb",/d' electron-builder.json
    # No need to compress the package
    sed -i 's/tar.gz/dir/' electron-builder.json
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
    # SVG icon available in next release
    # install -Dm644 resources/linux/icon.svg "${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg"
    install -Dm644 resources/linux/icon.png "${pkgdir}/usr/share/icons/hicolor/512x512/apps/${pkgname}.png"

    cd "${srcdir}"
    install -Dm755 ${pkgname}.sh "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 ${pkgname/-/.} -t "${pkgdir}/usr/share/applications/"
}

