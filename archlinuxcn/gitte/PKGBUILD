# Maintainer: George Hu <integral@archlinux.org>

pkgname=gitte
_srcname=Gitte
pkgver=0.7.0
pkgrel=1
pkgdesc="A GTK4/libadwaita Git client for the GNOME desktop"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://codeberg.org/ckruse/${_srcname}"
license=('AGPL-3.0-or-later')
depends=(
	'cairo'
	'dconf'
	'glib2'
	'glibc'
	'graphene'
	'gtk4'
	'hicolor-icon-theme'
	'libadwaita'
	'libgcc'
	'libgit2'
	'libssh2'
	'openssl'
	'pango'
	'xz'
	'zlib'
)
makedepends=('cargo' 'git' 'meson' 'ninja')
source=("git+${url}.git#tag=${pkgver}")
sha256sums=('271f02a23277b6802aaae5297732deced23e39f56ffb825ffd757abd69657518')

build() {
	export CFLAGS+=" -ffat-lto-objects"
	export LIBSSH2_SYS_USE_PKG_CONFIG=1
	meson setup --prefix=/usr --libexecdir=lib --buildtype=release build "${_srcname}"
	meson compile -C build
}

check() {
	meson test -C build --print-errorlogs
}

package() {
	meson install -C build --no-rebuild --destdir "${pkgdir}"
}
