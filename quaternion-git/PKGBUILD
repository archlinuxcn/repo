# Maintainer: Ivan Semkin (ivan at semkin dot ru)
# Contributor: Martin Weinelt <hexa@darmstadt.ccc.de>
 
appname=Quaternion
pkgname=quaternion-git
pkgver=0.0.5.r21.63efb78
pkgrel=2
pkgdesc='Qt5-based IM client for the Matrix protocol'
arch=('any')
url='https://matrix.org/docs/projects/client/quaternion.html'
license=('GPL3')
depends=('qt5-base' 'qt5-declarative' 'qt5-quickcontrols')
makedepends=('git' 'cmake')
provides=('quaternion')
conflicts=('quaternion')
source=('git://github.com/QMatrixClient/Quaternion')
md5sums=('SKIP')

pkgver() {
  cd $appname
  echo "$(git describe --tags | sed 's/^v//; s/-/.r/; s/-g/./')"
}

prepare() {
  cd $appname
  git remote set-url origin https://github.com/QMatrixClient/Quaternion.git
  git submodule update --init --recursive
}
 
build() {
  mkdir $appname/build || true
  cd $appname/build
  cmake ..
  make $MAKEFLAGS
}
 
package() {
  cd $appname

  # The binary
  install -Dm755 "build/quaternion" -t "$pkgdir/usr/bin/"

  # .desktop file
  install -Dm644 "linux/quaternion.desktop" -t "$pkgdir/usr/share/applications/"

  # Icons
  install -Dm644 "icons/quaternion/16-apps-quaternion.png" -t "$pkgdir/usr/share/icons/hicolor/16x16/apps/"
  install -Dm644 "icons/quaternion/22-apps-quaternion.png" -t "$pkgdir/usr/share/icons/hicolor/22x22/apps/"
  install -Dm644 "icons/quaternion/32-apps-quaternion.png" -t "$pkgdir/usr/share/icons/hicolor/32x32/apps/"
  install -Dm644 "icons/quaternion/48-apps-quaternion.png" -t "$pkgdir/usr/share/icons/hicolor/48x48/apps/"
  install -Dm644 "icons/quaternion/64-apps-quaternion.png" -t "$pkgdir/usr/share/icons/hicolor/64x64/apps/"
  install -Dm644 "icons/quaternion/128-apps-quaternion.png" -t "$pkgdir/usr/share/icons/hicolor/128x1128/apps/"
  install -Dm644 "icons/quaternion/sources/quaternion.svg" -t "$pkgdir/usr/share/icons/hicolor/scalable/apps/"
}
# vim:set ts=2 sw=2 et:
