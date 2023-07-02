# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/pamac
ENABLE_FAKE_GNOME_SOFTWARE=0

pkgname=pamac-aur
pkgver=11.0.1
pkgrel=2
_pkgfixver=$pkgver
_pkgfixvercli=11.0.0

_commit='69d08b62a5217dbc98ffdea41718bf6e3a292dd6'
_commitcli='67b7eaa139af25530b4b10788b7b3b4884b9c2ed'
sha256sums=('057c6936b2059fd58a4dac143cefb82b9ea0607c25555a42b1d7414d80af53cf'
            '3addc587fd1605b41b942a073db086624e528009a981d265f5282d0c2a43c076')

pkgdesc="A Gtk3 frontend, Package Manager based on libalpm with AUR and Appstream support"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://gitlab.manjaro.org/applications/pamac"
license=('GPL3')
depends=('libnotify' 'libpamac-aur' 'libhandy' 'libadwaita' 'gtk4' 'desktop-file-utils' 'libpamac-aur>=11.5' 'gnutls>=3.4' 'git')

optdepends=('polkit-gnome: needed for authentification in Cinnamon, Gnome'
            'lxsession: needed for authentification in Xfce, LXDE etc.')
makedepends=('gettext' 'itstool' 'vala' 'meson' 'ninja' 'gobject-introspection' 'xorgproto' 'asciidoc' 'git')
conflicts=('pamac' 'pamac-tray-appindicator' 'pamac-cli')
provides=("pamac=$_pkgfixver-$pkgrel" "pamac-cli=$_pkgfixvercli-$pkgrel")
options=(!emptydirs !strip)
install=pamac.install
source=("pamac-$_pkgfixver-$pkgrel.tar.gz::$url/-/archive/$_commit/pamac-$_commit.tar.gz"
        "pamac-cli-$_pkgfixvercli-$pkgrel.tar.gz::$url-cli/-/archive/$_commitcli/pamac-cli-$_commitcli.tar.gz")

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
  sed -i -e "s|\"$_pkgfixvercli\"|\"$_pkgfixvercli-$pkgrel\"|g" src/version.vala
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
