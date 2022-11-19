# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel at yahoo dot com>

_pkgbase=hsa-amd-aqlprofile
pkgname=${_pkgbase}-bin
_pkgver_major=5
_pkgver_minor=3
_pkgver_patch=2
_pkgver_str="${_pkgver_major}$(printf '%02d' $_pkgver_minor $_pkgver_patch)"
_pkgver_magic=96
_pkgver_ubunturel=22.04
pkgver=$_pkgver_major.$_pkgver_minor.$_pkgver_patch
pkgrel=1
pkgdesc='AQLPROFILE library for AMD HSA runtime API extension support'
arch=('x86_64')
url='https://docs.amd.com/'
license=('EULA')
depends=()
provides=('hsa-amd-aqlprofile')
conflicts=('hsa-amd-aqlprofile')
source=(# https://repo.radeon.com/rocm/apt/5.3.2/pool/main/h/hsa-amd-aqlprofile/hsa-amd-aqlprofile_1.0.0.50302-96~22.04_amd64.deb
        "${_pkgbase}-${pkgver}.deb::https://repo.radeon.com/rocm/apt/${pkgver/.0/}/pool/main/${_pkgbase:0:1}/${_pkgbase}/${_pkgbase}_1.0.0.${_pkgver_str}-${_pkgver_magic}~${_pkgver_ubunturel}_amd64.deb")
sha256sums=('18a8279347137cd23e73d376501ec3e49502443817087aaf48fe5e7b51d6c9d5')

prepare() {
  tar -xf data.tar.gz
}

package() {
  mv ${srcdir}/opt ${pkgdir}/opt
  rename -- "-$pkgver" '' "$pkgdir/opt/rocm-$pkgver"
  rename -- "${_pkgbase#hsa}" '' "$pkgdir/opt/rocm/$_pkgbase"
  find "$pkgdir" -type d -exec chmod 755 '{}' '+'
  ln -sf "/opt/rocm/hsa/lib/libhsa-amd-aqlprofile64.so" "$pkgdir/opt/rocm/lib/libhsa-amd-aqlprofile64.so.1"
}
