# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/pamac
ENABLE_FAKE_GNOME_SOFTWARE=0

pkgname=pamac-aur
pkgver=11.6.0
pkgrel=1
_pkgfixver=$pkgver
_pkgfixvercli=11.6.0

_commit='9220b38c6dd16bd9c9edb48d9480945c225cb806'
_commitcli='4a68ef57feb6d27c70a101999bcaba795d4d8588'
sha256sums=('7331c5569759494bf9ffa64622857c6428513d65ed9bfa157906f5224ca74367'
            '845573e577a5ba1e7fc6d6b778893b139e102c14918e4264161c5c8bc2b035f6')

pkgdesc="A Gtk3 frontend, Package Manager based on libalpm with AUR and Appstream support"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://gitlab.manjaro.org/applications/pamac"
license=('GPL3')
depends=('libnotify' 'libhandy' 'libadwaita' 'gtk4' 'desktop-file-utils' 'libpamac-aur>=11.6' 'gnutls>=3.4' 'git')

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
