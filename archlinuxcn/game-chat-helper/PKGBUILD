# Maintainer: Dct Mei <dctxmei@gmail.com>
pkgname=game-chat-helper
pkgver=1.0
pkgrel=1
pkgdesc="Game chat helper with IME (Chinese, Japanese, Korean) support"
arch=('any')
url="https://github.com/dctxmei/game-chat-helper"
license=('MIT')
depends=("zenity" "xdotool" "xdotool")
makedepends=('git')
source=("git://github.com/dctxmei/$pkgname.git")
sha512sums=("SKIP")

pkgver() {
    cd "$srcdir/$pkgname"
    git log -1 --format="%cd" --date=short | sed 's/-//g'
}

package() {
    install -Dm755 "$srcdir/$pkgname/$pkgname.sh" "$pkgdir/usr/bin/$pkgname"
}
