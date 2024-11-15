# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=iotas
pkgver=0.9.5
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
b2sums=('30c55f00f43abf7a7bc6ee7f76e4ef55ec2c0e7dd857e6621a1bb9e87f947099e8bc96d82acc2b4e7ef438a1c37ab384d23ab7a5228743a88951f01fa40aa7f1')

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
