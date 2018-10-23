# Maintainer: Philip Goto <philip.goto@gmail.com>

pkgname=elementary-code
pkgver=3.0
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
sha256sums=('a813b8fc2d9b2972702df6a5a779d150b44e14f8c555e49b4bef8309168b03c1')

build() {
    rm -rf build
    arch-meson code-${pkgver} build
    ninja -v -C build
}

package() {
    DESTDIR="$pkgdir/" ninja -C build install
}
