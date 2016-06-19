# Installation order:  freetype2-ubuntu fontconfig-ubuntu libxft cairo-ubuntu
pkgname=freetype2-ubuntu
pkgver=2.6.3
_ubver=2.6.3-3ubuntu1
_ubrel=utopic
pkgrel=3
pkgdesc="TrueType font rendering library, with Ubuntu's LCD rendering patches"
arch=('i686' 'x86_64')
url="https://launchpad.net/ubuntu/+source/freetype"
license=('GPL')
depends=('zlib' 'bzip2' 'sh')
conflicts=('freetype2' 'freetype2-cleartype' 'freetype2-lcd')
provides=("freetype2=$pkgver" "libfreetype.so")
options=('!libtool')
source=(http://downloads.sourceforge.net/sourceforge/freetype/freetype-${pkgver}.tar.bz2
		https://launchpad.net/ubuntu/+archive/primary/+files/freetype_${_ubver}.diff.gz
        freetype-2.2.1-enable-valid.patch
        freetype-2.3.0-enable-spr.patch
        freetype-2.4.11-enable-sph.patch)

prepare() {
  cd "${srcdir}/freetype-${pkgver}"

  # Patch from ubuntu
  patch -Np1 -i $srcdir/freetype_$_ubver.diff


  sed -e "s/-p[0-9]\|.*otvalid\.patch//g" \
      -i debian/patches-freetype/series

  sed -e 's/ src/ a\/src/g' \
      -e '/^Index.*ftbase.c/,/EOF/d' \
      -i debian/patches-freetype/freetype-2.1.7-backwards.compat.patch

  for _f in $(cat debian/patches-freetype/series) ; do    
    patch -Np1 -i debian/patches-freetype/$_f    
  done

  # Patches from arch trunkcat debian/patches-freetype/series
  patch -Np1 -i "${srcdir}/freetype-2.2.1-enable-valid.patch"
#  patch -Np1 -i "${srcdir}/freetype-2.3.0-enable-spr.patch"
  # Disabled for now due to resistance
  # Kept here for easier rebuilds via ABS
  # https://bugs.archlinux.org/task/35274
  #patch -Np1 -i "${srcdir}/freetype-2.4.11-enable-sph.patch"
}


build() {
  cd ${srcdir}/freetype-${pkgver}

  # PNG support is useless if FT_CONFIG_OPTION_USE_PNG is disabled
  ./configure --prefix=/usr --disable-static \
    --without-png

  make
}

check() {
  cd "${srcdir}/freetype-${pkgver}"
  make -k check
}

package() {
  cd ${srcdir}/freetype-${pkgver}
  make DESTDIR=${pkgdir} install
}
md5sums=('0037b25a8c090bc8a1218e867b32beb1'
         '161e88978b77ee9be913b98f33fb9a23'
         '214119610444c9b02766ccee5e220680'
         '38765b5cc604179bf3afe33671d8ae37'
         '4d4a0caad7aa5e09bea0719cd80681bf')
