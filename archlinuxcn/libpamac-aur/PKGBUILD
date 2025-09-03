# Contributor: Zeph <zeph33@gmail.com>
# Maintainer: Zeph <zeph33@gmail.com>
# https://gitlab.manjaro.org/packages/extra/libpamac
ENABLE_FLATPAK=0
ENABLE_SNAPD=0

pkgname=libpamac-aur
pkgver=11.7.3
pkgrel=5
_pkgfixver=$pkgver

_commit='84d9620dd707201b69d9516eda6ac789812efc66'
sha256sums=('13d8dfc2335e0b73d7a93f51d330f0f5dca67c6bc2fa650c94b47829a8c1a74b'
            '6e0c25f0fcb0076ce78845b037e32925fcc3f1cd1670062c48ed35f564a10244'
            'b5236af02c25cd7de4b2c9c2d0f064dac3c2f54da5cc72bf72fc6236a34bd9c4')

pkgdesc="Pamac package manager library based on libalpm"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/manjaro/libpamac/"
license=('GPL-3.0-or-later')
depends=('glib2>=2.42' 'json-glib' 'libsoup3' 'dbus-glib' 'polkit' 'vte3>=0.38' 'libalpm.so=15'
         'libnotify' 'pacman>=7.0' 'gnutls>=3.4' 'appstream'
         'appstream-glib>=0.7.18-1' 'archlinux-appstream-data' 'git')

makedepends=('gettext' 'itstool' 'vala>=0.46'  'asciidoc' 'meson' 'ninja' 'gobject-introspection' 'systemd')
backup=('etc/pamac.conf')
conflicts=('libpamac' 'libpamac-all')
provides=('libpamac.so=11' 'libpamac-appstream.so=11' "libpamac=$_pkgfixver")
options=(!emptydirs !strip)
install=pamac.install
source=("libpamac-$pkgver-$pkgrel.zip::$url/archive/$_commit.zip"
        'fix-appstream-data.sh' 'fix-appstream-data.hook')

define_meson=''
if [ "${ENABLE_FLATPAK}" = 1 ]; then
  depends+=('flatpak')
  define_meson+=' -Denable-flatpak=true'
fi

if [ "${ENABLE_SNAPD}" = 1 ]; then
  depends+=('snapd' 'snapd-glib')
  define_meson+=' -Denable-snap=true'
fi

create_links() {
  # create soname links
  find "$pkgdir" -type f -name '*.so*' ! -path '*xorg/*' -print0 | while read -d $'\0' _lib; do
      _soname=$(dirname "${_lib}")/$(readelf -d "${_lib}" | grep -Po 'SONAME.*: \[\K[^]]*' || true)
      _base=$(echo ${_soname} | sed -r 's/(.*)\.so.*/\1.so/')
      [[ -e "${_soname}" ]] || ln -s $(basename "${_lib}") "${_soname}"
      [[ -e "${_base}" ]] || ln -s $(basename "${_soname}") "${_base}"
  done
}

prepare() {
  cd "$srcdir/libpamac-$_commit"
  # adjust version string
  sed -i -e "s|\"$_pkgfixver\"|\"$pkgver-$pkgrel\"|g" src/version.vala
}

build() {
  cd "$srcdir/libpamac-$_commit"
  arch-meson build -Denable-aur=true -Denable-appstream=true $define_meson
  # build
  meson compile -C build
}

package() {
  cd "$srcdir/libpamac-$_commit"
  meson install -C build --no-rebuild --destdir "$pkgdir"
  # fix appstream issue
  install -Dm644 "$srcdir/fix-appstream-data.hook" "$pkgdir/etc/pacman.d/hooks/fix-appstream-data.hook"
  install -Dm755 "$srcdir/fix-appstream-data.sh" "$pkgdir/etc/pacman.d/hooks.bin/fix-appstream-data.sh"
  create_links

}
# vim:set ts=2 sw=2 et:
