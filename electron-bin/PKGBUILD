# Maintainer: Piotr Mrożek <dnadesigned@gmail.com>
# Contributor: /dev/rs0 <rs0@secretco.de.com>
# Contributor: Daniel Perez <tuvistavie@gmail.com>

pkgname=electron-bin
pkgver=1.3.2
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
  'arm'   ) _arch='arm' ; sha256sums=('93d7ddb7f7e080b7c378ab83a48777a5516182cf0ee549833f2fe26d7132a1b3');;
  'i686'  ) _arch='ia32'; sha256sums=('6a3c901ee47ad9119c92502bb96cc3784379a45cb417d68685cfc7d58f922604');;
  'x86_64') _arch='x64' ; sha256sums=('a40777aa1ecdf30359b0532f2243baa83f0a41135ee6fa272af48a7cda011c29');;
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
