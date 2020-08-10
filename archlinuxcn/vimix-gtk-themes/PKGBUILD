# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=vimix-gtk-themes
_pkgver=2020-02-24
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A flat Material Design theme for GTK 3, GTK 2, GNOME Shell, etc."
arch=('any')
url="https://vinceliuice.github.io/theme-vimix.html"
license=('GPL3')
depends=('gtk3' 'gtk-engine-murrine' 'gtk-engines')
optdepends=('kvantum-theme-vimix: Matching Kvantum theme'
            'vimix-icon-theme: Matching icon theme'
            'vimix-cursors: Matching cursor theme'
            'tela-icon-theme: Recommended icon theme')
conflicts=('vimix-gtk-themes-git')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::https://github.com/vinceliuice/$pkgname/archive/$_pkgver.tar.gz")
sha256sums=('5630d7bfb09820978459b2ce2f7db6cacbb2a34a4c8f73ca3b706301310927bd')

package() {
	cd "$pkgname-$_pkgver"
	install -dm755 "$pkgdir/usr/share/themes"
	./install.sh -d "$pkgdir/usr/share/themes"
}
