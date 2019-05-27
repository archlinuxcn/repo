# Maintainer: grimi

_pkgname=fs-uae-arcade
pkgname=fs-uae-arcade-devel
pkgver=2.9.9dev
pkgrel=1
pkgdesc="Full-screen game browser for FS-UAE (development version)."
arch=("any")
url="http://fs-uae.net/download-devel"
license=("GPL2")
depends=("fs-uae-devel" "python-pyqt5" "python-setuptools" "python-opengl>=3.1.0"
         "python-lhafile" "hicolor-icon-theme")
source=("http://fs-uae.net/devel/${pkgver}/${_pkgname}-${pkgver}.tar.gz")
#source=("http://downloadcontent.opensuse.org/repositories/home:/FrodeSolheim:/devel/Debian_9.0/${_pkgname}_${pkgver/dev/~dev}.orig.tar.gz")
provides=("fs-uae-game-center")
conflicts=("fs-uae-game-center" "fs-uae-game-center-devel")
replaces=("fs-uae-game-center-devel")
sha256sums=('d05a0de8ef9516e76444005511cb567cc12132e2fc0cc44fe568f93e5d75203b')



prepare() {
   cd ${_pkgname}-${pkgver}
   ## fix typing module compatybility problem
   #local pyver="$(python -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
   #cp -f /usr/lib/python${pyver}/typing.py fstd/typing.py

   ## disable included OpenGL
   sed '/OpenGL/d' -i setup.py
}

build() {
   cd ${_pkgname}-${pkgver}
   make
}

package() {
   cd ${_pkgname}-${pkgver}
   make install DESTDIR="${pkgdir}" prefix=/usr
}


# vim:set ts=3 sw=3 et:

