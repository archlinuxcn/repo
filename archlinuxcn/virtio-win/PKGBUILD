# Maintainer: Javier Tia <javier dot tia at gmail dot com>

pkgname=virtio-win
_ver=0.1.285
# upstream version
_pkgver=${_ver}-1
# package version
pkgver=${_ver}.1
pkgrel=2
pkgdesc='virtio drivers for Windows 7 and newer guests'
arch=('any')
url='https://docs.fedoraproject.org/en-US/quick-docs/creating-windows-virtual-machines-using-virtio-drivers/index.html'
license=('BSD-3-Clause')
optdepends=('qemu')
# https://fedorapeople.org/groups/virt/virtio-win/CHANGELOG
changelog="${pkgname}.changelog"
# install="${pkgname}.install"
_url=https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio
source=("${pkgname}-${_pkgver}.iso::${_url}/${pkgname}-${_pkgver}/${pkgname}.iso")
noextract=("${pkgname}-${_pkgver}.iso")
sha256sums=('e14cf2b94492c3e925f0070ba7fdfedeb2048c91eea9c5a5afb30232a3976331')

note() {
	printf "${blue}==>${yellow} NOTE:${bold} $1${all_off}\n"
}

package() {
	IMG_PATH=/var/lib/libvirt/images
	install -Dm 644 ${pkgname}-${_pkgver}.iso \
		"${pkgdir}${IMG_PATH}/${pkgname}.iso"

	note "The images can be found in ${IMG_PATH}"
}

# vim:set ts=2 sw=2 et:
