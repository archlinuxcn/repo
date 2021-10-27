# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/pamac

pkgname=pamac-aur
pkgver=10.2.2
pkgrel=2
_pkgfixver=$pkgver

_commit='125033f1da74b617c9ef3b74c8b26d4156ed7daa'
sha256sums=('ee8a7ef693cce365127bd19adce75b389ed92fbc7da91a0f6c7f0df384e3cff3')

pkgdesc="A Gtk3 frontend, Package Manager based on libalpm with AUR and Appstream support"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://gitlab.manjaro.org/applications/pamac"
license=('GPL3')
depends=('glib2>=2.42' 'json-glib' 'libsoup' 'dbus-glib' 'polkit' 'vte3>=0.38' 'gtk3>=3.22'
         'libnotify' 'desktop-file-utils' 'libpamac-aur>=11.1' 'gnutls>=3.4' 'git'
         'appstream-glib>=0.7.18-1' 'archlinux-appstream-data' 'libhandy' 'git')

optdepends=('polkit-gnome: needed for authentification in Cinnamon, Gnome'
            'lxsession: needed for authentification in Xfce, LXDE etc.')
makedepends=('gettext' 'itstool' 'vala>=0.46' 'gtk3>=3.22' 'asciidoc' 'meson' 'ninja' 'gobject-introspection' 'libappindicator-gtk3' 'xorgproto')
conflicts=('pamac' 'pamac-tray-appindicator')
provides=("pamac=$pkgver-$pkgrel")
options=(!emptydirs !strip)
install=pamac.install
source=("pamac-$pkgver-$pkgrel.tar.gz::$url/-/archive/$_commit/pamac-$_commit.tar.gz")

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
        --sysconfdir=/etc
  ninja
}

package() {
  cd "$srcdir/pamac-$_commit/builddir"
  DESTDIR="$pkgdir" ninja install
  cp -r "$srcdir/pamac-$_commit/data/gnome-shell/pamac-updates@manjaro.org" "$pkgdir/usr/share/gnome-shell/extensions"
}
# vim:set ts=2 sw=2 et:
