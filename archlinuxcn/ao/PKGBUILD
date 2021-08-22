# Maintainer: peeweep <peeweep at 0x0 dot ee>
# Contributor: David Naramski <david.naramski AT gmail.com>
# Contributor: Paul Oppenheimer <redg3ar@airmail.cc>
pkgname=ao
pkgver=6.9.0
pkgrel=5
pkgdesc="An Electron wrapper for Microsoft To-Do"
arch=('x86_64')
url="https://github.com/klaussinani/ao/"
license=('MIT')
depends=('gconf' 'libnotify' 'libxtst' 'nss' 'libxss')
provides=('ao')
conflicts=('ao-git')
source=("${url}/releases/download/v${pkgver}/${pkgname}_${pkgver}_amd64.deb")
md5sums=('8fe0128134c2aca685049a14cf0fd6bf')

package() {
  tar xfJ ${srcdir}/data.tar.xz -C ${pkgdir}
  install -d ${pkgdir}/usr/bin/
  ln -s /opt/Ao/ao ${pkgdir}/usr/bin/ao
  install -Dm 644 "${pkgdir}/usr/share/icons/hicolor/0x0/apps/ao.png" "${pkgdir}/usr/share/pixmaps/ao.png"
  rm -rfv "${pkgdir}/usr/share/icons/hicolor"
}
