# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
pkgname=pamac-aur
_pkgver=6.2.7
pkgver=$_pkgver
pkgrel=2
pkgdesc="A Gtk3 frontend for libalpm"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/manjaro/pamac"
license=('GPL3')
depends=('glib2>=2.42' 'json-glib' 'libsoup' 'dbus-glib' 'polkit' 'vte3>=0.38' 'gtk3>=3.22'
         'libnotify' 'desktop-file-utils' 'pacman>=5.0' 'gnutls>=3.4'
         'appstream-glib' 'archlinux-appstream-data')

  optdepends=('polkit-gnome: needed for authentification in Cinnamon, Gnome'
              'lxsession: needed for authentification in Xfce, LXDE etc.'
              'pamac-tray-appindicator: tray icon for KDE')
makedepends=('gettext' 'itstool' 'vala>=0.36' 'meson' 'ninja')
backup=('etc/pamac.conf')
conflicts=('pamac')
provides=('pamac')
options=(!emptydirs)
install=pamac.install

source=("pamac-$pkgver-$pkgrel.tar.gz::$url/archive/v$_pkgver.tar.gz"
        #"git-$pkgver-$pkgrel.patch::https://github.com/manjaro/pamac/compare/v$_pkgver...master.patch"
       )
sha256sums=('0a3f36b5d67ca38f3f535ebd7000b3247e617e89dc8a0dc45628328d8646d58b')

prepare() {
  cd "$srcdir/pamac-$pkgver"
  # patches here
  #patch -p1 -i "$srcdir/git-$pkgver-$pkgrel.patch"

  # adjust version string
  sed -i -e "s|\"$_pkgver\"|\"$pkgver-$pkgrel\"|g" src/manager_window.vala
}

build() {
  cd "$srcdir/pamac-$pkgver"
  mkdir -p builddir
  cd builddir
  meson --prefix=/usr --sysconfdir=/etc

  # build
  ninja
}

package() {
  cd "$srcdir/pamac-$pkgver/builddir"
  
  DESTDIR="$pkgdir" ninja install
  # remove pamac-tray-appindicator
#  rm "$pkgdir/usr/bin/pamac-tray-appindicator"
#  rm "$pkgdir/etc/xdg/autostart/pamac-tray-appindicator.desktop"
}
# vim:set ts=2 sw=2 et:
