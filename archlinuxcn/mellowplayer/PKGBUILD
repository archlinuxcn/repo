# Maintainer: Colin Duquesnoy <colin.duquesnoy@gmail.com>
# Maintainer: ZeroDot1 <zerodot1@bk.ru>
pkgname=mellowplayer
_pkgname=MellowPlayer
pkgver=3.5.2
pkgrel=2
pkgdesc="Open source and cross-platform desktop application that runs web-based music streaming 
         services in its own window and provides integration with your desktop."
url='https://github.com/ColinDuquesnoy/MellowPlayer'
license=('GPL')
arch=('x86_64')
depends=('qt5-base' 'qt5-webengine' 'qt5-svg' 'qt5-quickcontrols2' 'qt5-quickcontrols' 'qt5-translations' 'qt5-graphicaleffects' 'xdg-utils' 'libnotify' 'libevent')
makedepends=('qt5-tools' 'cmake' 'mesa')
optdepends=( 'qt5-webengine-widevine: DRM needed for Spotify' 'pepper-flash: needed for Tidal and Deezer')
source=("https://gitlab.com/ColinDuquesnoy/MellowPlayer/-/archive/${pkgver}/MellowPlayer-${pkgver}.tar.gz" 
        "widevine-path.patch")
md5sums=('604a33c9f3608ee7403675969c1de902'
         '67f8c5c6af4b770a4017a5ca9f137b90')

prepare() {
    cd $srcdir/MellowPlayer-${pkgver}
    patch -Np1 -i "${srcdir}/widevine-path.patch" "$srcdir/MellowPlayer-${pkgver}/src/main/share/applications/mellowplayer.desktop"
}

build() {
  cd $srcdir/MellowPlayer-${pkgver}
  export MAKEFLAGS="-j$(nproc)"
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib .
  make 
}

package() {
  cd $srcdir/MellowPlayer-${pkgver}
  make DESTDIR=${pkgdir} install
}

