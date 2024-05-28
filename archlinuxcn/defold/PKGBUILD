# Maintainer: Asakura Mizu <asakuramizu111@gmail.com>
pkgname=defold
pkgver=1.8.0.r33118cd
pkgrel=1
epoch=
pkgdesc='Defold is a completely free to use game engine for development of desktop, mobile and web games.'
arch=('x86_64')
url='https://defold.com/'
license=('custom')
groups=()
depends=('glu')
makedepends=('gendesk' 'curl' 'jq')
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
validpgpkeys=()
source=('LICENSE'
    'logo.zip')
sha256sums=('be6e9921ba01445d200ba3dc09b5cab149a58d57a76ca98376b52af87d817a7a'
    '3b8caea5c51ed35d0b192b621e55102c7336904d5bc096d801cbbe700ebf17ca')

prepare() {
    cd "$srcdir"

    curl -O https://d.defold.com/editor-alpha/info.json
    _sha1=$(cat info.json | jq -r '.sha1')
    curl -O "https://d.defold.com/archive/editor-alpha/${_sha1}/editor-alpha/editor2/Defold-x86_64-linux.zip"

    gendesk -f -n --pkgname "$pkgname" --pkgdesc "$pkgdesc" --path /opt/Defold --name Defold --exec /opt/Defold/Defold --categories "Game;Development;Utility"
}

pkgver() {
    cd "$srcdir"

    _version=$(cat info.json | jq -r '.version')
    _sha1=$(cat info.json | jq -r '.sha1')
    echo "${_version}.r${_sha1:0:7}"
}

package() {
    cd "$srcdir"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 defold.desktop "$pkgdir/usr/share/applications/defold.desktop"
    install -Dm644 "logo/64.png" "$pkgdir/usr/share/icons/hicolor/64x64/apps/defold.png"
    install -Dm644 "logo/128.png" "$pkgdir/usr/share/icons/hicolor/128x128/apps/defold.png"
    install -Dm644 "logo/150.png" "$pkgdir/usr/share/icons/hicolor/150x150/apps/defold.png"
    install -Dm644 "logo/310.png" "$pkgdir/usr/share/icons/hicolor/310x310/apps/defold.png"
    install -Dm644 "logo/1024.png" "$pkgdir/usr/share/icons/hicolor/1024x1024/apps/defold.png"
    mkdir -p "$pkgdir/opt"
    bsdtar -xf Defold-x86_64-linux.zip -C "$pkgdir/opt"
}
