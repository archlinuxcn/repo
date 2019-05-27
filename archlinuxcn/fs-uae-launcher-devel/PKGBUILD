# Maintainer: grimi

_pkgname=fs-uae-launcher
pkgname=fs-uae-launcher-devel
pkgver=2.9.9dev
pkgrel=1
pkgdesc="Launcher and configuration program for FS-UAE (development version)."
arch=("any")
url="http://fs-uae.net/download-devel"
license=("GPL2")
depends=("fs-uae-devel" "python-pyqt5" "python-setuptools" "python-opengl>=3.1.0"
        "python-lhafile" "hicolor-icon-theme")
optdepends=("p7zip: for .7z zip support")
source=("http://fs-uae.net/devel/${pkgver}/${_pkgname}-${pkgver}.tar.gz")
#source=("http://downloadcontent.opensuse.org/repositories/home:/FrodeSolheim:/devel/Debian_9.0/${_pkgname}_${pkgver/dev/~dev}.orig.tar.gz")
provides=("fs-uae-launcher")
conflicts=("fs-uae-launcher")
sha256sums=('16712910028cd3fc0047609ef1d85d94b1843246fad9756b4d8c763412a454a4')



prepare() {
   cd ${_pkgname}-${pkgver}
   ## fix typing module compatybility problem
   #local pyver="$(python -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
   #cp -f /usr/lib/python${pyver}/typing.py fstd/typing.py

   ## disable included, OpenGL
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

