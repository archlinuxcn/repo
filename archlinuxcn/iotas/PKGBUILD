# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=iotas
pkgver=0.9.0
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
b2sums=('6f4cfc40ef811703513b767ca79dd18ce497607df8b1c86c33a55ec14d5e6756eddbb5bd91eb5a9d1b21fb8899a0e4a4310466ef41c5e84fc733b9e2e527158b')

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
