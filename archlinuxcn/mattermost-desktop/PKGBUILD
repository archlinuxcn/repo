# Maintainer: William Gathoye <william + aur at gathoye dot be>
# Maintainer: Aleksandar Trifunović <akstrfn at gmail dot com>
# Contributor: Jan Was <janek dot jan at gmail dot com>
# Contributor: Bruno Pagani <archange at archlinux dot org>

pkgname=mattermost-desktop
pkgver=4.3.2
_electronMajorVersion=5
pkgrel=1
pkgdesc="Mattermost Desktop application for Linux"
arch=('i686' 'x86_64')
url="https://github.com/mattermost/desktop"
license=('Apache')
depends=("electron${_electronMajorVersion}")
makedepends=('npm' 'git' 'jq')
#optdepends=('hunspell: spell checking')
source=(
    "${pkgname}-${pkgver}.tar.gz"::"${url}/archive/${pkgver}.tar.gz"
    "${pkgname}.sh"
    "${pkgname/-/.}"
)
sha512sums=(
    '40e871e0699b1e0ba7670024a368498d7477b5716ff3523ab04bb9c1567bb577cfc220071f6d0228ec2b1fdfe4caeaeba859fe47faf47c76e8f0dd135ef3cf78'
    '717a463d47cee1e70f210a78c6d72f64e62de36921b5805888ec48ade0cd037a250567c677b1a39243af82144d556cb708d8d79eb0b13499e75d3dc4bf533d98'
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

    # Do not build tar.gz, nor .deb or appimages. This reduces build time.
    jq '.linux .target |= ["dir"]' \
        electron-builder.json > electron-builder-new.json
    # jq cannot output to the same file it get input from.
    mv electron-builder-new.json electron-builder.json

    # Prepend to system electron in order to avoid an unneeded download.
    local electronDist="/usr/lib/electron${_electronMajorVersion}"
    local electronVersion="$(<${electronDist}/version)"
    jq '{"electronDist": $electronDist, "electronVersion": $electronVersion} + .' \
        --arg electronDist "$electronDist" \
        --arg electronVersion "$electronVersion" \
        electron-builder.json > electron-builder-new.json
    mv electron-builder-new.json electron-builder.json

    # Mattermost Desktop is using simple-spellchecker which prevents to bind on
    # the system Arch Linux hunspell dictionnaries. This is due to the fact
    # simple-spellchecker comes with its own set of dictionnaries. They differ
    # from the hunspell dictionnaries in the sense of, hunspell's dictionnaries
    # have additional pieces of info attributed to each line.
    # e.g. in /usr/share/hunspell/fr_FR.dic, "ordinateur" (computer in English)
    # ordinateur/S*() po:nom is:mas
    # simple-spellcheck expects a line with:
    # ordinateur
    # instead
    #
    # Asking upstream to switch to electron-spellchecker will fix the issue.
    # https://github.com/electron-userland/electron-spellchecker

    # Install dependencies should be in prepare(), that way we don't need an
    # internet connection during build().
    # We don't need to run "npm run build" because that target is run by "npm
    # run package:linux" any way.
    npm install --cache "${srcdir}/npm-cache"
}

package() {
    cd "desktop-${pkgver}"
    npm run package:linux --cache "${srcdir}/npm-cache"

    install -d "${pkgdir}/usr/lib"
    # The wildcard in the unpackaged is needed for i686 or ARM platforms.
    install -Dm644 release/linux*unpacked/resources/app.asar "${pkgdir}/usr/lib/${pkgname}/app.asar"

    install -Dm644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm644 resources/linux/icon.svg "${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg"

    cd "${srcdir}"
    install -Dm755 ${pkgname}.sh "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 ${pkgname/-/.} -t "${pkgdir}/usr/share/applications/"
}

