# Maintainer: ava1ar <mail@ava1ar.me>
# Contributor: Duong Pham <dthpham@gmail.com>
# Contributor: Eric Quackenbush <mail@ericquackenbush.com>
# Contributor: Wei-Ning Huang <aitjcize@gmail.com>

pkgname=intel-opencl-runtime
epoch=1
pkgver=16.1.2
_package=opencl_runtime_${pkgver}_x64_rh_6.4.0.37
pkgrel=1
pkgdesc="OpenCL runtime for Intel Core and Xeon processors"
arch=('x86_64')
url="https://software.intel.com/en-us/articles/opencl-drivers#latest_CPU_runtime"
license=('custom:intel')
depends=('numactl' 'intel-tbb' 'zlib' 'ncurses5-compat-libs')
optdepends=('intel-opencl-sdk: Intel SDK for OpenCL Applications')
provides=('opencl')
source=(http://registrationcenter-download.intel.com/akdlm/irc_nas/12556/${_package}.tgz)
sha256sums=('7dabca91d9ef76a68858d8c3f2a70fb75e7c80861f2824642d7119aa0dbf8a9a')

package() {
	cd "${srcdir}"/${_package}/

	# Copy license
	install -Dm644 EULA.txt "${pkgdir}"/usr/share/licenses/intel-opencl-runtime/license

	# Unpack RPM
	rm rpm/opencl-1.2-base-pset-*.rpm
	for i in rpm/*.rpm; do bsdtar -xf "$i"; done

	# Register ICD
	mkdir -p "${pkgdir}/etc/OpenCL/vendors"
	echo "/opt/intel/opencl-runtime/lib64/libintelocl.so" > "${pkgdir}/etc/OpenCL/vendors/intel.icd"

	# Install files
	mkdir -p "${pkgdir}/opt/intel/opencl-runtime"
	cp -r opt/intel/opencl-*/* "${pkgdir}/opt/intel/opencl-runtime"
}
