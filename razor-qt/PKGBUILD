# Contributor: Sergio Montesinos <sermonpe@yahoo.es>
pkgname=razor-qt
pkgver=0.5.2
pkgrel=5
pkgdesc="Razor is a toolbox-like desktop-environment"
url="http://razor-qt.org"
arch=('i686' 'x86_64' 'armv6h' )
license="GPL2"
depends=('qt4' 'polkit-qt' 'udev' 'libxrender' 'libxcomposite' 'libxdamage' 'zlib' 'file' 'libxcursor' 'libstatgrab' 'icu')
makedepends=('cmake')
optdepends=('openbox: Razor-qt works with various WM, but most of Razor developers use Openbox.'
            'upower: To Shutdown/Reboot from Razor'
            'udisks: For the Removable Media plugin to work'
            'qxkb: Keyboard layout switching'
	    'razor-lightdm-greeter'
            )
conflicts=('razor-qt-git')
source=("http://razor-qt.org/downloads/razorqt-${pkgver}.tar.bz2")
md5sums=('8b2da8ab69065926bfc998cf1960bffb')

build() {
  cd "${srcdir}/razorqt-${pkgver}"
  cmake ./ -DCMAKE_INSTALL_PREFIX=/usr -DQT_QMAKE_EXECUTABLE=qmake-qt4 -DLIB_SUFFIX="" -DENABLE_LIGHTDM_GREETER=OFF -DMODULE_LIGHTDM=OFF
  make
}
 
package() {
  cd "${srcdir}/razorqt-${pkgver}"
  make DESTDIR="${pkgdir}" install
}

