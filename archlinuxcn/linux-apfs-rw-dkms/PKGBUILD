# Maintainer: Integral <integral@member.fsf.org>

pkgname=linux-apfs-rw-dkms
_pkgname=${pkgname%-dkms}
epoch=1
pkgver=0.3.13
pkgrel=1
pkgdesc="Experimental APFS kernel module with Write support (DKMS)"
arch=('any')
url="https://github.com/linux-apfs/${_pkgname}"
license=('GPL-2.0-only')
depends=('dkms')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('1272c0441c6810cb7096038ed8990daa05c317175b1d2bbfd6780784eb71aebb')

package() {
	local dkms_dir="${pkgdir}/usr/src/${_pkgname}-${pkgver}/"
	install -d "${dkms_dir}"
	cp -r ${_pkgname}-${pkgver}/* "${dkms_dir}"
}
