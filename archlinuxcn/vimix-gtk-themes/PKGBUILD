# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=vimix-gtk-themes
_pkgver=2024-04-20
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A flat Material Design theme for GTK 3, GTK 2, GNOME Shell, etc."
arch=('any')
url="https://vinceliuice.github.io/theme-vimix.html"
license=('GPL-3.0-or-later')
makedepends=('sassc')
optdepends=('gtk-engine-murrine: GTK2 theme support'
            'gtk-engines: GTK2 theme support'
            'kvantum-theme-vimix: Matching Kvantum theme'
            'vimix-icon-theme: Matching icon theme'
            'vimix-cursors: Matching cursor theme')
options=('!strip')
install="$pkgname.install"
source=("$pkgname-$_pkgver.tar.gz::https://github.com/vinceliuice/vimix-gtk-themes/archive/$_pkgver.tar.gz")
sha256sums=('dd64d7a3d6b49f5a51290d93af41c0031943e3ff1edb8739ee13ad4593212059')

package() {
  cd "$pkgname-$_pkgver"
  install -d "$pkgdir/usr/share/themes"
  ./install.sh -t all -s all -d "$pkgdir/usr/share/themes"
}
