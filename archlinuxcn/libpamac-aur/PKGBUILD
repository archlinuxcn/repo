# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/pamac
ENABLE_FLATPAK=0
ENABLE_SNAPD=0

pkgname=libpamac-aur
pkgver=11.1.3
pkgrel=1
_pkgfixver=$pkgver

_commit='da8af3e20df847f64437d1e4e279796a27a735f1'
sha256sums=('ec0ec7a076e1c789258ce0dd71f5cf76cf608c395563138f5c1f2eb3e490a4a9'
            'e9fe7c14d15cbce1d337749cf317e4460bce485b102b5c228b7efa479998d4fa'
            'c2b943318a01ba1f3dabbf32e48e6a6f4b4b774e167ab86c6bfee31aa4a3424c')

pkgdesc="Pamac package manager library based on libalpm"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://gitlab.manjaro.org/applications/libpamac"
license=('GPL3')
depends=('glib2>=2.42' 'json-glib' 'libsoup' 'dbus-glib' 'polkit' 'vte3>=0.38' 
         'libnotify' 'pacman>=6.0' 'pacman<6.1' 'gnutls>=3.4' 'git'
         'appstream-glib>=0.7.18-1' 'archlinux-appstream-data' 'git')

makedepends=('gettext' 'itstool' 'vala>=0.46'  'asciidoc' 'meson' 'ninja' 'gobject-introspection')
backup=('etc/pamac.conf')
conflicts=('libpamac' 'libpamac-all')
provides=('libpamac')
options=(!emptydirs !strip)
install=pamac.install
source=("libpamac-$pkgver-$pkgrel.tar.gz::$url/-/archive/$_commit/libpamac-$_commit.tar.gz"
        fix-appstream-data.sh fix-appstream-data.hook)

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
  cd "$srcdir/libpamac-$_commit"
  # adjust version string
  sed -i -e "s|\"$_pkgfixver\"|\"$pkgver-$pkgrel\"|g" src/version.vala
}

build() {
  cd "$srcdir/libpamac-$_commit"
  mkdir -p builddir
  cd builddir
  meson setup --buildtype=release \
        --prefix=/usr \
        -Denable-appindicator=true \
        --sysconfdir=/etc $define_meson
  # build
  ninja
}

package() {
  cd "$srcdir/libpamac-$_commit/builddir"
  DESTDIR="$pkgdir" ninja install
  # fix appstream issue
  install -Dm644 "$srcdir/fix-appstream-data.hook" "$pkgdir/etc/pacman.d/hooks/fix-appstream-data.hook"
  install -Dm755 "$srcdir/fix-appstream-data.sh" "$pkgdir/etc/pacman.d/hooks.bin/fix-appstream-data.sh"  

}
# vim:set ts=2 sw=2 et:
