# Maintainer: Daniel M. Capella <polycitizen@gmail.com>
# Contributor: Bin Jin <bjin@ctrl-d.org>

pkgname=shaderc
pkgver=2018.0
pkgrel=1
pkgdesc='A collection of tools, libraries and tests for shader compilation'
arch=('x86_64')
url=https://github.com/google/shaderc
license=('Apache')
depends=('gcc-libs' 'glslang' 'spirv-tools')
makedepends=('asciidoctor' 'cmake' 'ninja' 'python2')
source=("shaderc-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        'fix-glslang-link-order.patch::https://github.com/google/shaderc/pull/463/commits/21c8be385b3fab5edcb934a6d99f69fd389c4e67.patch'
        'https://raw.githubusercontent.com/gentoo/gentoo/0b2433a05d9de287c93b7eab508643ffad676671/media-libs/shaderc/files/shaderc-2018.0-restore-NV_EXTENSIONS-guard.patch')
sha512sums=('7a420fde73c9f2aae3f13558d538a1f4ae43bba19e2b4d2da8fbbd017e9e4f328ece5f330f1bbcb9fe84c91b7eb84b9158dc2e3d144c82939090a0fa6f5b4ef0'
            '94e1fa8d8b5a886efb90b4956a266799af78c6d54ab8cc8f8a89533885e8148ea415dda7faff732fc5ce01015bfa0de9e5ebd35bc503c677769b423a2491f101'
            '08c31a071d5ba385f3d612ff12950512917ce704fa0266820633906f2620c0ecb3d0e8f1d423117386745d155a065e42398bda8f02bec8035df5a222f305a94e')

# https://github.com/gentoo/gentoo/blob/c31d001aeedaf97917fa29fa859e16090cc50282/media-libs/shaderc/shaderc-2017.2.ebuild#L35-L65
prepare() {
  cd shaderc-$pkgver
  patch -Np1 -i ../fix-glslang-link-order.patch
  patch -Np1 -i ../shaderc-2018.0-restore-NV_EXTENSIONS-guard.patch
  sed -i /examples/d\;/third_party/d CMakeLists.txt
  sed -i /build-version/d glslc/CMakeLists.txt
  cat <<- EOF > glslc/src/build-version.inc
"$pkgver\n"
"$(pacman -Q spirv-tools | cut -d \  -f 2 | sed 's/-.*//')\n"
"$(pacman -Q glslang-git | cut -d \  -f 2 | sed 's/-.*//')\n"
EOF
}

build() {
  mkdir -p build && cd build
  cmake ../shaderc-$pkgver \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX="$pkgdir"/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DSHADERC_SKIP_TESTS=on \
    -DPYTHON_EXE=/usr/bin/python2 \
    -GNinja \
    -DSHADERC_ENABLE_NV_EXTENSIONS=OFF # Currently requires glslang-git
  ninja

  cd ../shaderc-$pkgver/glslc
  asciidoctor -b manpage README.asciidoc -o glslc.1
}

package() {
  cd build
  ninja install
  install -Dm644 -t "$pkgdir"/usr/share/man/man1/ ../shaderc-$pkgver/glslc/glslc.1
}
