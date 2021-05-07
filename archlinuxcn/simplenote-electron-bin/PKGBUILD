# Maintainer: Kewl <xrjy@nygb.rh.bet(rot13)>
# Maintainer: Samuel Walladge <samuel at swalladge dot id dot au>

pkgname=simplenote-electron-bin
pkgver=2.10.0
pkgrel=1
pkgdesc="The simplest way to keep notes"
arch=('x86_64' 'armv7h')
url="https://github.com/Automattic/simplenote-electron"
license=('GPL2')
depends=('nss' 'gtk3' 'libxss')
provides=('simplenote')
source_x86_64=("${url}/releases/download/v${pkgver}/Simplenote-linux-${pkgver}-amd64.deb")
source_armv7h=("${url}/releases/download/v${pkgver}/Simplenote-linux-${pkgver}-armv7l.deb")
sha256sums_x86_64=('24d85d4aa0df88b3bca4d4e987e5aa9788f4040f5141519dd58aa5facc971fe4')
sha256sums_armv7h=('16b4c326a97afaf89582f906ec7fc9a217e4436043124c7a11316e93dd594723')

# Warning: the release deb file has been known to be silently modified, resulting in a different checksum. 
# If the checksum fails to validate, this is most likely the cause. If you are concerned about the
# security implications of this, do not install this package.
# This issue has been raised and acknowledged by Automattic in Sep'18: https://github.com/Automattic/simplenote-electron/issues/759

package() {
  bsdtar -xv -C "${pkgdir}" -f "${srcdir}/data.tar.gz"
  mkdir -p "${pkgdir}/usr/bin/"
  ln -s "/opt/Simplenote/${pkgname%-electron-bin}" "${pkgdir}/usr/bin"
}
