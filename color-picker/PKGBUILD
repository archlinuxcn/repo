# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=color-picker
pkgver=1.0.5
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
sha256sums_x86_64=('71590f01eabf102bf10e44c2310b6e3f4782a71e00f02cab015b7b1e3cbc0a97')

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
