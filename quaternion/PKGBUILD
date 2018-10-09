# Maintainer: Ivan Semkin (ivan at semkin dot ru)
# Contributor: Martin Weinelt <hexa@darmstadt.ccc.de>
 
appname=Quaternion
pkgname=quaternion
libname=libQMatrixClient
_libname=libqmatrixclient
pkgver=0.0.9.2
_libqmatrixclient_pkgver=0.3.0.2
pkgrel=1
pkgdesc='Qt5-based IM client for the Matrix protocol'
url='https://matrix.org/docs/projects/client/quaternion.html'
arch=('i686' 'x86_64')
license=(GPL3)
depends=(qt5-declarative hicolor-icon-theme)
makedepends=(cmake)
provides=(quaternion)
conflicts=(quaternion-git)
source=("https://github.com/QMatrixClient/Quaternion/archive/v$pkgver.tar.gz"
        "https://github.com/QMatrixClient/libqmatrixclient/archive/v${_libqmatrixclient_pkgver}.tar.gz"
)
sha256sums=('e859b232802ca0ce68a3fd97bd44bf4252718324c95d1d740bc20a1d02bf5568'
            'c363af0c9d1e357000ed3f50af70722a35d6511c6bd2b9faec287da101a7877a')

prepare() {
  cp -r ${_libname}-${_libqmatrixclient_pkgver}/* ${srcdir}/${appname}-${pkgver}/lib/
}

build() {
  mkdir ${appname}-${pkgver}/build_dir -p
  cd ${appname}-${pkgver}/build_dir
  cmake .. -DBUILD_SHARED_LIBS:BOOL=ON
  cmake --build . --target all
}
 
package() {
  cd ${appname}-${pkgver}

  # The binary
  install -Dm755 "build_dir/${pkgname}" -t "${pkgdir}/usr/bin/"

  # .desktop file
  install -Dm644 "linux/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications/"

  # Icons
  install -Dm644 "icons/quaternion/16-apps-quaternion.png" -t "${pkgdir}/usr/share/icons/hicolor/16x16/apps/"
  install -Dm644 "icons/quaternion/22-apps-quaternion.png" -t "${pkgdir}/usr/share/icons/hicolor/22x22/apps/"
  install -Dm644 "icons/quaternion/32-apps-quaternion.png" -t "${pkgdir}/usr/share/icons/hicolor/32x32/apps/"
  install -Dm644 "icons/quaternion/48-apps-quaternion.png" -t "${pkgdir}/usr/share/icons/hicolor/48x48/apps/"
  install -Dm644 "icons/quaternion/64-apps-quaternion.png" -t "${pkgdir}/usr/share/icons/hicolor/64x64/apps/"
  install -Dm644 "icons/quaternion/128-apps-quaternion.png" -t "${pkgdir}/usr/share/icons/hicolor/128x128/apps/"
  install -Dm644 "icons/quaternion/sources/quaternion.svg" -t "${pkgdir}/usr/share/icons/hicolor/scalable/apps/"

  # The lib
  mkdir ${pkgdir}/usr/lib
  mv build_dir/lib/${libname}.so.0.3.0 ${pkgdir}/usr/lib/
  ln -s /usr/lib/${libname}.so.0.3.0 ${pkgdir}/usr/lib/${libname}.so.0
  ln -s /usr/lib/${libname}.so.0.3.0 ${pkgdir}/usr/lib/${libname}.so
}
# vim:set ts=2 sw=2 et:
