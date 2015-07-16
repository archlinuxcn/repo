# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: nylocx <aur@nyloc.de>

pkgname=telegramqml
_pkgname=TelegramQML
pkgver=0.8.0
_pkgtar=$pkgver-stable
pkgrel=2
pkgdesc="Telegram API tools for QtQml and Qml"
arch=('i686' 'x86_64')
url="https://github.com/Aseman-Land/TelegramQML"
license=('GPL')
depends=('qt5-quick1' 'qt5-webkit>=5.5' 'qt5-imageformats' 'qt5-graphicaleffects'
         'qt5-quickcontrols' 'libqtelegram-ae>=2:5.0')
source=("https://github.com/Aseman-Land/TelegramQML/archive/v$_pkgtar.tar.gz")
sha256sums=('38d4cd7cc26f6ea6852c94bb0c9b4648fbeef7db281053a99f2a2bd3327082d0')

prepare() {
  cd "${srcdir}/${_pkgname}-${_pkgtar}"
  sed -i 's#target.path = $$PREFIX/lib/$$LIB_PATH#target.path = $$PREFIX/lib#' telegramqml.pro
  mkdir -p build 
}

build() {
  cd "${srcdir}/${_pkgname}-${_pkgtar}/build"
  qmake-qt5 -r .. PREFIX=/usr BUILD_MODE+=lib
  make
}

package() {
  cd "${srcdir}/${_pkgname}-${_pkgtar}/build"
  make INSTALL_ROOT="${pkgdir}" install
}
