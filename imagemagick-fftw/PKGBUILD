# $Id$
# Maintainer: Eric Bélanger <eric@archlinux.org>

pkgbase=imagemagick-fftw
pkgname=(libmagick-fftw imagemagick-fftw)
pkgver=7.0.7.27
pkgrel=2
pkgdesc="An image viewing/manipulation program"
url="https://www.imagemagick.org/"
arch=(x86_64)
license=(custom)
depends=(libltdl lcms2 fontconfig libxext liblqr libraqm libpng libxml2)
makedepends=(ghostscript openexr libwmf librsvg libxml2 openjpeg2 libraw opencl-headers libwebp
             chrpath ocl-icd glu ghostpcl ghostxps 'fftw')
checkdepends=(gsfonts ttf-dejavu)
_relname=ImageMagick-${pkgver%%.*}
_tarname=ImageMagick-${pkgver%.*}-${pkgver##*.}
source=(https://www.imagemagick.org/download/$_tarname.tar.xz{,.asc}
        arch-fonts.diff)
sha256sums=('543776f09d69e3ca29b1b83a9c0223185ba26bec673593840b4d7face6ea253b'
            'SKIP'
            'a85b744c61b1b563743ecb7c7adad999d7ed9a8af816650e3ab9321b2b102e73')
validpgpkeys=(D8272EF51DA223E4D05B466989AB63D48277377A)  # Lexie Parsimoniae

shopt -s extglob

prepare() {
  mkdir -p binpkg/usr/lib/pkgconfig {binpkg,docpkg}/usr/share

  cd $_tarname

  # Fix up typemaps to match our packages, where possible
  patch -Np1 -i ../arch-fonts.diff

  # Don't run auto(re)conf; assumes use of git
}

build() {
  cd $_tarname
  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --with-dejavu-font-dir=/usr/share/fonts/TTF \
    --with-gs-font-dir=/usr/share/fonts/gsfonts \
    PSDelegate=/usr/bin/gs \
    XPSDelegate=/usr/bin/gxps \
    PCLDelegate=/usr/bin/gpcl6 \
    --enable-hdri \
    --enable-opencl \
    --with-gslib \
    --with-lqr \
    --with-modules \
    --with-openexr \
    --with-openjp2 \
    --with-perl \
    --with-perl-options=INSTALLDIRS=vendor \
    --with-rsvg \
    --with-webp \
    --with-wmf \
    --with-xml \
    --without-autotrace \
    --without-djvu \
    --without-dps \
    --with-fftw \
    --without-fpx \
    --without-gcc-arch \
    --without-gvc \
    --without-jbig
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

check() (
  cd $_tarname
  ulimit -n 4096
  make check
)

package_libmagick-fftw() {
  provides=("libmagick=$pkgver")
  conflicts=("libmagick")
  pkgdesc+=" (library)"
  optdepends=('ghostscript: PS/PDF support'
              'libraw: DNG support'
              'librsvg: SVG support'
              'libwebp: WEBP support'
              'libwmf: WMF support'
              'libxml2: Magick Scripting Language'
              'ocl-icd: OpenCL support'
              'openexr: OpenEXR support'
              'openjpeg2: JPEG2000 support'
              'pango: Text rendering')
  backup=(etc/$_relname/{coder,colors,delegates,log,magic,mime,policy,quantization-table,thresholds,type,type-{dejavu,ghostscript}}.xml)
  options=('!emptydirs' libtool)

  cd $_tarname
  make DESTDIR="$pkgdir" install

  rm "$pkgdir"/etc/$_relname/type-{apple,urw-base35,windows}.xml
  rm "$pkgdir"/usr/lib/*.la

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 LICENSE NOTICE

# Split 'imagemagick'
  cd ../binpkg
  mv "$pkgdir/usr/bin" usr/
  mv "$pkgdir/usr/lib/perl5" usr/lib/
  mv "$pkgdir/usr/share/man" usr/share/

# Split docs
  mv "$pkgdir/usr/share/doc" "$srcdir/docpkg/usr/share/"
}

package_imagemagick-fftw() {
  provides=("imagemagick=$pkgver")
  conflicts=("imagemagick")
  depends=("libmagick-fftw=$pkgver-$pkgrel")
  optdepends=('imagemagick-doc: manual and API docs')
  options=('!emptydirs')

  mv binpkg/* "$pkgdir"

  find "$pkgdir/usr/lib/perl5" -name '*.so' -exec chrpath -d {} +

# template start; name=perl-binary-module-dependency; version=1;
if [[ $(find "$pkgdir/usr/lib/perl5/" -name "*.so") ]]; then
        _perlver_min=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]);')
        _perlver_max=$(perl -e '$v = $^V->{version}; print $v->[0].".".($v->[1]+1);')
        depends+=("perl>=$_perlver_min" "perl<$_perlver_max")
fi
# template end;

  cd $_tarname
  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 LICENSE NOTICE
}

