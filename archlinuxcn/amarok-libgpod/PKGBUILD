# Maintainer: Antonio Rojas <arojas@archlinux.org>

pkgname=amarok-libgpod
pkgver=3.3.3
pkgrel=1
pkgdesc='Powerful music player that lets you rediscover your music. Built with iPod support.'
arch=(x86_64)
license=(GPL-2.0-or-later)
url='https://apps.kde.org/amarok/'
provides=(amarok)
conflicts=(amarok)
depends=(ffmpeg
         fftw
         glib2
         glibc
         gst-plugins-base
         gstreamer
         karchive
         kcodecs
         kcolorscheme
         kcompletion
         kconfig
         kconfigwidgets
         kcoreaddons
         kcrash
         kdbusaddons
         kdnssd
         kglobalaccel
         kguiaddons
         ki18n
         kiconthemes
         kitemviews
         kcmutils
         kio
         kirigami
         knotifications
         kpackage
         kstatusnotifieritem
         ktexteditor
         ktextwidgets
         kwallet
         kwidgetsaddons
         kwindowsystem
         kxmlgui
         libmtp
         libmygpo-qt6
         libstdc++
         mariadb
         mariadb-libs
         qt6-base
         qt6-declarative
         qt6-svg
         qt6-tools
         qt6-webengine
         solid
         taglib
         threadweaver
	 libgpod
)

makedepends=(extra-cmake-modules
             kdoctools)
source=(https://download.kde.org/stable/amarok/$pkgver/amarok-$pkgver.tar.xz)
sha256sums=('68e9e83d7d8c0cbdd470958e768815f573d61f3ce32be7bc1b87fb56d622436e')

build() {
  cmake -B build -S amarok-$pkgver \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
