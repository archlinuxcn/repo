# Maintainer: Integral <integral@member.fsf.org>

pkgname=linux-apfs-rw-dkms
_pkgname=${pkgname%-dkms}
epoch=1
pkgver=0.3.12
pkgrel=1
pkgdesc="Experimental APFS kernel module with Write support (DKMS)"
arch=('any')
url="https://github.com/linux-apfs/${_pkgname}"
license=('GPL-2.0-only')
depends=('dkms')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('b66a2213c69279d2fc08ce21f16868a1c416f7dd5af4c33d7e41c6b1f1c9e4ae')

package() {
	local dkms_dir="${pkgdir}/usr/src/${_pkgname}-${pkgver}/"
	install -d "${dkms_dir}"
	cp -r ${_pkgname}-${pkgver}/* "${dkms_dir}"
}
