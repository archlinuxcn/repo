# Contributor: Splex
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=inkscape-bzr
pkgver=r15536
pkgrel=1
pkgdesc="An Open Source vector graphics editor, using SVG file format, from bzr trunk"
url="https://launchpad.net/inkscape"
arch=('i686' 'x86_64')
license=('GPL' 'LGPL')
depends=('aspell' 'gc' 'poppler-glib' 'libxslt' 'gsl' 'imagemagick' 'libyaml' 'potrace'
	 'gdl>=3.8.0.25' 'gtkmm3' 'libcdr' 'libvisio' 'popt' 'python2' 'dbus-glib')
optdepends=('python2-numpy: some extensions'
            'python2-lxml: some extensions and filters'
            'uniconvertor: reading/writing to some proprietary formats'
 	    'gtkspell3: for spelling'
	    'ruby: for simplepath extension')
makedepends=('cmake' 'boost' 'intltool' 'bzr' 'gettext' 'pango' 'python' 'fontconfig')
provides=('inkscape')
conflicts=('inkscape')
options=('!libtool' '!buildflags' '!makeflags')
source=('inkscape::bzr+http://bazaar.launchpad.net/~inkscape.dev/inkscape/trunk/')
sha1sums=('SKIP')
_bzrmod="inkscape"

pkgver() {
  cd "$srcdir/$_bzrmod"
  printf "r%s" "$(bzr revno)"
}

prepare() {
  cd "$srcdir/$_bzrmod"
  sed -i 's|"python"|"python2"|g' src/main.cpp
  find share -type f -name "*.py" -exec \
       sed -i '1s|/usr/bin/env python\>|/usr/bin/env python2|g' {} \;
  sed -i '1s|/usr/bin/env python3\>|/usr/bin/env python2|g' CMakeScripts/cmake_consistency_check.py
}

build() {
  cd "$srcdir/$_bzrmod"
  [[ -d build ]] || mkdir build
  cd build
  
  cmake .. \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_BUILD_TYPE=RELEASE \
	-DWITH_GNOME_VFS=OFF \
	-DWITH_DBUS=ON
  make 
}

package() {
  cd "$srcdir/$_bzrmod/build"
  make DESTDIR=$pkgdir install
}

