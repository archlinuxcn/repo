# $Id$
# Maintainer: Eric Bélanger <eric@archlinux.org>

pkgname=imagemagick-fftw
pkgver=6.9.3.8
pkgrel=1
arch=('i686' 'x86_64')
url="http://www.imagemagick.org/"
license=('custom')
makedepends=('libltdl' 'lcms2' 'libxt' 'fontconfig' 'libxext' 'ghostscript'
             'openexr' 'libwmf' 'librsvg' 'libxml2' 'liblqr' 'openjpeg2'
             'opencl-headers' 'libcl' 'libwebp' 'subversion' 'glu' 'fftw')
source=(http://www.imagemagick.org/download/ImageMagick-${pkgver%.*}-${pkgver##*.}.tar.xz{,.asc}
        perlmagick.rpath.patch)
sha1sums=('ab3a16e1ac223153a76c98d20ed6dda98116d91a'
          'SKIP'
          'e143cf9d530fabf3b58023899b5cc544ba93daec')
validpgpkeys=('D8272EF51DA223E4D05B466989AB63D48277377A')

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
    --enable-hdri --with-wmf --with-openexr --with-xml \
    --with-webp --with-gslib --with-gs-font-dir=/usr/share/fonts/Type1 \
    --with-perl --with-perl-options="INSTALLDIRS=vendor" --with-lqr --with-rsvg \
    --enable-opencl --with-openjp2 --without-gvc --without-djvu --without-autotrace \
    --without-jbig --without-fpx --without-dps --with-fftw $EXTRAOPTS
  make
}

check() {
  cd ImageMagick-${pkgver%.*}-${pkgver##*.}
#  make check
}

package() {
  pkgdesc="An image viewing/manipulation program"
  depends=('libltdl' 'lcms2' 'libxt' 'fontconfig' 'libxext' 'liblqr' 'libcl')
  optdepends=('imagemagick-doc: for additional information'
              'ghostscript: for Ghostscript support' 
              'openexr: for OpenEXR support' 
	      'openjpeg2: for JP2 support' 
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
  provides=("imagemagick=$pkgver")
  conflicts=("imagemagick")
  cd ImageMagick-${pkgver%.*}-${pkgver##*.}
  make -j1 DESTDIR="${pkgdir}" install
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/imagemagick/LICENSE"
  install -Dm644 NOTICE "${pkgdir}/usr/share/licenses/imagemagick/NOTICE"
  provides=("imagemagick=$pkgver")
  conflicts=("imagemagick")
#Cleaning
  rm -f "${pkgdir}"/usr/lib/*.la
  provides=("imagemagick=$pkgver")
  conflicts=("imagemagick")
# template start; name=perl-binary-module-dependency; version=1;
if [[ $(find "$pkgdir/usr/lib/perl5/" -name "*.so") ]]; then
	_perlver_min=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]);')
	_perlver_max=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]+1);')
	depends+=("perl>=$_perlver_min" "perl<$_perlver_max")
fi
# template end;
}

