# Maintainer: Kewl <xrjy@nygb.rh.bet(rot13)>
# Maintainer: Samuel Walladge <samuel at swalladge dot id dot au>

pkgname=simplenote-electron-bin
pkgver=2.16.0
pkgrel=1
pkgdesc="The simplest way to keep notes"
arch=('x86_64' 'armv7h')
url="https://github.com/Automattic/simplenote-electron"
license=('GPL2')
depends=('nss' 'gtk3' 'libxss')
provides=('simplenote')
source_x86_64=("${url}/releases/download/v${pkgver}/Simplenote-linux-${pkgver}-amd64.deb")
source_armv7h=("${url}/releases/download/v${pkgver}/Simplenote-linux-${pkgver}-armv7l.deb")
sha256sums_x86_64=('7e752a53436b87483d64b88cf588e81f71e7875adf683bc55b7983771726eb86')
sha256sums_armv7h=('70a3388af44d7d6fb71cd9d7e009159c02155f92624816e506916763fd290c7f')

# Warning: the release deb file has been known to be silently modified, resulting in a different checksum. 
# If the checksum fails to validate, this is most likely the cause. If you are concerned about the
# security implications of this, do not install this package.
# This issue has been raised and acknowledged by Automattic in Sep'18: https://github.com/Automattic/simplenote-electron/issues/759

package() {
  bsdtar -xv -C "${pkgdir}" -f "${srcdir}/data.tar.gz"
  mkdir -p "${pkgdir}/usr/bin/"
  ln -s "/opt/Simplenote/${pkgname%-electron-bin}" "${pkgdir}/usr/bin"
}
