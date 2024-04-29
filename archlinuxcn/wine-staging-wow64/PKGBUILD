# Maintainer: Daniele Basso <d dot bass05 at proton dot me>

## useful links:
# https://www.winehq.org
# https://gitlab.winehq.org/wine/wine
# https://gitlab.winehq.org/wine/wine-staging
# https://github.com/wine-staging/wine-staging

pkgname="wine-staging-wow64"
pkgver=9.7
_pkgver="${pkgver/rc/-rc}"
pkgrel=1
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

  # with-wayland
  libxkbcommon
  wayland
)
_spacehogs=(
  samba
  sane
)
makedepends=(
  # staging
  git

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

  "${_spacehogs[@]}"
)
optdepends=(
  alsa-lib              #lib32-alsa-lib
  cups
  dosbox

  "${_spacehogs[@]}"
)

provides=(
  "wine=$pkgver"
  "wine-staging=$pkgver"
  "wine-wow64=$pkgver"
)
conflicts=("wine")

install="wine.install"
backup=("usr/lib/binfmt.d/wine.conf")

options=(staticlibs !lto)

source=(
  "git+https://gitlab.winehq.org/wine/wine.git#tag=wine-$pkgver"
  "30-win32-aliases.conf"
  "wine-binfmt.conf"
  "git+https://gitlab.winehq.org/wine/wine-staging.git#tag=v$pkgver"
)
b2sums=('939c89ddc4f9fb14258a8671b3dcf037e457a8575f32caed23ba006abcc153d3901d5a6522629af447e6c78aac4278663c26b9708eeb2a5a221a8256550f8a4d'
        '45db34fb35a679dc191b4119603eba37b8008326bd4f7d6bd422fbbb2a74b675bdbc9f0cc6995ed0c564cf088b7ecd9fbe2d06d42ff8a4464828f3c4f188075b'
        'e9de76a32493c601ab32bde28a2c8f8aded12978057159dd9bf35eefbf82f2389a4d5e30170218956101331cf3e7452ae82ad0db6aad623651b0cc2174a61588'
        '17ebd779c6010ca223849960c972e33d06c0ad38a1e9f903de20c7ffb3c76b8ab7a2bdaf4ae3fc37356196e9c9f5e2bd5ac6f301922bfaea95a59eb93f0605a5')

prepare() {
  # apply wine-staging patchset
  cd "wine"
  "../wine-staging/staging/patchinstall.py" --all
}

build() {
  cd "wine"
  ./configure \
    --disable-tests \
    --prefix=/usr \
    --libdir=/usr/lib \
    --with-wayland \
    --enable-archs=x86_64,i386
  make
}

package() {
  cd "wine"
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
