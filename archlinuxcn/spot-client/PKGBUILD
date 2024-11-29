# Maintainer: Manuel Hüsers <aur@huesers.de>
# Contributor: Daniel Peukert <daniel@peukert.cc>
# Contributor: NicoHood <archlinux {cat} nicohood {dog} de>

_projectname='spot'
pkgname="$_projectname-client"
pkgver=0.5.0
pkgrel=1
pkgdesc='Gtk/Rust native Spotify client'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/xou816/$_projectname"
license=('MIT')
depends=('alsa-lib' 'cairo' 'glib2' 'glibc' 'graphene' 'gtk4' 'libadwaita' 'libpulse' 'openssl' 'pango')
optdepends=('org.freedesktop.secrets')
makedepends=('cargo' 'meson>=0.59.0' 'blueprint-compiler>=0.8.1')
checkdepends=('appstream-glib')
options=('!lto') # Build breaks with LTO enabled
source=("https://github.com/xou816/$_projectname/archive/$pkgver/$_projectname-$pkgver.tar.gz"
	'disable-clippy.patch')
sha512sums=('a2acbc2666c3acea86562227b490373bdeff67831bef7275b47e759db366cacbeb2411578f56be824cca6cd72c833e5830db89c203af1c8165e06927eabcf3ec'
            '4e38fff2a5867c46749959ceb0fb16372f12c8f8038b6a33d43e126e741f43e524e1499bb9b514e56b036097aaa0ac5dd149823c2c9eba277ab0ea4f58d5fb55')
validpgpkeys=() # Waiting for https://github.com/xou816/spot/issues/283

_sourcedirectory="$_projectname-$pkgver"
_builddirectory='build'

prepare() {
	cd "$srcdir/$_sourcedirectory/"
	# Disable failing clippy tests
	patch -Np1 < '../disable-clippy.patch'
}

build() {
	cd "$srcdir/"
	# We're not using arch-meson, because upstream recommends using --buildtype 'release'
	# The offline build flag is turned off, as we're not predownloading rust dependencies
	meson setup --prefix '/usr' --libexecdir 'lib' --sbindir 'bin' --buildtype 'release' --wrap-mode 'nodownload' \
		-Db_lto='true' -Db_pie='true' -Doffline='false' "$_sourcedirectory" "$_builddirectory"
	meson compile -C "$_builddirectory"
}

check() {
	cd "$srcdir/"
	meson test -C "$_builddirectory" --timeout-multiplier -1
}

package() {
	cd "$srcdir/"
	meson install -C "$_builddirectory" --destdir "$pkgdir"
	install -Dm644 "$_sourcedirectory/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
