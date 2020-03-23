# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgbase=imagemagick-fftw
pkgname=(imagemagick-fftw)
pkgver=7.0.10.2
pkgrel=2
pkgdesc="An image viewing/manipulation program"
url="https://www.imagemagick.org/"
arch=(x86_64)
license=(custom)
makedepends=(ghostscript openexr libwmf librsvg libxml2 openjpeg2 libraw opencl-headers libwebp
             chrpath ocl-icd glu ghostpcl ghostxps libheif jbigkit lcms2 libxext liblqr libraqm libpng 'fftw')
checkdepends=(gsfonts ttf-dejavu)
_relname=ImageMagick-${pkgver%%.*}
_tarname=ImageMagick-${pkgver%.*}-${pkgver##*.}
source=(https://imagemagick.org/download/$_tarname.tar.xz{,.asc}
        arch-fonts.diff)
sha256sums=('f22b72bd96c63233f23bfd21a3d9c70252bc9f388613117991e70669324a2305'
            'SKIP'
            'a85b744c61b1b563743ecb7c7adad999d7ed9a8af816650e3ab9321b2b102e73')
validpgpkeys=(D8272EF51DA223E4D05B466989AB63D48277377A)  # Lexie Parsimoniae

shopt -s extglob

prepare() {
  mkdir -p docpkg/usr/share

  cd $_tarname

  # Fix up typemaps to match our packages, where possible
  patch -p1 -i ../arch-fonts.diff
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
    --without-gslib \
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
    --without-gvc
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

check() (
  cd $_tarname
  ulimit -n 4096
  make check
)

package_imagemagick-fftw() {
  depends=(libltdl lcms2 fontconfig libxext liblqr libraqm libpng libxml2)
  optdepends=('ghostscript: PS/PDF support'
              'libheif: HEIF support'
              'libraw: DNG support'
              'librsvg: SVG support'
              'libwebp: WEBP support'
              'libwmf: WMF support'
              'libxml2: Magick Scripting Language'
              'ocl-icd: OpenCL support'
              'openexr: OpenEXR support'
              'openjpeg2: JPEG2000 support'
              'pango: Text rendering'
              'imagemagick-doc: manual and API docs')
  options=(!emptydirs libtool)
  backup=(etc/$_relname/{colors,delegates,log,mime,policy,quantization-table,thresholds,type,type-{dejavu,ghostscript}}.xml)
  conflicts=(imagemagick6 imagemagick)
  provides=(libmagick libmagick-fftw imagemagick=$pkgver)
  replaces=(libmagick-fftw)

  cd $_tarname
  make DESTDIR="$pkgdir" install

  find "$pkgdir/usr/lib/perl5" -name '*.so' -exec chrpath -d {} +
  rm "$pkgdir"/etc/$_relname/type-{apple,urw-base35,windows}.xml
  rm "$pkgdir"/usr/lib/*.la

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 LICENSE NOTICE

# Split docs
  mv "$pkgdir/usr/share/doc" "$srcdir/docpkg/usr/share/"

# Harden security policy https://bugs.archlinux.org/task/62785
  sed -e '/<\/policymap>/i \ \ <policy domain="delegate" rights="none" pattern="gs" \/>' -i "$pkgdir"/etc/ImageMagick-7/policy.xml

# Use correct options for inkscape<1.0
  sed -e 's|--export-file|--export-png|' -i "$pkgdir"/etc/ImageMagick-7/delegates.xml
}

