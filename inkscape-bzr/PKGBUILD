# Contributor: Splex
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=inkscape-bzr
pkgver=r15054
pkgrel=1
pkgdesc="An Open Source vector graphics editor, using Scalable Vector Graphics (SVG) file format, built with experimental gtk3 enabled"
url="https://launchpad.net/inkscape"
arch=('i686' 'x86_64')
license=('GPL' 'LGPL')
depends=('aspell' 'gc' 'poppler-glib' 'libxslt' 'gsl' 'imagemagick'
	 'gdl>=3.8.0.25' 'gtkmm3' 'python2' 'potrace' 'libcdr' 'libvisio'
	 'gnome-vfs' )
optdepends=('python2-numpy: some extensions'
            'python2-lxml: some extensions and filters'
            'uniconvertor: reading/writing to some proprietary formats'
 	    'gtkspell3: for spelling'
	    'ruby: for simplepath extension')
makedepends=('cmake' 'boost' 'intltool' 'bzr' 'gettext' 'pango' 'fontconfig')
provides=('inkscape')
conflicts=('inkscape')
options=('!libtool' '!makeflags')
source=('inkscape::bzr+http://bazaar.launchpad.net/~inkscape.dev/inkscape/trunk/')
md5sums=('SKIP')
_bzrmod="inkscape"

pkgver() {
  cd "$srcdir/$_bzrmod"
  printf "r%s" "$(bzr revno)"
}

prepare() {
  cd "$srcdir/$_bzrmod"
  sed -i '1s|/usr/bin/env python\>|/usr/bin/env python2|g' share/extensions/*.py
}

build() {
  cd "$srcdir/$_bzrmod"
  
  [[ -d build ]] || mkdir build
  cd build
  cmake .. -DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_BUILD_TYPE=Release \
	-DWITH_DBUS=OFF
  make 
}

package() {
  cd "$srcdir/$_bzrmod"/build
  make DESTDIR=$pkgdir install
}
