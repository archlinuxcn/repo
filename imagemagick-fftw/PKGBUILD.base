# $Id$
# Maintainer: Eric Bélanger <eric@archlinux.org>

pkgbase=imagemagick
pkgname=('imagemagick' 'imagemagick-doc')
pkgver=6.8.8.7
pkgrel=1
arch=('i686' 'x86_64')
url="http://www.imagemagick.org/"
license=('custom')
makedepends=('libltdl' 'lcms2' 'libxt' 'fontconfig' 'libxext' 'ghostscript'
             'openexr' 'libwmf' 'librsvg' 'libxml2' 'liblqr'
             'opencl-headers' 'libcl' 'libwebp')
#source=(http://www.imagemagick.org/download/ImageMagick-${pkgver%.*}-${pkgver##*.}.tar.xz{,.asc}
source=(ftp://ftp.sunet.se/pub/multimedia/graphics/ImageMagick/ImageMagick-${pkgver%.*}-${pkgver##*.}.tar.xz{,.asc}
        perlmagick.rpath.patch)
sha1sums=('8a8b0d70cc8692c32efbfcb7b739973a2ac39a36'
          'SKIP'
          'e143cf9d530fabf3b58023899b5cc544ba93daec')

prepare() {
  cd ImageMagick-${pkgver%.*}-${pkgver##*.}
  sed '/AC_PATH_XTRA/d' -i configure.ac
  autoreconf --force --install
  patch -p0 -i "${srcdir}/perlmagick.rpath.patch"
}

build() {
  cd ImageMagick-${pkgver%.*}-${pkgver##*.}
  [[ $CARCH = "i686" ]] && EXTRAOPTS="--with-gcc-arch=i686"
  [[ $CARCH = "x86_64" ]] && EXTRAOPTS="--with-gcc-arch=x86-64"

  ./configure --prefix=/usr --sysconfdir=/etc --with-modules \
    --enable-hdri --with-wmf --with-openexr --with-xml --with-lcms2 \
    --with-webp --with-gslib --with-gs-font-dir=/usr/share/fonts/Type1 \
    --with-perl --with-perl-options="INSTALLDIRS=vendor" --with-lqr --with-rsvg \
    --enable-opencl --without-gvc --without-djvu --without-autotrace \
    --without-jbig --without-fpx --without-dps --without-fftw $EXTRAOPTS
  make
}

check() {
  cd ImageMagick-${pkgver%.*}-${pkgver##*.}
#  make check
}

package_imagemagick() {
  pkgdesc="An image viewing/manipulation program"
  depends=('perl' 'libltdl' 'lcms2' 'libxt' 'fontconfig' 'libxext' 'liblqr' 'libcl')
  optdepends=('imagemagick-doc: for additional information'
              'ghostscript: for Ghostscript support' 
              'openexr: for OpenEXR support' 
              'libwmf: for WMF support' 
              'librsvg: for SVG support' 
              'libxml2: for XML support' 
              'libpng: for PNG support' 
	      'libwebp: for WEBP support')
  backup=("etc/ImageMagick-${pkgver%%.*}/coder.xml"
          "etc/ImageMagick-${pkgver%%.*}/colors.xml"
          "etc/ImageMagick-${pkgver%%.*}/delegates.xml"
          "etc/ImageMagick-${pkgver%%.*}/log.xml"
          "etc/ImageMagick-${pkgver%%.*}/magic.xml"
          "etc/ImageMagick-${pkgver%%.*}/mime.xml"
          "etc/ImageMagick-${pkgver%%.*}/policy.xml"
          "etc/ImageMagick-${pkgver%%.*}/quantization-table.xml"
          "etc/ImageMagick-${pkgver%%.*}/thresholds.xml"
          "etc/ImageMagick-${pkgver%%.*}/type.xml"
          "etc/ImageMagick-${pkgver%%.*}/type-dejavu.xml"
          "etc/ImageMagick-${pkgver%%.*}/type-ghostscript.xml"
          "etc/ImageMagick-${pkgver%%.*}/type-windows.xml")
  options=('!docs' 'libtool' '!emptydirs')

  cd ImageMagick-${pkgver%.*}-${pkgver##*.}
  make -j1 DESTDIR="${pkgdir}" install
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/imagemagick/LICENSE"
  install -Dm644 NOTICE "${pkgdir}/usr/share/licenses/imagemagick/NOTICE"

#Cleaning
  rm -f "${pkgdir}"/usr/lib/*.la
}

package_imagemagick-doc() {
  pkgdesc="The ImageMagick documentation (utilities manuals and libraries API)"

  cd ImageMagick-${pkgver%.*}-${pkgver##*.}
  make DESTDIR="${pkgdir}" install-data-html
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/imagemagick-doc/LICENSE"
  install -Dm644 NOTICE "${pkgdir}/usr/share/licenses/imagemagick-doc/NOTICE"
}
