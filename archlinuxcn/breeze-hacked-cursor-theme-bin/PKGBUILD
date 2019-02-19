# Maintainer: Dct Mei <dctxmei@gmail.com>
# Maintainer: Jeremy Pope <jpope at jpope dot org> PGP-Key: E00B4261
pkgname=breeze-hacked-cursor-theme-bin
pkgver=2.0
pkgrel=6
pkgdesc="Breeze Hacked cursor theme"
arch=("any")
url="https://kver.wordpress.com/2015/01/09/curses-i-mean-cursors/"
license=("GPL")
makedepends=("gnome-themes-extra" "inkscape" "xorg-xcursorgen")
provides=("breeze-hacked-cursor-theme")
conflicts=("breeze-hacked-cursor-theme")
source=("https://downloads.dctxmei.me/plasma-cursors-breeze_hacked.source-2.0-kvermette.zip")
sha512sums=("08b29793bf6e8ea0579e1d3f882f330e16f10893bfaa2d05688825fc5cf48c1f921ce0fcc3f6c082ab8f3b085c878bd4c4e2a6007bdcee08093e9f275c43c080")

build() {
    cd $srcdir/Breeze_Hacked
    ./build.sh
}

package() {
    cd $srcdir/Breeze_Hacked/Breeze_Hacked
    install -d $pkgdir/usr/share/icons/Breeze_Hacked
    cp -rf * $pkgdir/usr/share/icons/Breeze_Hacked
    chmod -R 644 $pkgdir/usr/share/icons/Breeze_Hacked/*
    chmod 755 $pkgdir/usr/share/icons/Breeze_Hacked
    chmod 755 $pkgdir/usr/share/icons/Breeze_Hacked/cursors
}
