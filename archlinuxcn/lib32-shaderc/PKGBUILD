# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>

_setPrefix="/usr"
_setLibdir="lib32"
_setFullLibdir="${_setPrefix}/${_setLibdir}"
_pkgbasename=shaderc

pkgname=lib32-$_pkgbasename
pkgver=2022.1
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
        "${_pkgbasename}-${pkgver}.tar.gz::https://github.com/google/shaderc/archive/v${pkgver}.tar.gz"
        )
sha512sums=(
        '21c2462cb434d94da87c71ba660f6cd5b161450d7faeff8789b41db25e64f2baa7c560e78aa856d128c5a73699215d6b1085b5ca19a4640237adf194793ad44b'
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
      -DSHADERC_SKIP_TESTS=ON \
      -Dglslang_SOURCE_DIR=/usr/include/glslang \
      -G Ninja
    ninja -C build

#  cd glslc
#  asciidoctor -b manpage README.asciidoc -o glslc.1
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
