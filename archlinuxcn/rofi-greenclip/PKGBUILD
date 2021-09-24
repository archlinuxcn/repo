# Maintainer: Romain GERARD <erebe@erebe.eu>

pkgname=rofi-greenclip
pkgver=4.2
pkgrel=2
pkgdesc="Clipboard manager to use with rofi - Image support and blacklist"
arch=('x86_64')
url="https://github.com/erebe/greenclip"
license=('GPL')
groups=()
changelog=changelog
depends=()
makedepends=()
checkdepends=()
optdepends=('rofi' 'fzf' 'dmenu')
provides=("greenclip")
conflicts=("rofi-greenclip-beta")
replaces=("rofi-greenclip-beta")
backup=()
options=('!strip')
source=("https://github.com/erebe/greenclip/releases/download/v4.2/greenclip-v4.2"
        "greenclip.service")
noextract=()
sha256sums=('80b189fc9ce2e0a56e33be642875f5c3fb53647465f8024a541621307a6a290f'
            '85ecca9b6f5903ee53615c09802efd389662ddba7ce1febe34302a6a1d87179e')

package() {
        install -Dm755 greenclip-v4.2 "$pkgdir/usr/bin/greenclip"
        install -Dm644 "$srcdir/greenclip.service" "$pkgdir/usr/lib/systemd/user/greenclip.service"
}

