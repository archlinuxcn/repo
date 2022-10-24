# Maintainer: Ybalrid <ybalrid@ybalrid.org>
# Contributor: X0rg

pkgname=systemd-numlockontty
pkgver=0.1
pkgrel=14
pkgdesc="Systemd service + script, automatically activate numpad on ttys"
arch=('any')
url="http://percival.ybalrid.info/aur/numlockontty.html"
depends=('systemd')
replaces=('numlockontty')
license=('GPL')
install=numlockontty.install
source=("https://github.com/Ybalrid/systemd-numlockontty/releases/download/$pkgver-$pkgrel/numlockontty-$pkgver.tar.gz")
md5sums=('65569e3b4a2240c3bd5dfe02414e33da')

package() {
	install -Dvm755 "$srcdir/numlockOnTty"		 "$pkgdir/usr/bin/numlockOnTty"
	install -Dvm644 "$srcdir/numlockOnTty.service"	 "$pkgdir/usr/lib/systemd/system/numLockOnTty.service"
}
