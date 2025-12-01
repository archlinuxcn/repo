# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/pamac
ENABLE_FAKE_GNOME_SOFTWARE=0

pkgname=pamac-aur
pkgver=11.7.4
pkgrel=1
_pkgfixver=$pkgver
_pkgfixvercli=11.7.4
_pkgrelcli=1

_commit='188905011b64f385c72c5c8f795237bf894390fa'
_commitcli='1ce8a93aeeae71244ecec6d257daae5eea3f3fc4'
sha256sums=('64279615b249aa9d663aa9084b618141dacae83af1a58bc1764cea57b60c77ab'
            'e826479979fcc7818385bb146eb1e9f946bb5543489d9a2b671a2ce45ca31a8d')

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
provides=("pamac=$_pkgfixver-$pkgrel" "pamac-cli=$_pkgfixvercli-$_pkgrelcli")
options=(!emptydirs !strip)
install=pamac.install
source=("pamac-$_pkgfixver-$pkgrel.zip::$url/archive/$_commit.zip"
        "pamac-cli-$_pkgfixvercli-$_pkgrelcli.zip::$urlcli/archive/$_commitcli.zip")

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
  sed -i -e "s|\"$_pkgfixvercli\"|\"$_pkgfixvercli-$__pkgrelcli\"|g" src/version.vala
}

build() {
  cd "${srcdir}/${_srcdir}"
  arch-meson build $define_meson
	meson compile -C build
  cd "${srcdir}/${_srcdircli}"
  arch-meson build
	meson compile -C build
}

package() {
  cd "${srcdir}/${_srcdir}"
#  DESTDIR="$pkgdir" ninja install
  meson install -C build --no-rebuild --destdir "$pkgdir"
  cp -r "$srcdir/pamac-$_commit/data/gnome-shell/pamac-updates@manjaro.org" "$pkgdir/usr/share/gnome-shell/extensions"
  cd "${srcdir}/${_srcdircli}"
  meson install -C build --no-rebuild --destdir "$pkgdir"

  install -Dm644 "${srcdir}/${_srcdir}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
# vim:set ts=2 sw=2 et:
