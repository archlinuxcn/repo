# Maintainer: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Eduardo Romero <eduardo@archlinux.org>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>

pkgname=wine
pkgver=7.0rc1
pkgrel=1

_pkgbasever=${pkgver/rc/-rc}

source=(https://dl.winehq.org/wine/source/7.0/$pkgname-$_pkgbasever.tar.xz{,.sign}
        30-win32-aliases.conf
        wine-binfmt.conf)
sha512sums=('700359a8353597ce10284152cb318011aef1111cb9bc98e4794cfa6f630d6a03a8ae5556b6f6aaec8b4cd64bc4f21587f5ce2b7cc9635abeacda426dabf268bb'
            'SKIP'
            '6e54ece7ec7022b3c9d94ad64bdf1017338da16c618966e8baf398e6f18f80f7b0576edf1d1da47ed77b96d577e4cbb2bb0156b0b11c183a0accf22654b0a2bb'
            'bdde7ae015d8a98ba55e84b86dc05aca1d4f8de85be7e4bd6187054bfe4ac83b5a20538945b63fb073caab78022141e9545685e4e3698c97ff173cf30859e285')
validpgpkeys=(5AC1A08B03BD7A313E0A955AF5E6E9EEB9461DD7
              DA23579A74D4AD9AF9D3F945CEFAC8EAAF17519D)

pkgdesc="A compatibility layer for running Windows programs"
url="http://www.winehq.com"
arch=(x86_64)
options=(staticlibs)
license=(LGPL)
depends=(
  fontconfig      lib32-fontconfig
  lcms2           lib32-lcms2
  libxml2         lib32-libxml2
  libxcursor      lib32-libxcursor
  libxrandr       lib32-libxrandr
  libxdamage      lib32-libxdamage
  libxi           lib32-libxi
  gettext         lib32-gettext
  freetype2       lib32-freetype2
  glu             lib32-glu
  libsm           lib32-libsm
  gcc-libs        lib32-gcc-libs
  libpcap         lib32-libpcap
  faudio          lib32-faudio
  desktop-file-utils
)
makedepends=(autoconf bison perl fontforge flex mingw-w64-gcc
  giflib                lib32-giflib
  libpng                lib32-libpng
  gnutls                lib32-gnutls
  libxinerama           lib32-libxinerama
  libxcomposite         lib32-libxcomposite
  libxmu                lib32-libxmu
  libxxf86vm            lib32-libxxf86vm
  libldap               lib32-libldap
  mpg123                lib32-mpg123
  openal                lib32-openal
  v4l-utils             lib32-v4l-utils
  libpulse              lib32-libpulse
  alsa-lib              lib32-alsa-lib
  libxcomposite         lib32-libxcomposite
  mesa                  lib32-mesa
  mesa-libgl            lib32-mesa-libgl
  opencl-icd-loader     lib32-opencl-icd-loader
  libxslt               lib32-libxslt
  gst-plugins-base-libs lib32-gst-plugins-base-libs
  vulkan-icd-loader     lib32-vulkan-icd-loader
  vkd3d                 lib32-vkd3d
  sdl2                  lib32-sdl2
  libcups               lib32-libcups
  libgphoto2
  sane
  gsm
  vulkan-headers
  samba
  opencl-headers
)
optdepends=(
  giflib                lib32-giflib
  libpng                lib32-libpng
  libldap               lib32-libldap
  gnutls                lib32-gnutls
  mpg123                lib32-mpg123
  openal                lib32-openal
  v4l-utils             lib32-v4l-utils
  libpulse              lib32-libpulse
  alsa-plugins          lib32-alsa-plugins
  alsa-lib              lib32-alsa-lib
  libjpeg-turbo         lib32-libjpeg-turbo
  libxcomposite         lib32-libxcomposite
  libxinerama           lib32-libxinerama
  opencl-icd-loader     lib32-opencl-icd-loader
  libxslt               lib32-libxslt
  gst-plugins-base-libs lib32-gst-plugins-base-libs
  vkd3d                 lib32-vkd3d
  sdl2                  lib32-sdl2
  libgphoto2
  sane
  gsm
  cups
  samba           dosbox
)
makedepends=(${makedepends[@]} ${depends[@]})
install=wine.install

prepare() {
  # Allow ccache to work
  mv wine-$_pkgbasever $pkgname

  scard4wine_dir=scard4wine-yan12125/src
  cp -v $scard4wine_dir/winscard.c $pkgname/dlls/winscard/winscard.c
  cp -v $scard4wine_dir/winscard.spec $pkgname/dlls/winscard/winscard.spec
  cp -v $scard4wine_dir/winscard.h $pkgname/include/winscard.h
  cp -v $scard4wine_dir/winsmcrd.h $pkgname/include/winsmcrd.h
  cp -v $scard4wine_dir/wine-compat56.h $pkgname/include/wine-compat.h

  echo EXTRADLLFLAGS = -mcygwin >> $pkgname/dlls/winscard/Makefile.in

  # Doesn't compile without remove these flags as of 4.10
  export CFLAGS="${CFLAGS/-fno-plt/}"
  export LDFLAGS="${LDFLAGS/,-z,now/}"

  sed 's|OpenCL/opencl.h|CL/opencl.h|g' -i $pkgname/configure*

  # Fix openldap 2.5+ detection
  sed 's/-lldap_r/-lldap/' -i $pkgname/configure

  # Get rid of old build dirs
  rm -rf $pkgname-{32,64}-build
  mkdir $pkgname-32-build
}

build() {
  cd "$srcdir"

  msg2 "Building Wine-64..."

  mkdir $pkgname-64-build
  cd "$srcdir/$pkgname-64-build"
  ../$pkgname/configure \
    --prefix=/usr \
    --libdir=/usr/lib \
    --with-x \
    --with-gstreamer \
    --enable-win64
  # Gstreamer was disabled for FS#33655

  make

  _wine32opts=(
    --libdir=/usr/lib32
    --with-wine64="$srcdir/$pkgname-64-build"
  )

  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  msg2 "Building Wine-32..."
  cd "$srcdir/$pkgname-32-build"
  ../$pkgname/configure \
    --prefix=/usr \
    --with-x \
    --with-gstreamer \
    "${_wine32opts[@]}"

  make
}

package() {
  msg2 "Packaging Wine-32..."
  cd "$srcdir/$pkgname-32-build"

  make prefix="$pkgdir/usr" \
    libdir="$pkgdir/usr/lib32" \
    dlldir="$pkgdir/usr/lib32/wine" install

  msg2 "Packaging Wine-64..."
  cd "$srcdir/$pkgname-64-build"
  make prefix="$pkgdir/usr" \
    libdir="$pkgdir/usr/lib" \
    dlldir="$pkgdir/usr/lib/wine" install

  # Font aliasing settings for Win32 applications
  install -d "$pkgdir"/usr/share/fontconfig/conf.{avail,default}
  install -m644 "$srcdir/30-win32-aliases.conf" "$pkgdir/usr/share/fontconfig/conf.avail"
  ln -s ../conf.avail/30-win32-aliases.conf "$pkgdir/usr/share/fontconfig/conf.default/30-win32-aliases.conf"
  install -Dm 644 "$srcdir/wine-binfmt.conf" "$pkgdir/usr/lib/binfmt.d/wine.conf"

  i686-w64-mingw32-strip --strip-unneeded "$pkgdir"/usr/lib32/wine/i386-windows/*.dll
  x86_64-w64-mingw32-strip --strip-unneeded "$pkgdir"/usr/lib/wine/x86_64-windows/*.dll
}

# vim:set ts=8 sts=2 sw=2 et:

source+=("scard4wine-yan12125::git+https://git.code.sf.net/u/yan12125/scard4wine.git#commit=7621961210a55b4333f3039bae2355430f9bd8cd")
sha512sums+=('SKIP')
makedepends+=(git)
provides=("$pkgname=$pkgver")
conflicts=("$pkgname")
pkgname+='-winscard'
pkgdesc+=" (with IDRASSI's winscard patch)"
