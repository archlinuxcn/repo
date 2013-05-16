# Maintainer: speps <speps at aur dot archlinux dot org>

_uname=lyricat
_commit=1f68d33
pkgbase=hotot
pkgname=hotot
true && pkgname=('hotot-data' 'hotot-gtk2' 'hotot-gtk3' 'hotot-qt4' 'hotot-qt5')
#true && pkgname+=('hotot-kde')
pkgver=0.9.8.14 # identi.ca support is broken
pkgrel=1
pkgdesc="A lightweight & open source microblogging software (twitter identi.ca)"
arch=('any')
url="http://www.hotot.org/"
license=('LGPL3')
makedepends=('cmake' 'intltool' 'python2' 'qt5-webkit')
#makedepends+=('kdebase-runtime')
install="hotot.install"
source=("https://github.com/$_uname/Hotot/archive/$pkgver.tar.gz")
md5sums=('7437f5132a50f7239e1b4bd09f410a17')

build() {
  cd ${srcdir}/Hotot-*
  [ -d bld ] || mkdir bld && cd bld
  cmake .. -DCMAKE_INSTALL_PREFIX=/usr \
           -DWITH_GTK=ON \
           -DWITH_GTK2=ON \
           -DWITH_GTK3=ON \
           -DWITH_QT=ON \
           -DWITH_QT5=ON \
           -DWITH_CHROME=OFF \
           -DPYTHON_EXECUTABLE=/usr/bin/python2
  make
}

package_hotot-data() {
  true && depends=('hicolor-icon-theme')

  cd ${srcdir}/Hotot-*/bld/misc
  DESTDIR="$pkgdir/" cmake -P cmake_install.cmake

  cd ${srcdir}/Hotot-*/bld/po
  DESTDIR="$pkgdir/" cmake -P cmake_install.cmake

  # remove google analytics tracking code (tnx to ianux)
  find "$pkgdir" -name hotot.js -exec \
    sed -i '/\/\/ 7. run track code/,+12d' {} \;
}

package_hotot-qt4() {
  true && arch=('i686' 'x86_64')
  true && depends=('hotot-data' 'qtwebkit')
  true && provides=('hotot-qt')
  true && conflicts=('hotot-qt')
  true && replaces=('hotot-qt')
  cd ${srcdir}/Hotot-*/bld/qt

  DESTDIR="$pkgdir/" cmake -P cmake_install.cmake
}

package_hotot-qt5() {
  true && arch=('i686' 'x86_64')
  true && depends=('hotot-data' 'qt5-webkit')
  cd ${srcdir}/Hotot-*/bld/qt5

  DESTDIR="$pkgdir/" cmake -P cmake_install.cmake
}

#package_hotot-kde() {
#  true && arch=('i686' 'x86_64')
#  true && depends=('hotot-data' 'kdebase-runtime')
#  cd ${srcdir}/Hotot-*/bld/kde

#  DESTDIR="$pkgdir/" cmake -P cmake_install.cmake
#}

package_hotot-gtk2() {
  true && depends=('hotot-data' 'pywebkitgtk' 'python2-notify' 'python2-pycurl'
                   'python2-keybinder2' 'python2-dbus' 'desktop-file-utils')
  true && optdepends=('libappindicator: unity menubar integration')
  cd ${srcdir}/Hotot-*/bld/hotot

  DESTDIR="$pkgdir/" cmake -P cmake_install.cmake

  # bin
  install -Dm755 ../scripts/hotot-gtk2 \
    "$pkgdir/usr/bin/hotot-gtk2"

  # desktop file
  install -Dm644 ../misc/hotot-gtk2.desktop \
    "$pkgdir/usr/share/applications/hotot-gtk2.desktop"
}

package_hotot-gtk3() {
  true && depends=('hotot-data' 'python2-gobject' 'python2-dbus'
                   'python2-pycurl' 'webkitgtk3' 'desktop-file-utils')
  true && optdepends=('libappindicator3: unity menubar integration')
  cd ${srcdir}/Hotot-*/bld/hotot-gir

  DESTDIR="$pkgdir/" cmake -P cmake_install.cmake

  # bin
  install -Dm755 ../scripts/hotot-gtk3 \
    "$pkgdir/usr/bin/hotot-gtk3"

  # desktop file
  install -Dm644 ../misc/hotot-gtk3.desktop \
    "$pkgdir/usr/share/applications/hotot-gtk3.desktop"
}

# vim:set ts=2 sw=2 et:
