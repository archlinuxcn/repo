# Maintainer: ava1ar <maiL@ava1ar.me>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: Nicolas Bigaouette <nbigaouette@gmail.com>
# Contributor: Vojtech "kralyk" Kral

pkgname=intel-opencl-sdk
pkgver=2016_6.2.0.1761
pkgrel=2
pkgdesc="Intel SDK for OpenCL Applications"
arch=('x86_64')
url="https://software.intel.com/en-us/intel-opencl/download"
license=('custom:intel')
depends=('opencl-icd-loader' 'libpng12' 'opencl-headers')
optdepends=('intel-opencl-runtime: OpenCL runtime for Intel Core and Xeon processors')
install=intel-opencl-sdk.install
source=(http://registrationcenter-download.intel.com/akdlm/irc_nas/9552/intel_sdk_for_opencl_${pkgver}_x64.tgz)
sha256sums=('cf6c575fb2fe5ce38d08f286eb7fd45fec7263f700788c4dc6a6bf9b13ec368c')

package() {
  cd "${srcdir}"/intel_sdk*/

  # Copy license
  install -Dm644 EULA.txt "${pkgdir}"/usr/share/licenses/intel-opencl-sdk/license
                
  # Unpack rpms
  for i in rpm/*.rpm; do bsdtar -xf "$i"; done

  # Install files
  mkdir -p "${pkgdir}/opt/intel/opencl-sdk"
  cp -r opt/intel/opencl-*/* "${pkgdir}/opt/intel/opencl-sdk"

  # Cleanup
  rm -rf "${pkgdir}"/opt/intel/opencl-sdk/uninstall*

  # Fix runtime_lib_dir and sdk_dir
  sed -i -e 's|/etc/alternatives/opencl-intel-tools|/opt/intel/opencl-sdk|g' \
	-e 's|$(dirname $(readlink /etc/alternatives/opencl-libOpenCL.so))|/opt/intel/opencl-runtime/lib64|g' \
  	"${pkgdir}"/opt/intel/opencl-sdk/bin/{KBServer64,KernelBuilder64,ioc64}

  # Symlink binaries
  mkdir -p "${pkgdir}/usr/bin"
  ln -s "/opt/intel/opencl-sdk/bin/ioc64" "${pkgdir}/usr/bin/ioc"
}
