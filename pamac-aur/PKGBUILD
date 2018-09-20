# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
pkgname=pamac-aur
_pkgver=7.0.1
pkgver=7.1.0rc3
#pkgver=$_pkgver
pkgrel=1
_commit=250cad77f395b9521c0560edd39328ee99095456
pkgdesc="A Gtk3 frontend for libalpm"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://gitlab.manjaro.org/applications/pamac"
license=('GPL3')
depends=('glib2>=2.42' 'json-glib' 'libsoup' 'dbus-glib' 'polkit' 'vte3>=0.38' 'gtk3>=3.22'
         'libnotify' 'desktop-file-utils' 'pacman>=5.1' 'gnutls>=3.4'
         'appstream-glib' 'archlinux-appstream-data')

  optdepends=('polkit-gnome: needed for authentification in Cinnamon, Gnome'
              'lxsession: needed for authentification in Xfce, LXDE etc.'
              'pamac-tray-appindicator: tray icon for KDE')
makedepends=('gettext' 'itstool' 'vala>=0.36.6' 'meson' 'ninja' 'git' 'gobject-introspection')
backup=('etc/pamac.conf')
conflicts=('pamac')
provides=('pamac')
options=(!emptydirs)
install=pamac.install

source=(#"pamac-$pkgver-$pkgrel.tar.gz::$url/-/archive/v$_pkgver/$pkgname-v$_pkgver.tar.gz")
        "pamac-$pkgver-$pkgrel.tar.gz::$url/-/archive/$_commit/$pkgname-$_commit.tar.gz")

sha256sums=('7e40ed9c19980fbdc3a3496a56c55999f3d877c798986d39710a9454e9b5c9be')

prepare() {
  mv "$srcdir/pamac-$_commit" "$srcdir/pamac-v$_pkgver"
  cd "$srcdir/pamac-v$_pkgver"
  # patches here
  #patch -p1 -i "$srcdir/git-$pkgver-$pkgrel.patch"

  # adjust version string
  sed -i -e "s|\"$_pkgver\"|\"$pkgver-$pkgrel\"|g" src/version.vala
}

build() {
  cd "$srcdir/pamac-v$_pkgver"
  mkdir -p builddir
  cd builddir
  meson --prefix=/usr --sysconfdir=/etc

  # build
  ninja
}

package() {
  cd "$srcdir/pamac-v$_pkgver/builddir"
  
  DESTDIR="$pkgdir" ninja install
  # remove pamac-tray-appindicator
#  rm "$pkgdir/usr/bin/pamac-tray-appindicator"
#  rm "$pkgdir/etc/xdg/autostart/pamac-tray-appindicator.desktop"
}
# vim:set ts=2 sw=2 et:
