# Maintainer: mrxx <mrxx at cyberhome dot at>
# Contributor: Shane Utt <shaneutt at linux.com>

pkgname=packetsender
pkgver=8.0.9
pkgrel=1
pkgdesc="Network utility for sending / receiving TCP and UDP packets"
_basename=PacketSender
arch=('any')
url="http://packetsender.com/"
license=('GPL')
depends=('qt5-base')
makedepends=('qt5-base')
source=("https://github.com/dannagle/PacketSender/archive/v${pkgver}.tar.gz" "${pkgname}.desktop" "${pkgname}.png")
sha256sums=('f9b0a68da3b541f83e248137deb4a35e5f412136b592f522a7aef1c6d537b207'
            '8a9c06f1ce7a0d7a919fb9664d2d5b83d957c34ef2357b0fd89ce0d638380370'
            '31f00a13c2823ddfadcf5cb3be90acc547c188ae3f3b30acde148eb8fce62ba8')

build() {
  cd "${srcdir}/${_basename}-${pkgver}/src"

  qmake-qt5 PacketSender.pro
  make
}

package() {
pwd
  install -Dm644 -t ${pkgdir}/usr/share/applications ${pkgname}.desktop
  install -Dm644 -t ${pkgdir}/usr/share/icons/hicolor/32x32/apps/ ${pkgname}.png
  install -Dm 755 ${srcdir}/${_basename}-${pkgver}/src/${pkgname} "${pkgdir}/usr/bin/${pkgname}"
}
