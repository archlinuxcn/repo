# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: nylocx <aur@nyloc.de>

pkgname=telegramqml-git
pkgver=0.8.0.stable.r0.gc8a2956
pkgrel=1
pkgdesc="Telegram API tools for QtQml and Qml"
arch=('i686' 'x86_64')
url="https://github.com/Aseman-Land/TelegramQML"
license=('GPL')
depends=('qt5-base' 'qt5-declarative' 'qt5-multimedia' 'qt5-quick1'
         'qt5-webengine' 'qt5-imageformats' 'qt5-graphicaleffects' 
         'qt5-quickcontrols' 'libqtelegram-ae>=2:0.5.0')
makedepends=('git')
source=("${pkgname}"::"git+https://github.com/Aseman-Land/TelegramQML.git")
md5sums=('SKIP')
provides=("telegramqml")
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
  sed -i 's#target.path = $$PREFIX/lib/$$LIB_PATH#target.path = $$PREFIX/lib#' telegramqml.pro
  mkdir -p build 
}

build() {
  cd "${srcdir}/${pkgname}/build"
  qmake-qt5 -r .. PREFIX=/usr BUILD_MODE+=lib
  make
}

package() {
  cd "${srcdir}/${pkgname}/build"
  make INSTALL_ROOT="${pkgdir}" install
}
