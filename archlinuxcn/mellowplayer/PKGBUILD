# Maintainer: Colin Duquesnoy <colin.duquesnoy@gmail.com>
# Maintainer: ZeroDot1 <zerodot1@bk.ru>
pkgname=mellowplayer
_pkgname=MellowPlayer
pkgver=3.5.5
pkgrel=1
pkgdesc="Open source and cross-platform desktop application that runs web-based music streaming 
         services in its own window and provides integration with your desktop."
url='https://gitlab.com/ColinDuquesnoy/MellowPlayer'
license=('GPL')
arch=('x86_64')
depends=('qt5-base' 'qt5-webengine' 'qt5-svg' 'qt5-quickcontrols2' 'qt5-quickcontrols' 'qt5-translations' 'qt5-graphicaleffects' 'xdg-utils' 'libnotify' 'libevent')
makedepends=('qt5-tools' 'cmake' 'mesa' 'ninja')
optdepends=( 'chromium-widevine: DRM needed for Spotify and Amazon Music' 'pepper-flash: needed for Tidal')
source=("https://gitlab.com/ColinDuquesnoy/MellowPlayer/-/archive/${pkgver}/MellowPlayer-${pkgver}.tar.gz" 
        "widevine-path.patch")
md5sums=('58b98eb32a5c9aa6c5009ccec15fbb63'
         '67f8c5c6af4b770a4017a5ca9f137b90')

prepare() {
    cd $srcdir/MellowPlayer-${pkgver}
    patch -Np1 -i "${srcdir}/widevine-path.patch" "$srcdir/MellowPlayer-${pkgver}/src/main/share/applications/mellowplayer.desktop"
}

build() {
  cd $srcdir/MellowPlayer-${pkgver}
  cmake -GNinja -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_PREFIX="$pkgdir/usr" .
  ninja 
}

package() {
  cd $srcdir/MellowPlayer-${pkgver}
  ninja install
}

