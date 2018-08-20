# Maintainer: grimi

_pkgname=fs-uae-launcher
pkgname=fs-uae-launcher-devel
pkgver=2.9.7dev2
pkgrel=2
pkgdesc="Launcher and configuration program for FS-UAE (development version)."
arch=("any")
url="http://fs-uae.net/download-devel"
license=("GPL2")
depends=("fs-uae-devel" "python-pyqt5" "python-setuptools" "python-opengl>=3.1.0"
        "python-lhafile" "hicolor-icon-theme")
optdepends=("p7zip: for .7z zip support")
source=("http://fs-uae.net/devel/${pkgver}/${_pkgname}-${pkgver}.tar.gz")
#source=("http://ppa.launchpad.net/fengestad/devel/ubuntu/pool/main/f/${_pkgname}/${_pkgname}_${pkgver}.orig.tar.gz")
provides=("fs-uae-launcher")
conflicts=("fs-uae-launcher")
sha256sums=('a51fafef1ce8eac66a051402fb19ddcfba1935a1858d616bcc592264fa3deaa6')



prepare() {
   cd ${_pkgname}-${pkgver}
   # fix typing module compatybility problem
   local pyver="$(python -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
   cp -f /usr/lib/python${pyver}/typing.py fstd/typing.py
   # disable included, OpenGL
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

