# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel at yahoo dot com>

pkgname=hsa-amd-aqlprofile-bin
_pkgname=hsa-amd-aqlprofile
pkgver=5.1.3
_pkgver=5.1.3
pkgrel=1
_debfile="hsa-amd-aqlprofile_1.0.0.50103-66_amd64.deb"
pkgdesc='AQLPROFILE library for AMD HSA runtime API extension support'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/'
license=('EULA')
depends=()
provides=('hsa-amd-aqlprofile')
conflicts=('hsa-amd-aqlprofile')
source=("$pkgname-$pkgver.tar.gz::http://repo.radeon.com/rocm/apt/${_pkgver}/pool/main/h/hsa-amd-aqlprofile/${_debfile}")
sha256sums=('ba76a30f078cfd2d4927fd43840f22265ebc0dfd1c03ac3bc36f637b67ec4119')

package() {
  tar -C "$pkgdir" -xf data.tar.gz
  rename -- "-$pkgver" '' "$pkgdir/opt/rocm-$pkgver"
  rename -- "${_pkgname#hsa}" '' "$pkgdir/opt/rocm/$_pkgname"
  find "$pkgdir" -type d -exec chmod 755 '{}' '+'
  ln -sf "/opt/rocm/hsa/lib/libhsa-amd-aqlprofile64.so" "$pkgdir/opt/rocm/lib/libhsa-amd-aqlprofile64.so" 
}
