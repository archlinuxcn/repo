# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=iotas
pkgver=0.9.4
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
b2sums=('70c5fb5ba0bd6b9e9faa64436d9c661436c7d0905853793f4e35c803e6e01cd9a3a7f66138204cb88c8091a2517729221570b740810256d75009b62f425d9301')

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
