# Maintainer: Yurii Kolesnykov <root@yurikoles.com>
# Based on uefitool-ng-git by Bailey Fox <bfox200012@gmail.com>

pkgname=uefitool
_pkgname=UEFITool
_tools=(UEFIPatch UEFIReplace)
pkgver=0.28.0
pkgrel=2
epoch=1
pkgdesc='UEFI firmware image viewer and editor and utilities'
arch=('armv7h' 'aarch64' 'i686' 'x86_64')
url='https://github.com/LongSoft/UEFITool'
license=('BSD')
depends=('qt5-base')
makedepends=('zip')
provides=(uefipatch)
conflicts=("${pkgname}-git" uefipatch)
replaces=(uefipatch)
source=("${_pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('453cc817e17cf9aa5c5306df1994828c4f6cf9180e67bede2bbaca1135b43d3c')

build() {
  cd "${_pkgname}-${pkgver}"

  ./unixbuild.sh
}

package() {
  cd "${_pkgname}-${pkgver}"

  local _tool="UEFITool"
  install -Dm755 "${_tool}" "${pkgdir}/usr/bin/${_tool,,}"

  for _tool in "${_tools[@]}"; do
    install -Dm755 "${_tool}/${_tool}" "${pkgdir}/usr/bin/${_tool,,}"
  done

  install -Dm644 UEFIPatch/patches{,-misc}.txt -t "${pkgdir}/usr/share/${pkgname}"
  install -Dm644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
