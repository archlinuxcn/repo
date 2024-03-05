# Maintainer: Daniele Basso <d dot bass05 at proton dot me>

## useful links:
# https://www.winehq.org
# https://gitlab.winehq.org/wine/wine
# https://gitlab.winehq.org/wine/wine-staging
# https://github.com/wine-staging/wine-staging

pkgname="wine-wow64"
pkgver=9.3
_pkgver="${pkgver/rc/-rc}"
pkgrel=2
pkgdesc="A compatibility layer for running Windows programs"
url="https://www.winehq.org"
license=(LGPL)
arch=(x86_64)

depends=(
  alsa-plugins          #lib32-alsa-plugins
  fontconfig            #lib32-fontconfig
  freetype2             #lib32-freetype2
  gettext               #lib32-gettext
  gst-plugins-base-libs #lib32-gst-plugins-base-libs
  libpulse              #lib32-libpulse
  libxcomposite         #lib32-libxcomposite
  libxcursor            #lib32-libxcursor
  libxi                 #lib32-libxi
  libxinerama           #lib32-libxinerama
  libxrandr             #lib32-libxrandr
  opencl-icd-loader     #lib32-opencl-icd-loader
  pcsclite              #lib32-pcsclite
  sdl2                  #lib32-sdl2
  v4l-utils             #lib32-v4l-utils
  desktop-file-utils
  libgphoto2
  samba
  sane

  # with-wayland
  libxkbcommon
  wayland
)
makedepends=(
  libcups               #lib32-libcups
  libxxf86vm            #lib32-libxxf86vm
  mesa                  #lib32-mesa
  mesa-libgl            #lib32-mesa-libgl
  vulkan-icd-loader     #lib32-vulkan-icd-loader
  autoconf
  bison
  flex
  mingw-w64-gcc
  opencl-headers
  perl
  vulkan-headers
)
optdepends=(
  alsa-lib              #lib32-alsa-lib
  cups
  dosbox
)

provides=("wine=$pkgver")
conflicts=("wine")

install="wine.install"
backup=("usr/lib/binfmt.d/wine.conf")

options=(staticlibs !lto)

source=(
  "https://dl.winehq.org/wine/source/${pkgver::1}.x/wine-$_pkgver.tar.xz"
  "30-win32-aliases.conf"
  "wine-binfmt.conf"
)
b2sums=('fa6f0c73f0886918b035557a37c0553feeea5692ae15e8d67fc4360c59c1bbab9f7f93e58ae29a41800da50b961b49957cf2d060d6b5da34bd956bf7cb3e5fab'
        '45db34fb35a679dc191b4119603eba37b8008326bd4f7d6bd422fbbb2a74b675bdbc9f0cc6995ed0c564cf088b7ecd9fbe2d06d42ff8a4464828f3c4f188075b'
        'e9de76a32493c601ab32bde28a2c8f8aded12978057159dd9bf35eefbf82f2389a4d5e30170218956101331cf3e7452ae82ad0db6aad623651b0cc2174a61588')

build() {
  cd "wine-$_pkgver"
  ./configure \
    --disable-tests \
    --prefix=/usr \
    --libdir=/usr/lib \
    --with-wayland \
    --enable-archs=x86_64,i386
  make
}

package() {
  cd "wine-$_pkgver"
  make prefix="$pkgdir"/usr \
    libdir="$pkgdir"/usr/lib \
    dlldir="$pkgdir"/usr/lib/wine install

  ln -sf /usr/bin/wine "$pkgdir"/usr/bin/wine64

  # Font aliasing settings for Win32 applications
  install -Dm644 "$srcdir"/30-win32-aliases.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -s ../conf.avail/30-win32-aliases.conf "$pkgdir"/usr/share/fontconfig/conf.default/30-win32-aliases.conf

  install -Dm644 "$srcdir"/wine-binfmt.conf "$pkgdir"/usr/lib/binfmt.d/wine.conf
}

# vim:set ts=8 sts=2 sw=2 et:
