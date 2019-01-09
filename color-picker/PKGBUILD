# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=color-picker
pkgver=1.1.2
pkgrel=1
pkgdesc="A color picker for elementary OS."
arch=('x86_64')
depends=('granite')
makedepends=('meson' 'vala')
conflicts=("color-picker-git")
provides=("color-picker")
url="https://github.com/RonnyDo/ColorPicker"
license=("GPL3")
source=("https://raw.githubusercontent.com/RonnyDo/ColorPicker/master/LICENSE")
source_x86_64=("ColorPicker-$pkgver.tar.gz::https://github.com/RonnyDo/ColorPicker/archive/$pkgver.tar.gz")

sha256sums=('589ed823e9a84c56feb95ac58e7cf384626b9cbf4fda2a907bc36e103de1bad2')
sha256sums_x86_64=('9b17b78cffedad22e675e13f7c008aef65872455f1efadbc8826d09b20dc8812')

build() {
    cd $srcdir/ColorPicker-$pkgver
    meson _build --prefix=/usr
    cd _build
    ninja
}

package() {
    install -Dm755 LICENSE ${pkgdir}/usr/share/licenses/$pkgname/LICENSE
    cd $srcdir/ColorPicker-$pkgver/_build
    DESTDIR="$pkgdir/" ninja install
}
