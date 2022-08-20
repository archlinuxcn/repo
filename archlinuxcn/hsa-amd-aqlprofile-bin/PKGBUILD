# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel at yahoo dot com>

pkgname=hsa-amd-aqlprofile-bin
_pkgname=hsa-amd-aqlprofile
pkgver=5.2.3
_pkgver=5.2.3
pkgrel=1
_debfile="hsa-amd-aqlprofile_1.0.0.50203-109_amd64.deb"
pkgdesc='AQLPROFILE library for AMD HSA runtime API extension support'
arch=('x86_64')
url='https://docs.amd.com/'
license=('EULA')
depends=()
provides=('hsa-amd-aqlprofile')
conflicts=('hsa-amd-aqlprofile')
source=("$pkgname-$pkgver.tar.gz::http://repo.radeon.com/rocm/apt/${_pkgver}/pool/main/h/hsa-amd-aqlprofile/${_debfile}")
sha256sums=('ac94ead24a5ecfc9462b09ef647ac036333c856391571e9071e3263f1232dd71')

package() {
  tar -C "$pkgdir" -xf data.tar.gz
  rename -- "-$pkgver" '' "$pkgdir/opt/rocm-$pkgver"
  rename -- "${_pkgname#hsa}" '' "$pkgdir/opt/rocm/$_pkgname"
  find "$pkgdir" -type d -exec chmod 755 '{}' '+'
  ln -sf "/opt/rocm/hsa/lib/libhsa-amd-aqlprofile64.so" "$pkgdir/opt/rocm/lib/libhsa-amd-aqlprofile64.so" 
}
