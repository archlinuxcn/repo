# Maintainer: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)
# Contributor: Utsob Roy <uroybd(at)gmail(dot)com>

pkgname=franz-bin
pkgver=5.0.0_beta.22
pkgrel=1
pkgdesc='Franz is a free messaging app for services like WhatsApp, Slack, Messenger and many more'
arch=('x86_64')
url='https://meetfranz.com'
license=('Apache')
depends=('alsa-lib' 'gconf' 'gtk2' 'libsecret' 'libxss' 'libxtst' 'nss')
optdepends=('gnome-keyring')
conflicts=('franz')
options=('!strip' '!emptydirs')
source=("https://github.com/meetfranz/franz/releases/download/v${pkgver//_/-}/franz_${pkgver//_/-}_amd64.deb"
        "${pkgname}.patch")
sha256sums=('52444cf6c07283a6e4c2daa4ffa5d4176ae00018e48b34faa318936c3c666e51'
            'e0d03405a75a0cd4492875b111d4750b8a925b514f3ce9ef47b69b9fcaee2b7f')

package() {
  # Extract package data
  bsdtar -xJf data.tar.xz

  # Install package data
  mv "usr" "${pkgdir}"
  install -dm755 "${pkgdir}/usr/bin" "${pkgdir}/usr/lib"
  mv "opt/Franz" "${pkgdir}/usr/lib/franz"
  ln -s "../lib/franz/franz" "${pkgdir}/usr/bin/franz"

  # Permission fix
  chmod 644 "${pkgdir}/usr/lib/franz/libnode.so"

  # Fix binary path in .desktop file
  patch -d "${pkgdir}" -p1 <"${pkgname}".patch

  # Link licenses
  install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}"
  ln -s "/usr/lib/franz/LICENSE.electron.txt" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.electron.txt"
  ln -s "/usr/lib/franz/LICENSES.chromium.html" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSES.chromium.html"
}
