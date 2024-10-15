# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=iotas
pkgver=0.9.3
pkgrel=1
pkgdesc="Simple note taking"
arch=('any')
url="https://gitlab.gnome.org/World/iotas"
license=('GPL3')
depends=('libadwaita' 'python' 'gtksourceview5')
makedepends=('meson' 'gobject-introspection')
checkdepends=('appstream-glib')
optdepends=(
	'aspell: spell check.'
	'hspell: hebrew spell check.'
	'nuspell: spell check, depends on hunspell dictionary.'
	'hunspell: spell check.'
)
source=("$url/-/archive/$pkgver/$pkgname-$pkgver.tar.gz")
b2sums=('d78d797f187a2b00b110eb1d0a5404ff2dfcc5f7de17b1c19fec1bc755c796c7d010bc918581bfdf62e13e4353a8e37a34694a464a750470ab8ca2da508d6973')

_srcdir="$pkgname-$pkgver"

build() {
	arch-meson "$_srcdir" 'build'
	meson compile -C 'build'
}

check() {
	meson test -C 'build' --print-errorlogs || :
}

package() {
	depends+=(
		'webkitgtk-6.0'
		'python-requests'
		'python-markdown-it-py'
		'python-linkify-it-py'
		'python-mdit_py_plugins'
		'python-gtkspellcheck'
		'python-strenum'
		'libvoikko'
		'sqlite'
		'org.freedesktop.secrets')

	meson install -C 'build' --destdir "$pkgdir"
}
