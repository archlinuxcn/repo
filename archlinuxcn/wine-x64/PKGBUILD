# Maintainer: Roland <hr_01y@protonmail.com>

pkgname=wine-x64
pkgver=5.17
pkgrel=1
pkgdesc="A compatibility layer for running Windows programs. This only configured with x64 support."
url="http://www.winehq.com"
arch=(x86_64)
options=(staticlibs)
license=(LGPL)


# replacing rc with -rc
# pkgver is not allowed to contain hyphens
_pkgbasever=${pkgver/rc/-rc}

source=(https://dl.winehq.org/wine/source/5.x/wine-$_pkgbasever.tar.xz{,.sign}
        30-win32-aliases.conf)
sha512sums=('05338036fa9b195d9cf8a84a1bcc03f35422d5f07744ec4430f20874601829be5904be10060353599cb0187728123f959ccc75e79f1ce1c47178ae9cd55ef696'
            '118c5ffefc986bec85c94c674317f81c609e325b791a8638652191a8a3011585d8de1d98029c0ed11a1f8abc83d1762546656c02188a3844d4fc929b663d765e'
            '6e54ece7ec7022b3c9d94ad64bdf1017338da16c618966e8baf398e6f18f80f7b0576edf1d1da47ed77b96d577e4cbb2bb0156b0b11c183a0accf22654b0a2bb')
validpgpkeys=(DA23579A74D4AD9AF9D3F945CEFAC8EAAF17519D)


depends=(
  libx11
  fontconfig
  lcms2
  sdl2
  libxcursor
  libjpeg
  libxslt
  libxrandr
  libxi
  freetype2
  libxinerama
  libxcomposite
  glu
)

makedepends=(
  bison
)

optdepends=(
  v4l-utils
  opencl-headers
  opencl-icd-loader
  libpulse
  gsm
  libgphoto2
  sane
  libcups
  openal
  faudio
  mpg123
  vkd3d
  vulkan-icd-loader
  vulkan-headers
)

prepare() {

  # https://bugs.winehq.org/show_bug.cgi?id=43530
  export CFLAGS="${CFLAGS/-fno-plt/}"
  export LDFLAGS="${LDFLAGS/,-z,now/}"

  sed 's|OpenCL/opencl.h|CL/opencl.h|g' -i wine-$_pkgbasever/configure*

  # Get rid of old build dirs
  rm -rf wine-64-build
}

build() {
  msg2 "building wine-$_pkgbasever ..."

  cd wine-$_pkgbasever

  ./configure \
    --prefix=/usr \
    --libdir=/usr/lib \
    --with-x \
    --without-gstreamer \
    --without-hal \
    --without-oss \
    --without-mingw \
    --enable-win64

  make
}

package() {
  msg2 "packaging wine-$_pkgbasever ..."

  cd wine-$_pkgbasever

  make prefix="$pkgdir/usr" \
    libdir="$pkgdir/usr/lib" \
    dlldir="$pkgdir/usr/lib/wine" install

  # font aliasing settings
  install -d "$pkgdir"/etc/fonts/conf.{avail,d}
  install -m644 "$srcdir/30-win32-aliases.conf" "$pkgdir/etc/fonts/conf.avail"
  ln -s ../conf.avail/30-win32-aliases.conf "$pkgdir/etc/fonts/conf.d/30-win32-aliases.conf"
}

