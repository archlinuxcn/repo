# Maintainer: Jameson Pugh <imntreal@gmail.com>
 
pkgname=shashlik-bin
pkgver=0.9.3
pkgrel=1
pkgdesc="run Android applications on a standard Linux desktop"
arch=('x86_64')
url="http://www.shashlik.io"
license=('GPL')
depends=('python' 'lib32-libgl' 'kdebase-kdialog')
conflicts=('shashlik')
provides=('shashlik')
source=("http://static.davidedmundson.co.uk/shashlik/shashlik_${pkgver}.deb")
sha256sums=('a0a9daaeea0436ec8bd90b97112694974f7cf121d5a54083244488ff2d86dbaa')
 
package() {
  cd "${srcdir}"
  
  tar -xJC "${pkgdir}" -f data.tar.xz
  install -dm755 "${pkgdir}/usr/bin"
  ln -s /opt/shashlik/bin/shashlik-run "${pkgdir}/usr/bin/"
  ln -s /opt/shashlik/bin/shashlik-install "${pkgdir}/usr/bin/"
}
 
# vim:set ts=2 sw=2 et:
