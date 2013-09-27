# Maintainer: Christoph Drexler <chrdr at gmx dot at>
# Contributor: Jelle van der Waa <jellevdwaa@gmail.com>

pkgname=xmind
pkgver=3.3.1
_pkgdate=201212250029
pkgrel=2
pkgdesc="Brainstorming and Mind Mapping Software"
arch=('i686' 'x86_64')
[ "${CARCH}" = "i686" ] && _arch="i386"
[ "${CARCH}" = "x86_64" ] && _arch="amd64"
url="http://www.xmind.net"
license=('EPL' 'LGPL')
depends=('desktop-file-utils' 'fontconfig' 'libxrender' 'java-runtime' 'shared-mime-info')
optdepends=('lame: needed for the feature audio notes')
install=xmind.install
source=(http://dl2.xmind.net/xmind-downloads/${pkgname}-linux-${pkgver}.${_pkgdate}_${_arch}.deb)
[ "${CARCH}" = "i686" ] && md5sums=('53d55f189879b4d2f27eb214456c754b')
[ "${CARCH}" = "x86_64" ] && md5sums=('a31c55dab417a8281ec4211f4ac111d7')

build() {
  cd "${srcdir}"
  ar x "${pkgname}-linux-${pkgver}.${_pkgdate}_${_arch}.deb"
  bsdtar -xf data.tar.gz
}

package() {
  install -d "${pkgdir}"/usr/share/xmind/
  cp -a "${srcdir}"/usr/local/xmind/* "${pkgdir}"/usr/share/xmind/
  cp -a "${srcdir}"/usr/share/* "${pkgdir}"/usr/share/
  install -d "${pkgdir}"/usr/bin/
  cd "${pkgdir}"/usr/bin/
  ln -s ../../usr/share/xmind/XMind .

  # getting the config files to the right place...
  install -d "${pkgdir}"/etc/xmind/
  mv "${pkgdir}"/usr/share/xmind/configuration/* \
    "${pkgdir}"/etc/xmind/
  cd "${pkgdir}"/usr/share/xmind/configuration/
  ln -s ../../../../etc/xmind/* .
  mv "${pkgdir}"/usr/share/xmind/XMind.ini \
    "${pkgdir}"/etc/xmind/
  cd ../
  ln -s ../../../etc/xmind/XMind.ini .

  # putting the png file where it belongs to
  install -d "${pkgdir}"/usr/share/pixmaps/
  mv "${pkgdir}"/usr/share/xmind/xmind-logo-36.png \
    "${pkgdir}"/usr/share/pixmaps/xmind.png
  sed -i s!Exec=.*!Exec=/usr/share/xmind/XMind! \
    "${pkgdir}"/usr/share/applications/xmind.desktop
  sed -i s!/usr/local/xmind/xmind-logo-36.png!xmind.png! \
    "${pkgdir}"/usr/share/applications/xmind.desktop
}
