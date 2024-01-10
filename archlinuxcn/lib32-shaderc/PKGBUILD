# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>

_setPrefix="/usr"
_setLibdir="lib32"
_setFullLibdir="${_setPrefix}/${_setLibdir}"
_pkgbasename=shaderc

pkgname=lib32-$_pkgbasename
pkgver=2023.7
pkgrel=2
pkgdesc='Collection of tools, libraries and tests for shader compilation (32bit)'
url='https://github.com/google/shaderc'
arch=('x86_64')
license=('Apache')
depends=(
        "$_pkgbasename>=$pkgver"
        'lib32-glibc'
        'lib32-gcc-libs'
        'lib32-glslang'
        'lib32-spirv-tools'
        )
makedepends=(
        'cmake'
        'ninja'
        'python'
        'spirv-headers'
        )
provides=('libshaderc_shared.so')
conflicts=('lib32-shaderc-git')
source=(
        "${_pkgbasename}-${pkgver}.tar.gz::https://github.com/google/shaderc/archive/v${pkgver}/${_pkgbasename}-${pkgver}.tar.gz"
        )
sha512sums=(
        'f3c1db574312e7e5ee22fb64f47f6609369754dd1648eb4e51c30b3c40aafd9994e54560e8334d01ac7d00011285a94d0543fa9ecd6977ec34c39a965fd72269'
        )
b2sums=(
        'de5ee8cc35bc76ba1301e80217587cbf55885999297755d78a72fe0940431351d4070cdd0793fe8f43208d40c9ec343bbe888da2b8ded471bd241be067b1addf'
        )

prepare() {
  cd ${_pkgbasename}-${pkgver}

  # de-vendor libs and disable git versioning
  sed '/examples/d;/third_party/d' -i CMakeLists.txt
  sed '/build-version/d' -i glslc/CMakeLists.txt
  cat <<- EOF > glslc/src/build-version.inc
"${pkgver}\\n"
"$(pacman -Q spirv-tools|cut -d \  -f 2|sed 's/-.*//')\\n"
"$(pacman -Q glslang|cut -d \  -f 2|sed 's/-.*//')\\n"
EOF
}

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
#  export CFLAGS+=" ${CPPFLAGS}"
#  export CXXFLAGS+=" ${CPPFLAGS} -I/usr/include/glslang"

  cd ${_pkgbasename}-${pkgver}
  cmake \
      -B build \
      -GNinja \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX="/usr" \
      -DCMAKE_INSTALL_LIBDIR="lib32" \
      -DCMAKE_CXX_FLAGS="$CXXFLAGS -ffat-lto-objects" \
      -DSHADERC_SKIP_TESTS=ON \
      -Dglslang_SOURCE_DIR=/usr/include/glslang
    ninja -C build

#  cd glslc
#  asciidoctor -b manpage README.asciidoc -o glslc.1
}

check() {
  cd ${_pkgbasename}-${pkgver}
  ninja -C build test
}

package() {
  cd ${_pkgbasename}-${pkgver}
  DESTDIR="${pkgdir}" ninja -C build install

  # Use the same naming scheme as the one in the lib32-shaderc-git package for coherence
  for i in "${pkgdir}/usr/bin/"*; do
    mv "$i" "$i"-32
  done

  rm -r "${pkgdir}"/usr/include
#  install -Dm 644 glslc/glslc.1 -t "${pkgdir}/usr/share/man/man1"

  # Remove unused shaderc_static.pc
  rm "${pkgdir}/usr/lib32/pkgconfig/shaderc_static.pc"

}
