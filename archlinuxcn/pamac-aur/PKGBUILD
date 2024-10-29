# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/pamac
ENABLE_FAKE_GNOME_SOFTWARE=0

pkgname=pamac-aur
pkgver=11.7.2
pkgrel=2
_pkgfixver=$pkgver
_pkgfixvercli=11.7.0


_commit='71ced277e5931ccea2433ece291430481a2694ee'
_commitcli='035e66944ce8633b6362b45ced879f00ba00a09b'
sha256sums=('ca2995fd9605bf9841cfcf8c6e642932e7fe5016c42eeea21ead6bd2a6d97226'
            '98e605a67cf0a72ef74c8521c2ab85aaddb1d95ad075b14fc27bd3165b859694')

pkgdesc="A Gtk frontend, Package Manager based on libalpm with AUR and Appstream support"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/manjaro/pamac"
urlcli="https://github.com/manjaro/pamac-cli"
license=('GPL-3.0-or-later')
depends=('libnotify' 'libhandy' 'libadwaita' 'gtk4' 'desktop-file-utils' 'libpamac-aur>=11.7' 'gnutls>=3.4' 'git')

optdepends=('polkit-gnome: needed for authentification in Cinnamon, Gnome'
            'lxsession: needed for authentification in Xfce, LXDE etc.')
makedepends=('gettext' 'itstool' 'vala' 'meson' 'ninja' 'gobject-introspection' 'xorgproto' 'asciidoc' 'git' 'systemd')
conflicts=('pamac' 'pamac-tray-appindicator' 'pamac-cli')
provides=("pamac=$_pkgfixver-$pkgrel" "pamac-cli=$_pkgfixvercli-$pkgrel")
options=(!emptydirs !strip)
install=pamac.install
source=("pamac-$_pkgfixver-$pkgrel.zip::$url/archive/$_commit.zip"
        "pamac-cli-$_pkgfixvercli-$pkgrel.zip::$urlcli/archive/$_commitcli.zip")

define_meson=''
if [ "${ENABLE_FAKE_GNOME_SOFTWARE}" = 1 ]; then
  conflicts+=('pamac-gnome-integration' 'pamac-gnome-integration-dev' 'gnome-software')
  define_meson+=' -Denable-fake-gnome-software=true'
fi

_srcdir="pamac-$_commit"
_srcdircli="pamac-cli-$_commitcli"

prepare() {
  cd "${srcdir}/${_srcdir}"
  # adjust version string
  sed -i -e "s|\"$_pkgfixver\"|\"$pkgver-$pkgrel\"|g" src/version.vala
  cd "${srcdir}/${_srcdircli}"
  # adjust version string
  sed -i -e "s|\"$_pkgfixvercli\"|\"$_pkgfixvercli-$_pkgrelcli\"|g" src/version.vala
}

build() {
  cd "${srcdir}/${_srcdir}"
  mkdir -p builddir && cd builddir
  meson --buildtype=release \
        --prefix=/usr \
        --sysconfdir=/etc $define_meson
  ninja

  cd "${srcdir}/${_srcdircli}"
  mkdir -p builddir && cd builddir
  meson setup --prefix=/usr --sysconfdir=/etc --buildtype=release
	meson compile
}

package() {
  cd "${srcdir}/${_srcdir}/builddir"
  DESTDIR="$pkgdir" ninja install
  cp -r "$srcdir/pamac-$_commit/data/gnome-shell/pamac-updates@manjaro.org" "$pkgdir/usr/share/gnome-shell/extensions"
  cd "${srcdir}/${_srcdircli}/builddir"
  meson install --destdir "$pkgdir"

  install -Dm644 "${srcdir}/${_srcdir}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
# vim:set ts=2 sw=2 et:
