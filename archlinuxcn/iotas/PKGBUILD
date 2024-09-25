# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=iotas
pkgver=0.9.1
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
b2sums=('37aca8bfab0761242bf8e2384b8451b74992268208df0602500ba6c8ccde1c720c21c4e021ae068595df5e2048bad33cef4ee81b8268743124e2c9bc5e832419')

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
