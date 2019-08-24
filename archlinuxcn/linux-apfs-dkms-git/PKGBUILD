# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: ManU
# Forked from aur/linux-can-dkms
# Contributor: Kyle Manna <kyle(at)kylemanna(dot)com>

pkgname=linux-apfs-dkms-git
epoch=1
pkgver=r4.6269eed
pkgrel=1
pkgdesc="Experimental APFS kernel module (DKMS)"
arch=('any')
url="https://github.com/eafer/linux-apfs-oot"
license=('GPL2')
depends=('dkms')
makedepends=('git')
source=("git+https://github.com/eafer/linux-apfs-oot"
        'dkms.patch::https://github.com/yan12125/linux-apfs-oot/commit/7f46eb50991b9ea5c674b5442e87ef53e73890d5.patch')
sha256sums=('SKIP'
            '822ce631d3b7816ef02243ebc31db09459b8279fab307b92c780615b23e7f170')

pkgver() {
  cd linux-apfs-oot
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd linux-apfs-oot
  patch -Np1 -i ../dkms.patch
}

package() {
  install -Ddm755 "${pkgdir}/usr/src/${pkgname}-${pkgver}/"
  cp -dr --no-preserve=ownership linux-apfs-oot/* "${pkgdir}/usr/src/${pkgname}-${pkgver}/"
}
