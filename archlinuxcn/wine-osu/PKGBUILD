# Maintainer: Hugo "ThePooN" Denizart <thepoon@cartooncraft.fr>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Eduardo Romero <eduardo@archlinux.org>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>

pkgname=wine-osu
pkgver=3.12
pkgrel=2

_pkgbasever=${pkgver/rc/-rc}

source=(https://dl.winehq.org/wine/source/3.x/wine-$_pkgbasever.tar.xz{,.sign}
        "wine-staging-v$_pkgbasever.tar.gz::https://github.com/wine-staging/wine-staging/archive/v$_pkgbasever.tar.gz"
        harmony-fix.diff
        winealsa_latency.patch
        winepulse_latency.patch)
sha512sums=('afc76e8975ea780f664de27a17128f730bcbe72a9fad0c01bfe6dcc98c2f98729ccde32e97fe4df2cf98f5d1b254b28f0e7cd380855148c5cfb41dd88f3012a1'
            'SKIP'
            '166f991f7c8f59df656f3fb28150a8e26e48d1ff6906b3eccd31cb84524e28efe7e7df00eadc21881940308ccc4b4edebcb2a71bdd03ba3de5beb1cf42e2f058'
            'b86edf07bfc560f403fdfd5a71f97930ee2a4c3f76c92cc1a0dbb2e107be9db3bed3a727a0430d8a049583c63dd11f5d4567fb7aa69b193997c6da241acc4f2e'
            '8212f4ec07045faa28704035ea6c8173ade503afe3bf94c4ec19e9edb788004579bb37e16c58d92ddc23e9a4de52480437f8486a32d794c5edc59d448db46874'
            '3c5eda2d24892ca6428138bd9f07d5c598b606f9e181533d73556b25aabe41935efb44748cdb65524d7598ceac1bc81d9c9d507b76a15c51f32e34b3cdc3969a')
validpgpkeys=(5AC1A08B03BD7A313E0A955AF5E6E9EEB9461DD7
              DA23579A74D4AD9AF9D3F945CEFAC8EAAF17519D)

pkgdesc="A compatibility layer for running Windows programs - Staging branch, optimized for audio low latency on osu! (by ThePooN)"
url="https://blog.thepoon.fr/osuLinuxAudioLatency/"
arch=(x86_64)
options=(staticlibs)
license=(LGPL)

depends=(
  attr             lib32-attr
  fontconfig       lib32-fontconfig
  lcms2            lib32-lcms2
  libxml2          lib32-libxml2
  libxcursor       lib32-libxcursor
  libxrandr        lib32-libxrandr
  libxdamage       lib32-libxdamage
  libxi            lib32-libxi
  gettext          lib32-gettext
  freetype2        lib32-freetype2
  glu              lib32-glu
  libsm            lib32-libsm
  gcc-libs         lib32-gcc-libs
  gnutls           lib32-gnutls
  libpulse         lib32-libpulse
  desktop-file-utils
)

makedepends=(autoconf ncurses bison perl fontforge flex
  'gcc>=4.5.0-2'
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
  alsa-lib              lib32-alsa-lib
  libxcomposite         lib32-libxcomposite
  mesa                  lib32-mesa
  mesa-libgl            lib32-mesa-libgl
  opencl-icd-loader     lib32-opencl-icd-loader
  libxslt               lib32-libxslt
  libpulse              lib32-libpulse
  libva                 lib32-libva
  gtk3                  lib32-gtk3
  gst-plugins-base-libs lib32-gst-plugins-base-libs
  vulkan-icd-loader     lib32-vulkan-icd-loader
  sdl2                  lib32-sdl2
  samba
  opencl-headers
)

optdepends=(
  giflib                lib32-giflib
  libpng                lib32-libpng
  libldap               lib32-libldap
  mpg123                lib32-mpg123
  openal                lib32-openal
  v4l-utils             lib32-v4l-utils
  alsa-plugins          lib32-alsa-plugins
  alsa-lib              lib32-alsa-lib
  libjpeg-turbo         lib32-libjpeg-turbo
  libxcomposite         lib32-libxcomposite
  libxinerama           lib32-libxinerama
  ncurses               lib32-ncurses
  opencl-icd-loader     lib32-opencl-icd-loader
  libxslt               lib32-libxslt
  libva                 lib32-libva
  gtk3                  lib32-gtk3
  gst-plugins-base-libs lib32-gst-plugins-base-libs
  vulkan-icd-loader     lib32-vulkan-icd-loader
  sdl2                  lib32-sdl2
  cups
  samba           dosbox
)

prepare() {
  # Allow ccache to work
  mv wine-$_pkgbasever $pkgname

  # apply wine-staging patchset
  pushd wine-staging-$_pkgbasever/patches
  ./patchinstall.sh DESTDIR="$srcdir/$pkgname" --all
  popd
  
  # https://bugs.winehq.org/show_bug.cgi?id=43530
  export CFLAGS="${CFLAGS/-fno-plt/}"
  export LDFLAGS="${LDFLAGS/,-z,now/}"

  patch -d $pkgname -Np1 < harmony-fix.diff

  patch -d $pkgname -Np1 < winealsa_latency.patch
  patch -d $pkgname -Np1 < winepulse_latency.patch

  sed 's|OpenCL/opencl.h|CL/opencl.h|g' -i $pkgname/configure*

  # Get rid of old build dirs
  rm -rf $pkgname-{32,64}-build
  mkdir $pkgname-{32,64}-build
}

build() {
  cd "$srcdir"

  msg2 "Building Wine-64..."

  cd "$srcdir/$pkgname-64-build"
  ../$pkgname/configure \
    --prefix=/opt/wine-osu \
    --libdir=/opt/wine-osu/lib \
    --with-x \
    --with-gstreamer \
    --without-pcap \
    --enable-win64 \
    --with-xattr

  make

  msg2 "Building Wine-32..."

  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  cd "$srcdir/$pkgname-32-build"
  ../$pkgname/configure \
    --prefix=/opt/wine-osu \
    --with-x \
    --with-gstreamer \
    --with-xattr \
    --without-pcap \
    --libdir=/opt/wine-osu/lib32 \
    --with-wine64="$srcdir/$pkgname-64-build"

  make
}

package() {
  msg2 "Packaging Wine-32..."
  cd "$srcdir/$pkgname-32-build"

  make prefix="$pkgdir/opt/wine-osu" \
    libdir="$pkgdir/opt/wine-osu/lib32" \
    dlldir="$pkgdir/opt/wine-osu/lib32/wine" install

  msg2 "Packaging Wine-64..."
  cd "$srcdir/$pkgname-64-build"
  make prefix="$pkgdir/opt/wine-osu" \
    libdir="$pkgdir/opt/wine-osu/lib" \
    dlldir="$pkgdir/opt/wine-osu/lib/wine" install
}

# vim:set ts=8 sts=2 sw=2 et:
