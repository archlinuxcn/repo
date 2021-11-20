# Maintainer: Piotr Miller <nwg.piotr@gmail.com>
pkgname=('nwg-launchers')
pkgver=0.6.3
pkgrel=1
pkgdesc="GTK+ launchers for sway, i3 and some other WMs"
arch=('x86_64')
url="https://github.com/nwg-piotr/nwg-launchers"
license=('GPL3')
makedepends=('git' 'meson')
depends=('gtk3' 'gtkmm3' 'nlohmann-json')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
md5sums=('3891f7f38207cc61370884cef46ce4b2')

build() {
   cd "$srcdir/$pkgname-${pkgver}"
   meson builddir -Dbuildtype=release -Dprefix=/usr
   ninja -C builddir
}

package() {
   cd "$srcdir/$pkgname-${pkgver}"
   DESTDIR="$pkgdir" ninja -C builddir install
}

