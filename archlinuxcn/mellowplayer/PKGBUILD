# Maintainer: Colin Duquesnoy <colin.duquesnoy@gmail.com>
# Maintainer: ZeroDot1 <zerodot1@bk.ru>
pkgname=mellowplayer
_pkgname=MellowPlayer
pkgver=3.6.3
pkgrel=2
pkgdesc="Open source and cross-platform desktop application that runs web-based music streaming 
         services in its own window and provides integration with your desktop."
url='https://gitlab.com/ColinDuquesnoy/MellowPlayer'
license=('GPL')
arch=('x86_64' 'aarch64')
depends=('qt5-base' 'qt5-webengine' 'qt5-svg' 'qt5-quickcontrols2' 'qt5-quickcontrols' 'qt5-translations' 'qt5-graphicaleffects' 'xdg-utils' 'libnotify' 'libevent')
makedepends=('qt5-tools' 'cmake' 'mesa' 'ninja' 'pkgconf')
optdepends=( 'chromium-widevine: DRM needed for Spotify and Amazon Music' 'pepper-flash: needed for Tidal')
source=("https://gitlab.com/ColinDuquesnoy/MellowPlayer/-/archive/${pkgver}/MellowPlayer-${pkgver}.tar.gz")
md5sums=('44fff77740d3f9c22188f97e913cc2b8')

build() {
  cd $srcdir/MellowPlayer-${pkgver}
  cmake -GNinja -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_PREFIX="$pkgdir/usr" .
  ninja 
}

package() {
  cd $srcdir/MellowPlayer-${pkgver}
  ninja install
}

