# Maintainer: /dev/rs0 <rs0@secretco.de.com>
# Contributor: Daniel Perez <tuvistavie@gmail.com>

pkgname=electron
pkgver=0.37.2
pkgrel=1
pkgdesc="Framework for writing cross-platform desktop applications using JavaScript, HTML and CSS."

arch=('arm' 'i686' 'x86_64')
url="https://github.com/atom/electron"
license=('MIT')

replaces=('atom-shell')

optdepends=('nodejs')
depends=('libgcrypt15' 'libnotify' 'gconf' 'alsa-lib' 'nss' 'libxtst' 'gtk2' 'libgnome-keyring')

case $CARCH in
  'arm'   ) _arch='arm' ; sha256sums=('847bb0698d5d6964b5ead44acec1a96133a56bc46d8ce05c85217d192211369e');;
  'ia32'  ) _arch='ia32'; sha256sums=('ef43ca089ad3f13a4c8f7bffdc9bd756b3e9aa90d92c362a5ca8fca49e6c1001');;
  'x86_64') _arch='x64' ; sha256sums=('328b4ff86e300205b6eb4d90b315457d66b17fc52ecdc3b5acdb59364be08023');;
esac

source=("electron.zip::https://github.com/atom/electron/releases/download/v${pkgver}/electron-v${pkgver}-linux-${_arch}.zip")

package() {
  rm "${srcdir}/electron.zip"

  install -d "${pkgdir}/usr/share/electron"
  cp -a "${srcdir}/." "${pkgdir}/usr/share/electron"

  install -d "${pkgdir}/usr/bin"
  ln -s "/usr/share/electron/electron" "${pkgdir}/usr/bin/electron"

  install -Dm644 "${pkgdir}/usr/share/electron/LICENSE" "${pkgdir}/usr/share/licenses/electron/LICENSE"
  rm "${pkgdir}/usr/share/electron/LICENSE"
  ln -sf "/usr/lib/libgcrypt.so.11" "${pkgdir}/usr/share/electron/libgcrypt.so.11"
  ln -sf "/usr/lib/libnotify.so.4" "${pkgdir}/usr/share/electron/libnotify.so.4"
  ln -sf "/usr/lib/libudev.so" "${pkgdir}/usr/share/electron/libudev.so.0"

  find "${pkgdir}" -type d -exec chmod 755 {} +
  find "${pkgdir}" -type f -exec chmod 644 {} +
  chmod 755 "${pkgdir}/usr/share/electron/electron"
}
