# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: nylocx <aur@nyloc.de>

pkgname=telegramqml
_pkgname=TelegramQML
pkgver=0.9.1
_pkgtar=$pkgver-stable
pkgrel=1
pkgdesc="Telegram API tools for QtQml and Qml"
arch=('i686' 'x86_64')
url="https://github.com/Aseman-Land/TelegramQML"
license=('GPL')
depends=('qt5-quick1' 'qt5-webkit>=5.5' 'qt5-imageformats' 'qt5-graphicaleffects'
         'qt5-quickcontrols' 'libqtelegram-ae>=2:6.0')
source=("https://github.com/Aseman-Land/TelegramQML/archive/v$_pkgtar.tar.gz")
sha256sums=('00a52f6212460c2cae1dbd8ec4aa21e226552642cee56220802590fd8c4f61e9')

prepare() {
  cd "${srcdir}/${_pkgname}-${_pkgtar}"
  mkdir -p build 
}

build() {
  cd "${srcdir}/${_pkgname}-${_pkgtar}/build"
  qmake-qt5 -r .. PREFIX=/usr INSTALL_LIBS_PREFIX=/usr/lib INSTALL_HEADERS_PREFIX=/usr/include BUILD_MODE+=lib
  make
}

package() {
  cd "${srcdir}/${_pkgname}-${_pkgtar}/build"
  make INSTALL_ROOT="${pkgdir}" install
}
