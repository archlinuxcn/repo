# Maintainer: Piotr Mrożek <dnadesigned@gmail.com>
# Contributor: /dev/rs0 <rs0@secretco.de.com>
# Contributor: Daniel Perez <tuvistavie@gmail.com>

pkgname=electron-bin
pkgver=1.3.3
pkgrel=1
pkgdesc="Framework for writing cross-platform desktop applications using JavaScript, HTML and CSS."

arch=('arm' 'i686' 'x86_64')
url="https://github.com/electron/electron"
license=('MIT')

replaces=('atom-shell')
provides=('electron')
conflicts=('electron')

optdepends=('nodejs')
depends=('libgcrypt15' 'libnotify' 'gconf' 'alsa-lib' 'nss' 'libxtst' 'gtk2' 'libgnome-keyring')

case $CARCH in
  'arm'   ) _arch='arm' ; sha256sums=('24dd633ffde02a8291488d0c32602cedd97c17383b340b8b976aa24feccafd2b');;
  'i686'  ) _arch='ia32'; sha256sums=('a2832f06215df2f32754000087c106018f99895136f1e4faf574d0705da27197');;
  'x86_64') _arch='x64' ; sha256sums=('277727209f60987aacb86227bf0e5cf6f9dca0a53476521d887f8944090ea53d');;
esac

_zipname="electron-v${pkgver}-linux-${_arch}.zip"

source=("https://github.com/electron/electron/releases/download/v${pkgver}/${_zipname}")

package() {
  install -d "${pkgdir}/usr/lib/electron"
  cp -a "${srcdir}/." "${pkgdir}/usr/lib/electron"
  rm "${pkgdir}/usr/lib/electron/${_zipname}"

  install -d "${pkgdir}/usr/bin"
  ln -s "/usr/lib/electron/electron" "${pkgdir}/usr/bin/electron"

  install -Dm644 "${pkgdir}/usr/lib/electron/LICENSE" "${pkgdir}/usr/share/licenses/electron/LICENSE"
  install -Dm644 "${pkgdir}/usr/lib/electron/LICENSES.chromium.html" "${pkgdir}/usr/share/licenses/electron/LICENSES.chromium.html"
  rm "${pkgdir}/usr/lib/electron/LICENSE"
  rm "${pkgdir}/usr/lib/electron/LICENSES.chromium.html"
  ln -sf "/usr/lib/libgcrypt.so.11" "${pkgdir}/usr/lib/electron/libgcrypt.so.11"
  ln -sf "/usr/lib/libnotify.so.4" "${pkgdir}/usr/lib/electron/libnotify.so.4"
  ln -sf "/usr/lib/libudev.so" "${pkgdir}/usr/lib/electron/libudev.so.0"

  find "${pkgdir}" -type d -exec chmod 755 {} +
  find "${pkgdir}" -type f -exec chmod 644 {} +
  chmod 755 "${pkgdir}/usr/lib/electron/electron"
}
