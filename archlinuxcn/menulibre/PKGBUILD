# Maintainer: Jonian Guveli <jonian@hardpixel.eu>
# Contributor: Evan Anderson <evananderson@thelinuxman.us>
# Contributor: Ner0

pkgname=menulibre
pkgver=2.4.0
pkgrel=1
epoch=1
pkgdesc="An advanced menu editor that provides modern features in a clean, easy-to-use interface"
arch=("any")
url="https://github.com/bluesabre/menulibre"
license=("GPL3")
depends=("gdk-pixbuf2" "gnome-menus" "gsettings-desktop-schemas" "gtksourceview3" "python" "python-gobject" "python-psutil" "python-xdg" "xdg-utils")
makedepends=("python-distutils-extra")
install=menulibre.install
source=("$pkgname-$pkgver.tar.gz::$url/releases/download/$pkgname-$pkgver/$pkgname-$pkgver.tar.gz")
md5sums=('b972469dc90394d3e43c7ee69a280770')

package() {
  cd "$pkgname-$pkgver" && python setup.py install --root="$pkgdir/" --optimize=1
}
