# Maintainer: ava1ar <maiL@ava1ar.me>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: Nicolas Bigaouette <nbigaouette@gmail.com>
# Contributor: Vojtech "kralyk" Kral

pkgname=intel-opencl-sdk
pkgver=2017_7.0.0.2568
pkgrel=2
pkgdesc="Intel SDK for OpenCL Applications"
arch=('x86_64')
url="https://software.intel.com/en-us/intel-opencl/download"
license=('custom:intel')
depends=('opencl-icd-loader' 'libpng12' 'opencl-headers')
optdepends=('intel-opencl-runtime: OpenCL runtime for Intel Core and Xeon processors')
install=intel-opencl-sdk.install
source=(http://registrationcenter-download.intel.com/akdlm/irc_nas/vcp/12526/intel_sdk_for_opencl_${pkgver}_x64.gz)
sha256sums=('c3e91c25bef6165f769078de21da168816750f9d9a75f1407c1a26757e2819eb')

package() {
  cd "${srcdir}"/intel_sdk_for_opencl_${pkgver}_x64/

  # Copy license
  install -Dm644 EULA.txt "${pkgdir}"/usr/share/licenses/intel-opencl-sdk/license

  # Unpack rpms
  for i in rpm/*.rpm; do bsdtar -xf "$i"; done

  # Install files
  mkdir -p "${pkgdir}/opt/intel/opencl-sdk"
  cp -r opt/intel/opencl/* "${pkgdir}/opt/intel/opencl-sdk"

  # Register ICD (uncomment if you want to use bundled libintelocl_2_1.so)
  #mkdir -p "${pkgdir}/etc/OpenCL/vendors"
  #echo "/opt/intel/opencl-sdk/exp-runtime-2.1/lib64/libintelocl_2_1.so" > "${pkgdir}/etc/OpenCL/vendors/intel.icd"

  # Cleanup
  rm -rf "${pkgdir}"/opt/intel/opencl-sdk/uninstall*

  # Fix runtime_lib_dir and sdk_dir
  sed -i -e 's|/etc/alternatives/opencl-intel-tools|/opt/intel/opencl-sdk/SDK|g' \
	-e 's|$(dirname $(readlink /etc/alternatives/opencl-libOpenCL.so))|/opt/intel/opencl-runtime/lib64|g' \
	"${pkgdir}"/opt/intel/opencl-sdk/SDK/bin/{KBServer64,ioc64}

  # Symlink binaries
  mkdir -p "${pkgdir}/usr/bin"
  ln -s "/opt/intel/opencl-sdk/SDK/bin/ioc64" "${pkgdir}/usr/bin/ioc"
}
