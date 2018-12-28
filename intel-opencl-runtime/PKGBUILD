# Maintainer: ava1ar <mail@ava1ar.me>
# Contributor: Duong Pham <dthpham@gmail.com>
# Contributor: Eric Quackenbush <mail@ericquackenbush.com>
# Contributor: Wei-Ning Huang <aitjcize@gmail.com>

pkgname=intel-opencl-runtime
epoch=1
pkgver=18.1.0.013
_package=l_opencl_p_${pkgver}
pkgrel=2
pkgdesc="OpenCL runtime for Intel Core and Xeon processors"
arch=('x86_64')
url="https://software.intel.com/en-us/articles/opencl-drivers#latest_CPU_runtime"
license=('custom:intel')
depends=('numactl' 'intel-tbb' 'zlib' 'ncurses5-compat-libs')
optdepends=('intel-opencl-sdk: Intel SDK for OpenCL Applications')
provides=('opencl-intel' 'opencl-driver')
source=(http://registrationcenter-download.intel.com/akdlm/irc_nas/13793/${_package}.tgz)
sha256sums=('208806279b0b9219ca6a17c64cbe0e4a3876a8b5d3f172bf296d85c0f1c74126')

package() {
    cd "${srcdir}"/${_package}/

    # Copy license
    install -Dm644 license.txt "${pkgdir}"/usr/share/licenses/intel-opencl-runtime/license

    # Unpack RPM
    rm rpm/intel-openclrt-pset-*.rpm
    for i in rpm/*.rpm; do bsdtar -xf "$i"; done

    # Register ICD
    mkdir -p "${pkgdir}/etc/OpenCL/vendors"
    echo "/opt/intel/opencl-runtime/linux/compiler/lib/intel64_lin/libintelocl.so" > "${pkgdir}/etc/OpenCL/vendors/intel.icd"

    # Install files
    mkdir -p "${pkgdir}/opt/intel/opencl-runtime"
    cp -r opt/intel/opencl_*/* "${pkgdir}/opt/intel/opencl-runtime"
}
