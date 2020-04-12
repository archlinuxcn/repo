# Maintainer: Romain GERARD <erebe@erebe.eu>

pkgname=rofi-greenclip
pkgver=3.3
pkgrel=1
pkgdesc="Clipboard manager to use with rofi - Image support and blacklist"
arch=('x86_64')
url="https://github.com/erebe/greenclip"
license=('GPL')
groups=()
changelog=changelog
depends=('rofi')
makedepends=()
checkdepends=()
optdepends=()
provides=("greenclip")
conflicts=("rofi-greenclip-beta")
replaces=("rofi-greenclip-beta")
backup=()
options=('!strip')
source=("https://github.com/erebe/greenclip/releases/download/3.3/greenclip"
        "greenclip.service")
noextract=()
sha256sums=('392d43e0caebf39f2124959177c74f3a152c9143d4c2e0e005d7cf2b1e32a58c'
            '85ecca9b6f5903ee53615c09802efd389662ddba7ce1febe34302a6a1d87179e')

package() {
        install -Dm755 greenclip "$pkgdir/usr/bin/greenclip"
        install -Dm644 "$srcdir/greenclip.service" "$pkgdir/usr/lib/systemd/user/greenclip.service"
}

