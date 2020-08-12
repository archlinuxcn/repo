# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/pamac
ENABLE_FLATPAK=0
ENABLE_SNAPD=0

pkgname=pamac-aur
pkgver=9.5.7
pkgrel=1
_pkgfixver=$pkgver

_commit='647b30bd208488b2281d16e69036be886495d9f3'
sha256sums=('e74743d44dfe1f239044e00a91182411a48ced079480da37088610f1dd20c993')

pkgdesc="A Gtk3 frontend for libalpm"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://gitlab.manjaro.org/applications/pamac"
license=('GPL3')
depends=('glib2>=2.42' 'json-glib' 'libsoup' 'dbus-glib' 'polkit' 'vte3>=0.38' 'gtk3>=3.22'
         'libnotify' 'desktop-file-utils' 'pacman>=5.2' 'gnutls>=3.4' 'git'
         'appstream-glib' 'archlinux-appstream-data')

optdepends=('polkit-gnome: needed for authentification in Cinnamon, Gnome'
              'lxsession: needed for authentification in Xfce, LXDE etc.'
              'pamac-tray-appindicator: tray icon for KDE')
makedepends=('gettext' 'itstool' 'vala>=0.45' 'meson' 'ninja' 'gobject-introspection' 'xorgproto')
backup=('etc/pamac.conf')
conflicts=('pamac')
provides=("pamac=$pkgver-$pkgrel")
options=(!emptydirs)
install=pamac.install
source=("pamac-$pkgver-$pkgrel.tar.gz::$url/-/archive/$_commit/pamac-$_commit.tar.gz")
define_meson=''
if [ "${ENABLE_FLATPAK}" = 1 ]; then
  depends+=('flatpak')
  define_meson+=' -Denable-flatpak=true'
fi

if [ "${ENABLE_SNAPD}" = 1 ]; then
  depends+=('snapd' 'snapd-glib')
  define_meson+=' -Denable-snap=true'
fi

prepare() {
  cd "$srcdir/pamac-$_commit"
  # adjust version string
  sed -i -e "s|\"$_pkgfixver\"|\"$pkgver-$pkgrel\"|g" src/version.vala
}

build() {
  cd "$srcdir/pamac-$_commit"
  mkdir -p builddir
  cd builddir
  meson --buildtype=release \
        --prefix=/usr \
        --sysconfdir=/etc $define_meson
  # build
  ninja
}

package() {
  cd "$srcdir/pamac-$_commit/builddir"

  DESTDIR="$pkgdir" ninja install
}
# vim:set ts=2 sw=2 et:
