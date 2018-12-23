# Maintainer: Philip Goto <philip.goto@gmail.com>

pkgname=elementary-code
pkgver=3.0.1
pkgrel=1
pkgdesc="Code editor designed for elementary OS"
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
url="https://github.com/elementary/code"
license=(GPL3)
depends=(editorconfig-core-c
         granite
         gtksourceview3
         gtkspell3
         libgit2-glib
         libpeas
         vala
         vte3
         webkit2gtk
         zeitgeist)
makedepends=(editorconfig-core-c
             git
             gobject-introspection
             granite
             gtksourceview3
             libgit2-glib
             libpeas
             meson
             vala
             zeitgeist)
conflicts=(elementary-code-git)
source=("https://github.com/elementary/code/archive/${pkgver}.tar.gz")
sha256sums=('c693c7167bebd6b324a8dc56ae6d5cbbf568af4dd382cd6c7b0ffe421f0906eb')

build() {
    arch-meson code-${pkgver} build
    ninja -C build
}

check() {
    ninja -C build test
}

package() {
    DESTDIR="$pkgdir/" ninja -C build install
}
