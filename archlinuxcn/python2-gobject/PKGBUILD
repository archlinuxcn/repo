# Maintainer: Bruno Pagani <archange@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Ionut Biru <ibiru@archlinux.org>

pkgname=python2-gobject
pkgver=3.36.1
pkgrel=5
pkgdesc="Python 2 Bindings for GLib/GObject/GIO/GTK+"
url="https://wiki.gnome.org/Projects/PyGObject"
arch=(x86_64)
license=(LGPL)
depends=(gobject-introspection-runtime python2)
makedepends=(python2-cairo gobject-introspection git meson)
optdepends=('cairo: Cairo bindings')
_commit=5c6bee1c2a0d08cf367aa61784b5b967128e68b2  # tags/3.36.1^0
source=("git+https://gitlab.gnome.org/GNOME/pygobject.git#commit=$_commit")
sha256sums=('SKIP')

build() {
  arch-meson pygobject build -D python=/usr/bin/python2
  meson compile -C build
}

package_python2-gobject() {
  DESTDIR="$pkgdir" meson install -C build
  python2 -m compileall -d /usr/lib "$pkgdir/usr/lib"
  python2 -O -m compileall -d /usr/lib "$pkgdir/usr/lib"

  # Remove devel stuff conflicting with python-gobject
  rm -r "$pkgdir"/usr/{include,lib/pkgconfig}
}
