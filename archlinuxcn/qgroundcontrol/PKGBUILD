# Maintainer: Kye Morton <pryre.dev@outlook.com>
pkgname=qgroundcontrol
pkgver=3.3.2
pkgrel=1
pkgdesc="Ground control for unmanned vehicles."
arch=('any')
url="http://qgroundcontrol.org/"
license=('GPL3')
depends=(\
  'espeak'  # optional but you have to decide if you want it at built-time\
  'qt5-svg' 'qt5-graphicaleffects' 'qt5-webkit' 'phonon-qt4' 'qt5-serialport'\
  'qt5-quickcontrols')

source=('qgroundcontrol-'${pkgver}'-'${pkgrel}'::https://github.com/mavlink/qgroundcontrol/releases/download/v'${pkgver}'/qgroundcontrol.tar.bz2')
sha256sums=('fe02e01447a191968ddc822fcc9a451d7e3b1429538edca6fa36adeb186eb110')

build() {
  echo "[Desktop Entry]
Type=Application
Name=QGroundControl
Comment=Ground control for unmanned vehicles
Path=/opt/qgroundcontrol/
Exec=/usr/bin/qgroundcontrol
Icon=/opt/qgroundcontrol/qgroundcontrol.png
Terminal=false
Categories=Qt;Utility;" > "$srcdir/${pkgname}/qgroundcontrol.desktop"
}

package() {
  mkdir -p "${pkgdir}/opt" "${pkgdir}/usr/bin" "${pkgdir}/usr/share/applications"
  cp -R "$srcdir/${pkgname}" "${pkgdir}/opt/qgroundcontrol"
  ln -s "/opt/qgroundcontrol/qgroundcontrol-start.sh" "${pkgdir}/usr/bin/qgroundcontrol"
  ln -s "/opt/qgroundcontrol/qgroundcontrol.desktop" "${pkgdir}/usr/share/applications/qgroundcontrol.desktop"
}

# vim:set ts=2 sw=2 et:
