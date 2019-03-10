# Maintainer: Philip Goto <philip.goto@gmail.com>

pkgname=elementary-code
pkgver=3.1.0
pkgrel=2
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
sha256sums=('445b6101b78156eae96be31ce4b2ab2779545c1d3d7e468e48985738ec3a88ab')

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
