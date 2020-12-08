# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>

# Careful when upgrading this package! It usually breaks ABI without bumping soname.
_setPrefix="/usr"
_setLibdir="lib32"
_setFullLibdir="${_setPrefix}/${_setLibdir}"
_pkgbasename=glslang

pkgname=lib32-$_pkgbasename
pkgver=8.13.3743
pkgrel=1
pkgdesc='OpenGL and OpenGL ES shader front end and validator (32bit)'
arch=('x86_64')
url='https://github.com/KhronosGroup/glslang'
license=('BSD')
depends=(
        "$_pkgbasename"
        'lib32-gcc-libs'
        'lib32-spirv-tools'
        'python'
        )
makedepends=(
        'cmake'
        'ninja'
        )
options=('staticlibs')
source=(
        "${_pkgbasename}-${pkgver}.tar.gz::https://github.com/KhronosGroup/glslang/archive/${pkgver}.tar.gz"
)
sha256sums=(
        '639ebec56f1a7402f2fa094469a5ddea1eceecfaf2e9efe361376a0f73a7ee2f'
)

prepare() {
    echo "Patching if needed"
    cd ${_pkgbasename}-${pkgver}
}

build() {
  export CCFLAGS="-m32"
  export CXXFLAGS="-m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  cd ${_pkgbasename}-${pkgver}
  mkdir -p build-{shared,static}
  (cd build-shared
    cmake .. \
      -G Ninja \
      -DCMAKE_INSTALL_PREFIX="/usr" \
      -DCMAKE_INSTALL_LIBDIR="lib32" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS:STRING=-m32 \
      -DCMAKE_CXX_FLAGS:STRING=-m32 \
      -DBUILD_SHARED_LIBS=ON
    ninja
  )
  (cd build-static
    cmake .. \
      -G Ninja \
      -DCMAKE_INSTALL_PREFIX="/usr" \
      -DCMAKE_INSTALL_LIBDIR="lib32" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS:STRING=-m32 \
      -DCMAKE_CXX_FLAGS:STRING=-m32 \
      -DBUILD_SHARED_LIBS=OFF
    ninja
  )
}

package() {
  cd ${_pkgbasename}-${pkgver}
  DESTDIR="${pkgdir}" ninja -C build-shared install
  DESTDIR="${pkgdir}" ninja -C build-static install

  cd "${pkgdir}/usr/lib32/"
  for lib in *.so; do
    ln -sf "${lib}" "${lib}.0"
  done
  cd ..

  for i in "${pkgdir}/usr/bin/"*; do
    mv "$i" "$i"32
  done

  rm -rf "${pkgdir}"/usr/{include,share}
}

# vim: ts=2 sw=2 et: