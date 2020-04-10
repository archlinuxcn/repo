# Maintainer: Jan de Groot <jgc@archlinux.org>
# Contributor: Sarah Hay <sarahhay@mb.sympatico.ca>

pkgname=pygtk
pkgver=2.24.0
pkgrel=11
pkgdesc="Python bindings for the GTK widget set"
url="http://www.pygtk.org/"
arch=('x86_64')
license=('LGPL')
depends=('libglade' 'python2-cairo' 'python2-gobject2')
makedepends=('python2-numpy' 'pygobject2-devel')
optdepends=('python2-numpy')
source=(https://download.gnome.org/sources/${pkgname}/${pkgver%.*}/${pkgname}-${pkgver}.tar.bz2
        "https://gitlab.gnome.org/Archive/pygtk/-/commit/4aaa48eb80c6802aec6d03e5695d2a0ff20e0fc2.patch"
        python27.patch
        fix-leaks-of-pango-objects.patch)
sha256sums=('cd1c1ea265bd63ff669e92a2d3c2a88eb26bcd9e5363e0f82c896e649f206912'
            '45700d4e048aeb353a71c9aa182b8299ddfb485e00845045561660ef7317bbbc'
            '39a30456cba055a452bb55c74ef1ff2f5f7bfaad22855b4dd569ab009b56b682'
            '0ca9e910e9bb88897089dd19752a419aa78de15463df766cb19a1d0c2dd45bcb')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  # https://bugzilla.gnome.org/show_bug.cgi?id=623965
  patch -Np1 -i "${srcdir}/python27.patch"

  # https://bugzilla.gnome.org/show_bug.cgi?id=660216
  patch -Np1 -i "${srcdir}/fix-leaks-of-pango-objects.patch"

  # fix build with new pango:
  # https://gitlab.gnome.org/Archive/pygtk/-/merge_requests/1
  patch -p1 -i ../4aaa48eb80c6802aec6d03e5695d2a0ff20e0fc2.patch

  # Python 2
  sed -i -e 's#env python$#env python2#' examples/pygtk-demo/{,demos/}*.py

  # No docs
  sed -i '/^SUBDIRS =/s/docs//' Makefile.in
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  PYTHON=/usr/bin/python2 ./configure --prefix=/usr --disable-docs
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  install -m644 gtk/gtk-extrafuncs.defs "${pkgdir}/usr/share/pygtk/2.0/defs/"
}
