# Maintainer: Omar Pakker <archlinux@opakker.nl>
# Maintainer: ston <2424284164@qq.com>
# Maintainer: Merrkry <jeffpotvin930@gmail.com>

_pkgname=looking-glass
pkgbase=looking-glass-rc
pkgname=("${pkgbase}"
	"${pkgbase}-module-dkms"
	"${pkgbase}-host"
	"obs-plugin-${pkgbase}")
epoch=1
pkgver=B7
_pkgver=$(echo "$pkgver" | sed 's/\([A-Z]\+[0-9]\+\)\(rc\)/\1-\2/')
pkgrel=1
pkgdesc="An extremely low latency KVMFR (KVM FrameRelay) implementation for guests with VGA PCI Passthrough. (Candidate Version)"
url="https://looking-glass.io/"
arch=('x86_64')
license=('GPL-2.0-or-later')
makedepends=('cmake' 'fontconfig' 'libpipewire' 'libpulse'
	'libsamplerate' 'libxi' 'libxpresent' 'libxss' 'obs-studio'
	'spice-protocol' 'wayland-protocols')
source=("looking-glass-${_pkgver}.tar.gz::https://looking-glass.io/artifact/${_pkgver}/source")
sha256sums=('09e506660ccc1b9691d06caa70179b52ffb4393299895cff3c2f0e74fcd69985')

_lgdir="${_pkgname}-${_pkgver}"

build() {
	cd "${srcdir}/${_lgdir}"
	for b in {client,host,obs}/build; do
		mkdir "${b}"
		pushd "${b}"
		# OPTIMIZE_FOR_NATIVE defined in ../cmake/OptimizeForNative.cmake
		# Defaults to AUTO and is automatically set if unspecified
		cmake -DOPTIMIZE_FOR_NATIVE=x86-64-v2 -DCMAKE_INSTALL_PREFIX=/usr ..
		make
		popd
	done
}

package_looking-glass-rc() {
	pkgdesc="A client application for accessing the LookingGlass IVSHMEM device of a VM"
	depends=('binutils' 'fontconfig' 'gcc-libs' 'glibc' 'gmp' 'libegl' 'libgl'
		'libpipewire' 'libpulse' 'libsamplerate' 'libx11' 'libxcursor'
		'libxfixes' 'libxi' 'libxinerama' 'libxkbcommon' 'libxpresent'
		'libxss' 'nettle' 'wayland' 'zlib' 'zstd')
	provides=("${_pkgname}")
	conflicts=("${_pkgname}")
	cd "${srcdir}/${_lgdir}/client/build"
	make DESTDIR="${pkgdir}" install
}

package_looking-glass-rc-module-dkms() {
	pkgdesc="A kernel module that implements a basic interface to the IVSHMEM device for when using LookingGlass in VM->VM mode"
	depends=('dkms')
	provides=("${_pkgname}-module-dkms")
	conflicts=("${_pkgname}-module-dkms")
	cd "${srcdir}/${_lgdir}/module"
	install -Dm644 -t "${pkgdir}/usr/src/${_pkgname}-${_pkgver}" \
		Makefile \
		dkms.conf \
		kvmfr.{h,c}
}

package_looking-glass-rc-host() {
	pkgdesc="Linux host application for pushing frame data to the LookingGlass IVSHMEM device"
	depends=('binutils' 'gcc-libs' 'glib2' 'glibc'
		'libpipewire' 'libxcb' 'zlib' 'zstd')
	provides=("${_pkgname}-host")
	conflicts=("${_pkgname}-host")
	cd "${srcdir}/${_lgdir}/host/build"
	make DESTDIR="${pkgdir}" install
}

package_obs-plugin-looking-glass-rc() {
	pkgdesc="Plugin for OBS Studio to stream directly from Looking Glass without having to record the Looking Glass client"
	depends=('glibc' 'obs-studio')
	provides=("obs-plugin-${_pkgname}")
	conflicts=("obs-plugin-${_pkgname}")
	install -Dm644 -t "${pkgdir}/usr/lib/obs-plugins" \
		"${srcdir}/${_lgdir}/obs/build/liblooking-glass-obs.so"
}
