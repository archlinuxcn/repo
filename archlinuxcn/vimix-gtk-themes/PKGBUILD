# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=vimix-gtk-themes
_pkgver=2023-09-09
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A flat Material Design theme for GTK 3, GTK 2, GNOME Shell, etc."
arch=('any')
url="https://vinceliuice.github.io/theme-vimix.html"
license=('GPL3')
makedepends=('sassc')
optdepends=('gtk-engine-murrine: GTK2 theme support'
            'gtk-engines: GTK2 theme support'
            'kvantum-theme-vimix: Matching Kvantum theme'
            'vimix-icon-theme: Matching icon theme'
            'vimix-cursors: Matching cursor theme')
options=('!strip')
install="$pkgname.install"
source=("$pkgname-$_pkgver.tar.gz::https://github.com/vinceliuice/vimix-gtk-themes/archive/$_pkgver.tar.gz")
sha256sums=('4f865b79d35abd459c9b9f0022ca0330539442761c5e667ae8b5c2cec44dccd0')

package() {
  cd "$pkgname-$_pkgver"
  install -d "$pkgdir/usr/share/themes"
  ./install.sh -t all -s all -d "$pkgdir/usr/share/themes"
}
