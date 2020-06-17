# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Maintainer: William Gathoye <william + aur at gathoye dot be>
# Contributor: Aleksandar Trifunović <akstrfn at gmail dot com>
# Contributor: Jan Was <janek dot jan at gmail dot com>
# Contributor: Bruno Pagani <archange at archlinux dot org>

pkgname=mattermost-desktop
pkgver=4.5.0
pkgrel=1
pkgdesc='Mattermost Desktop application for Linux'
arch=('x86_64' 'i686')
url="https://github.com/${pkgname/-//}"
license=('Apache')
depends=('electron7')
makedepends=('git' 'jq' 'npm')
#optdepends=('hunspell: spell checking')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        "$pkgname.sh"
        "${pkgname/-/.}")
sha256sums=('faffabce7c5e8e606a8e0d66136d65131d3de46e54edabbccdc16494dca530e6'
            '0f18f87764465f1fc5a9fdfb6ef2834af4623c13bc95fce58da6cb0d8d39a75e'
            'e628268d3393aac0d5b7237c6b8818d2e362c373f99874a19171bf96a25e4ffa')

prepare() {
    cd "desktop-$pkgver"

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
    local electronDist="/usr/lib/electron7"
    local electronVersion="$(<"$electronDist"/version)"
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
    npm install --cache "$srcdir/npm-cache"
}

package() {
    cd "desktop-$pkgver"
    npm run package:linux --cache "$srcdir/npm-cache"

    install -d "$pkgdir/usr/lib"
    # The wildcard in the unpackaged is needed for i686 or ARM platforms.
    install -Dm644 release/linux*unpacked/resources/app.asar "$pkgdir/usr/lib/$pkgname/app.asar"

    install -Dm644 LICENSE.txt -t "$pkgdir/usr/share/licenses/$pkgname"
    install -Dm644 resources/linux/icon.svg "$pkgdir/usr/share/icons/hicolor/scalable/apps/$pkgname.svg"

    cd "$srcdir"
    install -Dm755 "$pkgname".sh "$pkgdir/usr/bin/$pkgname"
    install -Dm644 "${pkgname/-/.}" -t "$pkgdir/usr/share/applications/"
}
