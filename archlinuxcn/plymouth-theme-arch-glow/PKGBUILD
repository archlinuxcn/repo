# Maintainer: Shayne Hartford <shayneehartford@gmail.com>

pkgname=plymouth-theme-arch-glow
pkgver=167535
pkgrel=1
pkgdesc="This is a simple Plymouth theme displaying the Arch Linux logo."
arch=('any')
url="https://store.kde.org/p/1000032/"
license=('CCPL:cc-by-3.0')
depends=('plymouth')
source=("arch-glow.tar.gz")
sha256sums=('781e3eb6409ecde3944c1144329ae08b7de661b0ead53a6986a9d87919e1ec33')

package() {
	cd $srcdir/arch-glow

	mkdir -p $pkgdir/usr/share/plymouth/themes/arch-glow
	install -Dm644 * $pkgdir/usr/share/plymouth/themes/arch-glow
}
