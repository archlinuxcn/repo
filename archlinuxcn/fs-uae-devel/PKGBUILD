# Maintainer: grimi

_pkgname=fs-uae
pkgname=fs-uae-devel
pkgver=2.9.12dev
pkgrel=2
pkgdesc="Cross-platform Amiga emulator based on UAE/WinUAE (development version)."
arch=("i686" "x86_64")
url="http://fs-uae.net/download-devel"
license=("GPL2")
depends=("sdl2" "libpng" "openal" "mesa" "libxi" "libmpeg2" "gettext" "freetype2" "hicolor-icon-theme"
         "desktop-file-utils" "shared-mime-info") # 'glib2' provided by 'gettext', 'zlib' by 'libpng'
makedepends=('zip')
source=("http://fs-uae.net/devel/${pkgver}/${_pkgname}-${pkgver}.tar.gz")
#source=("http://downloadcontent.opensuse.org/repositories/home:/FrodeSolheim:/devel/Debian_9.0/${_pkgname}_${pkgver/dev/~dev}.orig.tar.gz")
provides=("fs-uae")
conflicts=("fs-uae")
sha256sums=('995cc6972afdc43f9950308430efe73a9a51188f90e87e75680e8fc64b29c66f')

#MAKEFLAGS="-j1"
CXXFLAGS="$CXXFLAGS -Wno-narrowing"


build() {
   cd ${_pkgname}-${pkgver}

   ./configure --prefix=/usr
   make
}



package() {
   cd ${_pkgname}-${pkgver}

   make install DESTDIR="${pkgdir}"
}


# vim:set ts=3 sw=3 sts=3 et:

