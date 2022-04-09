# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/pamac
ENABLE_FAKE_GNOME_SOFTWARE=0

pkgname=pamac-aur
pkgver=10.4.0
pkgrel=0
_pkgfixver=$pkgver

_commit='c7db90d14c1c4ea71a5255d974d9b2722402a459'
sha256sums=('57ea71c69612f8dc7acafe77f2312b2c6728e14bf9c2b6126bc4889be796ae09')

pkgdesc="A Gtk3 frontend, Package Manager based on libalpm with AUR and Appstream support"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://gitlab.manjaro.org/applications/pamac"
license=('GPL3')
depends=('glib2>=2.42' 'json-glib' 'libsoup' 'dbus-glib' 'polkit' 'vte3>=0.38' 'gtk3>=3.24'
         'libnotify' 'desktop-file-utils' 'libpamac-aur>=11.2' 'gnutls>=3.4' 'git'
         'appstream-glib>=0.7.18-1' 'archlinux-appstream-data' 'libhandy' 'git')

optdepends=('polkit-gnome: needed for authentification in Cinnamon, Gnome'
            'lxsession: needed for authentification in Xfce, LXDE etc.')
makedepends=('gettext' 'itstool' 'vala>=0.46' 'gtk3>=3.24' 'asciidoc' 'meson' 'ninja' 'gobject-introspection' 'libappindicator-gtk3' 'xorgproto')
conflicts=('pamac' 'pamac-tray-appindicator')
provides=("pamac=$pkgver-$pkgrel")
options=(!emptydirs !strip)
install=pamac.install
source=("pamac-$pkgver-$pkgrel.tar.gz::$url/-/archive/$_commit/pamac-$_commit.tar.gz")

define_meson=''
if [ "${ENABLE_FAKE_GNOME_SOFTWARE}" = 1 ]; then
  conflicts+=('pamac-gnome-integration' 'pamac-gnome-integration-dev' 'gnome-software')
  define_meson+=' -Denable-fake-gnome-software=true'
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
  ninja
}

package() {
  cd "$srcdir/pamac-$_commit/builddir"
  DESTDIR="$pkgdir" ninja install
  cp -r "$srcdir/pamac-$_commit/data/gnome-shell/pamac-updates@manjaro.org" "$pkgdir/usr/share/gnome-shell/extensions"
}
# vim:set ts=2 sw=2 et:
