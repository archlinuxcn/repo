# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>

_pkgbasename=dav1d
pkgname=("lib32-$_pkgbasename" "lib32-lib$_pkgbasename")
pkgver=0.9.0
pkgrel=1
pkgdesc='AV1 cross-platform decoder focused on speed and correctness (32 bit)'
url='https://code.videolan.org/videolan/dav1d/'
arch=('x86_64')
license=('BSD')
makedepends=(
      'meson'
#      'meson-cross-x86-linux-gnu'
      'ninja'
      'nasm'
      'doxygen'
      'graphviz'
      'xxhash'
      )
source=(
      https://downloads.videolan.org/pub/videolan/${_pkgbasename}/${pkgver}/${_pkgbasename}-${pkgver}.tar.xz{,.asc}
      )
sha512sums=(
      '46ead83042ab951eb4c79c458e060875174739a8a0efd8d34fdcb6ad3c094093f629d16f467c1dbd37a125bba31d0a7b051933540e38c675eade25fefc80ed75'
      'SKIP'
      )
b2sums=(
      '261331fb339c4f5e1f854310dd5ee5f0d9d7730385c5eaa5c097a26daa2d92b4283ade127dffbec776da2737f1269797cfdda516d3531e8ac1c0947c431e6e68'
      'SKIP'
      )
validpgpkeys=('65F7C6B4206BD057A7EB73787180713BE58D1ADC') # VideoLAN Release Signing Key

prepare() {
  cd ${_pkgbasename}-${pkgver}

  # Patching if needed
}

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  export CFLAGS+=" ${CPPFLAGS}"
  export CXXFLAGS+=" ${CPPFLAGS} -I/usr/include/glslang"

  cd ${_pkgbasename}-${pkgver}
  arch-meson build \
    --prefix=/usr \
    --libdir=lib32 \
    -D enable_tests=false

# Options disabled
#     --cross-file x86-linux-gnu \ ## Meson doesn't use the system's LDFLAGS with cross-file yet...

  ninja -C build
}

check() {
  cd ${_pkgbasename}-${pkgver}/build
#  meson test
}

package_lib32-libdav1d(){
  pkgdesc='AV1 cross-platform decoder focused on speed and correctness - library (32 bit)'
  depends=(
    "${_pkgbasename}=${pkgver}"
    'lib32-glibc'
  )
  provides=('lib32-dav1d' 'libdav1d.so')

 cd ${_pkgbasename}-${pkgver}

  DESTDIR="${pkgdir}" ninja -C build install

  rm -r "$pkgdir"/usr/{include,bin}

  mkdir -p "${pkgdir}/usr/share/doc/${pkgname}/"
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}/"
  ln -s "/usr/share/doc/${_pkgbasename}/"README.md "${pkgdir}/usr/share/doc/${pkgname}/"
  ln -s "/usr/share/doc/${_pkgbasename}/"CONTRIBUTING.md "${pkgdir}/usr/share/doc/${pkgname}/"
  ln -s "/usr/share/doc/${_pkgbasename}/"NEWS "${pkgdir}/usr/share/doc/${pkgname}/"
  ln -s "/usr/share/licenses/${_pkgbasename}/"COPYING "${pkgdir}/usr/share/licenses/${pkgname}/"
}

package_lib32-dav1d() {
  pkgdesc='AV1 cross-platform decoder focused on speed and correctness (32 bit)'
  depends=(
    'lib32-glibc' 
    'lib32-libdav1d'
  )

  cd ${_pkgbasename}-${pkgver}

  DESTDIR="${pkgdir}" ninja -C build install

  # Keep files in bin since this is not a library only package. 
  # Use the same naming scheme as proposed in Arch's wiki:  https://wiki.archlinux.org/index.php/32-bit_package_guidelines
  # which is "--program-suffix="-32" with Autoconf
  for i in "${pkgdir}/usr/bin/"*; do
    mv "$i" "$i"-32
  done

  rm -r "$pkgdir"/usr/{include,lib32}

  mkdir -p "${pkgdir}/usr/share/doc/${pkgname}/"
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}/"
  ln -s "/usr/share/doc/${_pkgbasename}/"README.md "${pkgdir}/usr/share/doc/${pkgname}/"
  ln -s "/usr/share/licenses/${_pkgbasename}/"COPYING "${pkgdir}/usr/share/licenses/${pkgname}/"
}
