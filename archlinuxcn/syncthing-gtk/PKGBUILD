# Maintainer: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Martin Wimpress <code@flexion.org>
# Contributor: kozec <kozec at kozec dot com>

pkgname=syncthing-gtk
pkgver=0.9.4.4
pkgrel=2
epoch=1
pkgdesc='GTK3 based GUI and notification area icon for Syncthing'
arch=('any')
url='https://github.com/syncthing/syncthing-gtk'
license=('GPL2')
depends=('syncthing>=0.14.50' 'gtk3' 'libnotify' 'python2-bcrypt'
         'python2-cairo' 'python2-dateutil' 'python2-gobject')
makedepends=('python2-setuptools')
source=($pkgname-$pkgver.tar.gz::https://github.com/syncthing/$pkgname/archive/v$pkgver.tar.gz
        kde-statusicon.patch)
sha256sums=('896ddaaba4ad0b8f090c5a381a28b3da759932314562cdd50ca288543b03ddcc'
            '109d8c970045e60251fc64865f05322b23a0995ee6725be02905941cb3a1ae0d')

prepare() {
  cd $pkgname-$pkgver

  # Enable Gtk.StatusIcon in KDE
  patch -Np1 -i ../kde-statusicon.patch
}

build() {
  cd $pkgname-$pkgver
  python2 setup.py build
}

package() {
  cd $pkgname-$pkgver
  python2 setup.py install --root="${pkgdir}" --optimize=1
}
