# Maintainer: Kewl <xrjy@nygb.rh.bet(rot13)>
# Maintainer: Samuel Walladge <samuel at swalladge dot id dot au>

pkgname=simplenote-electron-bin
pkgver=2.17.0
pkgrel=1
pkgdesc="The simplest way to keep notes"
arch=('x86_64' 'armv7h')
url="https://github.com/Automattic/simplenote-electron"
license=('GPL2')
depends=('nss' 'gtk3' 'libxss')
provides=('simplenote')
source_x86_64=("${url}/releases/download/v${pkgver}/Simplenote-linux-${pkgver}-amd64.deb")
source_armv7h=("${url}/releases/download/v${pkgver}/Simplenote-linux-${pkgver}-armv7l.deb")
sha256sums_x86_64=('eb18a30b6e09e2da17ed42b8ec928e9b5f671a5b9072da3be7cea5dbb8ae3dc2')
sha256sums_armv7h=('ed1524e46dc2918b1044880b712b70fb7fc012890023c71924672b85a62bd8f5')

# Warning: the release deb file has been known to be silently modified, resulting in a different checksum. 
# If the checksum fails to validate, this is most likely the cause. If you are concerned about the
# security implications of this, do not install this package.
# This issue has been raised and acknowledged by Automattic in Sep'18: https://github.com/Automattic/simplenote-electron/issues/759

package() {
  bsdtar -xv -C "${pkgdir}" -f "${srcdir}/data.tar.gz"
  mkdir -p "${pkgdir}/usr/bin/"
  ln -s "/opt/Simplenote/${pkgname%-electron-bin}" "${pkgdir}/usr/bin"
}
