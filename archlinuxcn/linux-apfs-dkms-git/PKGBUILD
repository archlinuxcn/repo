# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: ManU
# Forked from aur/linux-can-dkms
# Contributor: Kyle Manna <kyle(at)kylemanna(dot)com>

pkgname=linux-apfs-dkms-git
epoch=1
pkgver=r5.277a34e
pkgrel=1
pkgdesc="Experimental APFS kernel module (DKMS)"
arch=('any')
url="https://github.com/eafer/linux-apfs-oot"
license=('GPL2')
depends=('dkms')
makedepends=('git')
source=("git+https://github.com/eafer/linux-apfs-oot")
sha256sums=('SKIP')

pkgver() {
  cd linux-apfs-oot
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd linux-apfs-oot
  dkms_version=$(grep PACKAGE_VERSION dkms.conf | sed -r 's#PACKAGE_VERSION="([0-9.]+)"#\1#')
  dkms_dir="$pkgdir/usr/src/linux-apfs-$dkms_version/"
  install -Ddm755 "$dkms_dir"
  cp -dr --no-preserve=ownership * "$dkms_dir"
}
