# Contributor: Splex
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=inkscape-gtk3-bzr
pkgver=r14662
pkgrel=1
pkgdesc="An Open Source vector graphics editor, using Scalable Vector Graphics (SVG) file format, built with experimental gtk3 enabled"
url="https://launchpad.net/inkscape"
arch=('i686' 'x86_64')
license=('GPL' 'LGPL')
depends=('aspell' 'gc' 'poppler-glib' 'libxslt' 'gsl' 'imagemagick'
	 'desktop-file-utils' 'gdl>=3.8.0.25' 'gtkmm3' 'python2' 'potrace'
	 'popt' 'dbus-glib' 'libcdr' 'libvisio' 'python2' 'gdk-pixbuf2'
	 'hicolor-icon-theme' 'libexif' )
optdepends=('python2-numpy: some extensions'
            'python2-lxml: some extensions and filters'
            'uniconvertor: reading/writing to some proprietary formats'
 	    'gtkspell3: for spelling'
	    'ruby: for simplepath extension')
makedepends=('boost' 'intltool' 'bzr' 'gettext' 'pango' 'fontconfig')
provides=('inkscape')
conflicts=('inkscape')
options=('!libtool')
source=('inkscape::bzr+http://bazaar.launchpad.net/~inkscape.dev/inkscape/trunk/')
md5sums=('SKIP')
install=inkscape-bzr.install
_bzrmod="inkscape"

pkgver() {
  cd $srcdir/$_bzrmod
  printf "r%s" "$(bzr revno)"
}

prepare() {
  cd "$srcdir/$_bzrmod"
  #fix for inkscape to use python2 with the python 3 package installed.
  sed -i '1s|/usr/bin/python\>|/usr/bin/python2|' cxxtest/*.py
  sed -i '1s|/usr/bin/env python\>|/usr/bin/env python2|g' share/*/{test/,}*.py
  sed -i 's|"python" },|"python2" },|g' src/extension/implementation/script.cpp
  sed -i 's|python -c |python2 -c|g' share/extensions/uniconv*.py
  sed -i 's|"python"|"python2"|g' src/main.cpp
  sed -i '1s|/usr/bin/env python\>|/usr/bin/env python2|g' share/extensions/ink2canvas/svg.py
  sed -i '1s|/usr/bin/env python\>|/usr/bin/env python2|g' share/extensions/ink2canvas/canvas.py
}

build() {
LANG=C
  cd "$srcdir/$_bzrmod"
  [[ -d ../build ]] || mkdir ../build
  export CXXFLAGS+=" `pkg-config --cflags glib` -fPIC -std=c++11"
  ./autogen.sh
  sed -i 's|python -c|python2 -c|g' configure 
  cd ../build
  ../inkscape/configure LIBS='-lpangoft2-1.0 -lfontconfig' \
    --prefix=/usr \
    --without-gnome-vfs \
    --enable-lcms \
    --enable-poppler-cairo \
    --enable-gtk3-experimental \
    --enable-dbusapi \
    --enable-visio \
    --enable-wpg \
    --disable-rpath \
    --enable-binreloc \
    --disable-dependency-tracking
  make 
}

package() {
  cd "$srcdir/build"
  make DESTDIR=$pkgdir install
}
