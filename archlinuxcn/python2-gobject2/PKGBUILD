# Maintainer: Michael Kogan (PhotonX) <michael.kogan@gmx.net>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=python2-gobject2
pkgver=2.28.7
pkgrel=7
pkgdesc="Legacy Python 2 bindings for GObject"
url="https://wiki.gnome.org/Projects/PyGObject"
arch=(x86_64)
license=(LGPL)
depends=(glib2 libffi python2)
makedepends=(git)
provides=("pygobject2-devel=$pkgver-$pkgrel")
conflicts=(pygobject2-devel)
replaces=('pygobject2-devel<=2.28.7-3')
_commit=c9594b6a91e6ca2086fedec2ed8249e0a9c029fc  # tags/PYGOBJECT_2_28_7^0
source=("git+https://gitlab.gnome.org/GNOME/pygobject.git#commit=$_commit")
sha256sums=('SKIP')

pkgver() {
  cd pygobject
  git describe --tags | sed 's/^PYGOBJECT_//;s/_/./g;s/-/+/g'
}

prepare() {
  cd pygobject
  find . \( -name '*.py' -o -name '*.py.in' \) -exec sed -i '1s|python$|&2|' {} +
  autoreconf -fvi
}

build() (
  cd pygobject
  CPPFLAGS+=' -Wno-deprecated-declarations'
  ./configure --prefix=/usr --disable-introspection PYTHON=/usr/bin/python2
  sed -i 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
)

package_python2-gobject2() {
  cd pygobject
  make DESTDIR="$pkgdir" install
  rm -r "$pkgdir/usr/share/gtk-doc"
}
