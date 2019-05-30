# Maintainer: grimi

_pkgname=fs-uae-launcher
pkgname=fs-uae-launcher-devel
pkgver=2.9.12dev
pkgrel=1
pkgdesc="Launcher and configuration program for FS-UAE (development version)."
arch=("any")
url="http://fs-uae.net/download-devel"
license=("GPL2")
depends=("fs-uae-devel" "python-pyqt5" "python-setuptools" "python-opengl>=3.1.0"
        "python-requests" "python-lhafile" "hicolor-icon-theme")
optdepends=("p7zip: for .7z zip support")
source=("http://fs-uae.net/devel/${pkgver}/${_pkgname}-${pkgver}.tar.gz")
#source=("http://downloadcontent.opensuse.org/repositories/home:/FrodeSolheim:/devel/Debian_9.0/${_pkgname}_${pkgver/dev/~dev}.orig.tar.gz")
provides=("fs-uae-launcher")
conflicts=("fs-uae-launcher")
sha256sums=('96b4d214ece44739c7b2623afd9dc34fe051ce525ea92891f7852f7dc486b712')



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

