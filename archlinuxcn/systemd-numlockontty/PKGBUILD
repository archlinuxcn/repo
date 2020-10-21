# Maintainer: Ybalrid <ybalrid@ybalrid.org>
# Contributor: X0rg

pkgname=systemd-numlockontty
pkgver=0.1
pkgrel=12
pkgdesc="Systemd service + script, automatically activate numpad on ttys"
arch=('any')
url="http://percival.ybalrid.info/aur/numlockontty.html"
depends=('systemd')
replaces=('numlockontty')
license=('GPL')
install=numlockontty.install
source=("http://percival.ybalrid.info/aur/numlockontty-$pkgver.tar.gz")
md5sums=('f7b69626dd83f5da5269b226688ff1b8')

package() {
	install -Dvm755 "$srcdir/numlockOnTty"		 "$pkgdir/usr/bin/numlockOnTty"
	install -Dvm644 "$srcdir/numLockOnTty.service"	 "$pkgdir/usr/lib/systemd/system/numLockOnTty.service"
}
