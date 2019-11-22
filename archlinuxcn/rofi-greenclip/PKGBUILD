# Maintainer: Romain GERARD <erebe@erebe.eu>

pkgname=rofi-greenclip
pkgver=3.2
pkgrel=3
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
source=("https://github.com/erebe/greenclip/releases/download/3.2/greenclip"
        "greenclip.service")
noextract=()
sha256sums=('18447e96c1fb0afebaa42507e59a2780fc4fdb2e88a44e84421cd1727648c443'
            'a5b84a8137aed68ab06d0d38cf1f4c705ce283f300d430b0c6e2d0fd13d1ddd0')

package() {
        install -Dm755 greenclip "$pkgdir/usr/bin/greenclip"
        install -Dm644 "$srcdir/greenclip.service" "$pkgdir/usr/lib/systemd/user/greenclip.service"
}

