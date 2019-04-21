# Maintainer: Kim Scarborough <sluggo@unknown.nu>

pkgname=vmware-keymaps
pkgver=1.0
pkgrel=1
pkgdesc="Keymaps required by some VMware packages"
arch=('any')
url="https://www.vmware.com/"
license=('custom:none')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/chowbok/${pkgname}/archive/master.tar.gz")
sha256sums=('cec825761cbd4ca7a682ff34f7a467f14439e1be0fb8f85aaa7a407fc96e177a')

package() {
	install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}"
	echo "The contents of this package are ineligible for copyright protection." > "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	install -dm755 "${pkgdir}/usr/lib/vmware/xkeymap"
	install -Dm644 "${srcdir}"/${pkgname}-master/* "${pkgdir}/usr/lib/vmware/xkeymap"
}
