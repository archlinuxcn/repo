# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: nylocx <aur@nyloc.de>

pkgname=telegramqml-git
pkgver=0.9.2.r21.g7d5110a
pkgrel=1
pkgdesc="Telegram API tools for QtQml and Qml"
arch=('i686' 'x86_64')
url="https://github.com/Aseman-Land/TelegramQML"
license=('GPL')
depends=('qt5-base' 'qt5-declarative' 'qt5-multimedia'
         'qt5-webkit>=5.5' 'qt5-imageformats' 'qt5-graphicaleffects'
         'qt5-quickcontrols' 'libqtelegram-ae>=2:6.0')
makedepends=('git')
source=("${pkgname}"::"git+https://github.com/Aseman-Land/TelegramQML.git")
md5sums=('SKIP')
provides=("telegramqml=$pkgver")
conflicts=("telegramqml")

pkgver() {
  cd "${srcdir}/${pkgname}"
  ( set -o pipefail
    git describe --long --tags 2>/dev/null | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

prepare() {
  cd "${srcdir}/${pkgname}"
  # fixing C++11 error
  echo "CONFIG += c++11" >> telegramqml.pro
  mkdir -p build 
}

build() {
  cd "${srcdir}/${pkgname}/build"
  qmake-qt5 -r .. PREFIX=/usr INSTALL_LIBS_PREFIX=/usr/lib INSTALL_HEADERS_PREFIX=/usr/include BUILD_MODE+=lib
  make
}

package() {
  cd "${srcdir}/${pkgname}/build"
  make INSTALL_ROOT="${pkgdir}" install
}
