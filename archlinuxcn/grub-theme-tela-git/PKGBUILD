# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=grub-theme-tela-git
_pkgname="${pkgname%-*}"
pkgver=1.0
pkgrel=1
pkgdesc="Tela grub theme"
arch=(any)
url="https://github.com/vinceliuice/grub2-themes"
license=('GPL3')
depends=(grub)
makedepends=(git)
provides=("$_pkgname")
conflicts=("$_pkgname")
source=("$_pkgname::git+https://github.com/vinceliuice/grub2-themes.git")
md5sums=(SKIP)

pkgver() {
    cd "$srcdir/$_pkgname"
    git log -1 --format='%cd' --date=short | tr -d -- '-'
}

package() {
    name="${pkgdesc%% *}"
    cd "$srcdir/$_pkgname"
    install -d "$pkgdir/boot/grub/themes/$name"
    install -d "$pkgdir/boot/grub/themes/$name/icons"
    install -Dm 755 common/* "$pkgdir/boot/grub/themes/$name"
    install -Dm 755 "backgrounds/background-${_pkgname##*-}.jpg" "$pkgdir/boot/grub/themes/$name/background.jpg"
    install -Dm 755 assets/assets-tela/icons/* "$pkgdir/boot/grub/themes/$name/icons"
    install -Dm 755 assets/assets-tela/select/*.png "$pkgdir/boot/grub/themes/$name"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
}
