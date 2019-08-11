# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=grub-theme-stylish-git
_pkgname="${pkgname%-*}"
pkgver=1.0
pkgrel=2
pkgdesc="Stylish grub theme"
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
    install -d "$pkgdir/usr/share/grub/themes/$name"
    install -d "$pkgdir/usr/share/grub/themes/$name/icons"
    install -Dm 644 common/* "$pkgdir/usr/share/grub/themes/$name"
    install -Dm 644 "backgrounds/background-${_pkgname##*-}.jpg" "$pkgdir/usr/share/grub/themes/$name/background.jpg"
    install -Dm 644 assets/assets-white/icons/* "$pkgdir/usr/share/grub/themes/$name/icons"
    install -Dm 644 assets/assets-white/select/*.png "$pkgdir/usr/share/grub/themes/$name"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$_pkgname/LICENSE"
}
