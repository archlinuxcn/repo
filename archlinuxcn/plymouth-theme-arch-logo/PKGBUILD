# Maintainer: Manuel Hüsers <manuel.huesers@uni-ol.de>
# Contributor: Manuel Hüsers <manuel.huesers@uni-ol.de>
# Contributor: Guillermo Garcia <ahioros@NO-SPAM.gmail.com>

pkgname=plymouth-theme-arch-logo
pkgver=1
pkgrel=2
pkgdesc='A remake of the ubuntu-logo Plymouth theme, based on the debian-logo theme, but featuring the Arch Linux logo.'
arch=('any')
# Alternative website(s)
#url='http://karlinux.deviantart.com/art/Arch-Logo-Plymouth-Theme-209553250'
url='https://www.gnome-look.org/content/show.php/Arch-logo+plymouth?content=141697'
license=('GPL')
depends=('plymouth')
install="${pkgname}.install"
source=(
	'plymouth-theme-arch-logo.tar.gz'
)
sha256sums=(
	'553ab3efd51abefc50c10b521c24183df9ef879d080a75c54fb1c1512fbc94e6'
)

package() {
	cd "${srcdir}/arch-logo"
	rm -fv *~
	mkdir -p "${pkgdir}/usr/share/plymouth/themes/arch-logo"
	install -Dvm644 * "${pkgdir}/usr/share/plymouth/themes/arch-logo"
}
