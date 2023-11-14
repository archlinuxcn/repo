# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>

_setPrefix="/usr"
_setLibdir="lib32"
_setFullLibdir="${_setPrefix}/${_setLibdir}"
_pkgbasename=shaderc

pkgname=lib32-$_pkgbasename
pkgver=2023.4
pkgrel=1
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
        '18b7c31eec9408fc038211d4424d5d82414f427a580ec6f412e9e8d6a7e060e4c39d2c223bfbbf4bd167a1575a7bb900591ff834b3356f4024772e0b96993e91'
        )
b2sums=(
        'b033f9d5e8afdf53afb5c3299a2b0496558b25d4fb1b04eab0ab1610377c391084fcb952bf2836bf88078e902e78bd579d46ae8f07aaed42569edbbc21b0d5c9'
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
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX="/usr" \
      -DCMAKE_INSTALL_LIBDIR="lib32" \
      -DCMAKE_CXX_FLAGS="$CXXFLAGS -ffat-lto-objects" \
      -DSHADERC_SKIP_TESTS=ON \
      -Dglslang_SOURCE_DIR=/usr/include/glslang \
      -G Ninja
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
}
