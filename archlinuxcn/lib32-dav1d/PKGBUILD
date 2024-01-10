# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>

_pkgbasename=dav1d
pkgname=("lib32-$_pkgbasename" "lib32-lib$_pkgbasename")
pkgver=1.3.0
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
      "https://code.videolan.org/videolan/dav1d-test-data/-/archive/${pkgver}/dav1d-test-data-${pkgver}.tar.gz"
      )
sha512sums=(
      'a91d217b8656c452dd80f5597e988f0e7a2ea32b12092c2695e7dc388033db7b193f7a8c98413bec31d1c38af376561d39f7618b935c4feeb6498c5d2b43f6a4'
      'SKIP'
      'ec066c690bb1db307cf2a002ddc0a1f0fa77fa8dafbb07fe74da3fbaf6d43b536e673c309f7665d197ef0ad606968040acdcb8252fdf286e749f6ac2de94ac24'
      )
b2sums=(
      'aa79eaa22adde287a31ed60b88ae8d4095e18b92359a7e30aecd13c10eafe07acdeeb2f0bdb232acc6b136cdbd87626ac641df0615683d50f355edfd6c028caf'
      'SKIP'
      '748edf8edbca716ea6742ef6d79b34bf6947b5cbdde213c4cefce43e6b5d9954ca302b880f07d70337b1a6e9a31fba98f588616c8f9a8dd4187518f08bf285e8'
      )
validpgpkeys=('65F7C6B4206BD057A7EB73787180713BE58D1ADC') # VideoLAN Release Signing Key

prepare() {
  cd ${_pkgbasename}-${pkgver}
  ln -s "${srcdir}/dav1d-test-data-${pkgver}" tests/dav1d-test-data

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
    -D enable_tests=false \
    -D enable_docs=false

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
    "${_pkgbasename}>=${pkgver}"
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
