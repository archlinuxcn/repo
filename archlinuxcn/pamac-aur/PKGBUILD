# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/pamac
ENABLE_FAKE_GNOME_SOFTWARE=0

pkgname=pamac-aur
pkgver=11.7.3
pkgrel=4
_pkgfixver=$pkgver
_pkgfixvercli=11.7.3
_pkgrelcli=3

_commit='950bb26d7d6025c5d4538c992da41ec67226634c'
_commitcli='1953797ae16a455ace764202e91849284c67b2cb'
sha256sums=('f9e7bad55a174656641dce415b987dddf57092021a32f2043a446e3bb98f18d0'
            '7dc2975934053045171692fd676de2e10955adeca3c48065cf042cf703b5cdd4')

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
