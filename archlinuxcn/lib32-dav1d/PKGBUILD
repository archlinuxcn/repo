# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>

_pkgbasename=dav1d
pkgname=("lib32-$_pkgbasename" "lib32-lib$_pkgbasename")
pkgver=0.9.2
pkgrel=2
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
      "https://code.videolan.org/videolan/dav1d/-/commit/c6a08b3aa1ee99dade53e5e32033bc1d14455a22.patch"
      )
sha512sums=(
      '87026f8b14e408ff50fc8f137ec2ede4b14c5f69687e615d2359d0f718ae5cb5176522490786d9ae1f7838182f82615c2674f7c2961b6dcec83f1ee587c3af7c'
      'SKIP'
      'SKIP'
      )
b2sums=(
      '7baa28821b06b05b95d3ea80b22dffe59d0793c9b4be4231ba0be99b548e1f5517a956dc865c2be1702576d078c2218e7e80342a26ab4003b4f06bcb0cdbb769'
      'SKIP'
      'SKIP'
      )
validpgpkeys=('65F7C6B4206BD057A7EB73787180713BE58D1ADC') # VideoLAN Release Signing Key

prepare() {
  cd ${_pkgbasename}-${pkgver}

  # Patching if needed
  echo "Patching meson.build"
  patch -p1 < ../c6a08b3aa1ee99dade53e5e32033bc1d14455a22.patch
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
