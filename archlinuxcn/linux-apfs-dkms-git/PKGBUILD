# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Forked from aur/linux-can-dkms
# Contributor: Kyle Manna <kyle(at)kylemanna(dot)com>

pkgname=linux-apfs-dkms-git
pkgver=r798863.5a89c2b80757
pkgrel=1
pkgdesc="Experimental APFS kernel module (DKMS)"
arch=('any')
url="https://github.com/eafer/linux-apfs"
license=('GPL2')
depends=('dkms')
makedepends=('git')
source=("git+https://github.com/eafer/linux-apfs#branch=for-merge"
        'dkms.conf'
        'Makefile')
sha256sums=('SKIP'
            '969ef32aab0f30471305e5d900cd28fc5ae91f976b6d55a5ad84c6034bb8c307'
            '970fba1817f9df2b08f62e41e4af28b6577959da3bcf369a8546fe9d20096fed')

pkgver() {
  cd linux-apfs
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  # Copy Makefile and dkms.conf
  install -Dm644 Makefile "${pkgdir}"/usr/src/${pkgname}-${pkgver}/Makefile
  install -Dm644 dkms.conf "${pkgdir}"/usr/src/${pkgname}-${pkgver}/dkms.conf

  # Set name and version
  sed -e "s/@PKGNAME@/${pkgname}/" \
      -e "s/@PKGVER@/${pkgver}/" \
      -i "${pkgdir}"/usr/src/${pkgname}-${pkgver}/dkms.conf

  # Copy sources
  install -Ddm755 "${pkgdir}/usr/src/${pkgname}-${pkgver}/fs/"
  cp -dr --no-preserve=ownership linux-apfs/fs/apfs "${pkgdir}/usr/src/${pkgname}-${pkgver}/fs/apfs"
}
