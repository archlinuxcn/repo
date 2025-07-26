# Maintainer: Integral <integral@member.fsf.org>

pkgname=linux-apfs-rw-dkms
_pkgname=${pkgname%-dkms}
epoch=1
pkgver=0.3.15
pkgrel=1
pkgdesc="Experimental APFS kernel module with Write support (DKMS)"
arch=('any')
url="https://github.com/linux-apfs/${_pkgname}"
license=('GPL-2.0-only')
depends=('dkms')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('bbf6b2e044c004ce0b0cb3f035ae80faf6b8d25475e573272b52e0494bf38e0a')

package() {
	local dkms_dir="${pkgdir}/usr/src/${_pkgname}-${pkgver}/"
	install -d "${dkms_dir}"
	cp -r ${_pkgname}-${pkgver}/* "${dkms_dir}"
}
