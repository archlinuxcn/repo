# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/libpamac
ENABLE_FLATPAK=0
ENABLE_SNAPD=0

pkgname=libpamac-aur
pkgver=11.3.1
pkgrel=0
_pkgfixver=$pkgver

_commit='9b64211cc08d8ec27df98c157261b8b9c04d11df'
sha256sums=('9fccd36b994305d4fb02c9950127b795c6d244454d720a972bf48fd85e21394b'
            '6e0c25f0fcb0076ce78845b037e32925fcc3f1cd1670062c48ed35f564a10244'
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
        --sysconfdir=/etc $define_meson
  # build
  meson compile
}

package() {
  cd "$srcdir/libpamac-$_commit/builddir"
  DESTDIR="$pkgdir" ninja install
  # fix appstream issue
  install -Dm644 "$srcdir/fix-appstream-data.hook" "$pkgdir/etc/pacman.d/hooks/fix-appstream-data.hook"
  install -Dm755 "$srcdir/fix-appstream-data.sh" "$pkgdir/etc/pacman.d/hooks.bin/fix-appstream-data.sh"  

}
# vim:set ts=2 sw=2 et:
