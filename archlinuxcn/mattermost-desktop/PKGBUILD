# Maintainer: William Gathoye <william at gathoye dot be>
# Maintainer: Aleksandar Trifunović <akstrfn at gmail dot com>
# Contributor: Jan Was <janek dot jan at gmail dot com>
# Contributor: Bruno Pagani <archange at archlinux dot org>

pkgname=mattermost-desktop
pkgver=4.2.1
pkgrel=2
pkgdesc="Mattermost Desktop application for Linux (Beta)"
arch=('i686' 'x86_64')
url="https://github.com/mattermost/desktop"
license=('Apache')
depends=('electron4')
makedepends=('npm' 'git')
source=(
    "${pkgname}-${pkgver}.tar.gz"::"${url}/archive/v${pkgver}.tar.gz"
    "${pkgname}.sh"
    "${pkgname/-/.}"
    "${pkgname%%-*}-package-json.patch"
    "https://github.com/mattermost/desktop/commit/40257cf93e153a84a94f888aea3225788fbb9d3a.patch"
)
sha512sums=('54484871cdeb52f70241b6f154215f7aaeaa0aac0abae4293e19988032e18a50fa1744dbecab5ce333c35f4ba151434101b68f49c7a256cd3aaf70395fc94afb'
            'ec10960a56593429996f153d0832345d1f9279aa386d5d09f078aed39a5e8e4c3d1900fc8ff608318c9c57a161c3850b2c7924d86af0ae41f76649c080fccc1f'
            'a8db88c1db7cba497ee2a1db059430d235942052322b26a2ece7a1340a28ae24686630fa89a37fcfa6bf9f277cbf8a7018ce78e7117b247b2b408fa0fb709d84'
            '09605ae4d5b6fe895f1ca9904984393ea7e2a3c08ca519e270d3d26fa0b14ae353c374bfd5917055f7fa3034f33a428e5bcd9b6c70c64dcbdf106a1733de023a'
            'beb984681a1a381de59e6eb3b5dc65a8fbffe3f4a14bf9568f4b18c7394d45c449386a033de34ea625e59b17b7a85273040ea86472455ff2ce177d0b12ff9ea1')

prepare() {
    cd "desktop-${pkgver}"

    # Bump dependencies. Temporary patch. Remove when 4.3 is out.
    patch < "${srcdir}"/mattermost-package-json.patch
    patch -p1 < "${srcdir}"/40257cf93e153a84a94f888aea3225788fbb9d3a.patch

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

