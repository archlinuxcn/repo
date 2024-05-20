# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Daniel M. Capella <polycitizen@gmail.com>
# Contributor: Bin Jin <bjin@ctrl-d.org>

pkgname=shaderc-non-semantic-debug
pkgver=2024.0
pkgrel=1
pkgdesc='Collection of tools, libraries and tests for shader compilation'
url='https://github.com/google/shaderc'
arch=('x86_64')
license=('Apache-2.0')
depends=('glibc' 'gcc-libs' 'glslang' 'spirv-tools')
makedepends=('asciidoctor' 'cmake' 'ninja' 'python' 'spirv-headers')
provides=('libshaderc_shared.so' 'shaderc')
source=(
    https://github.com/google/shaderc/archive/v${pkgver}/shaderc-${pkgver}.tar.gz
shaderc-changes.patch)
sha512sums=('ca80b22a80bf1a222e6deecbe63f99c6eed980c6c31b4f7981b6c8dc5637b7271c861543566e01aaf945df40da095b63a69f2e22f061a41faad2ecca5dc187ae')
b2sums=('f11f2acad796f41015d4738b964526f119e944b1cfa2103ab3452adcf5790a04adbd10f9d55423b3ce567e87f64eb241067c786c4a7b76bb884aa70c100d0eb8')
conflicts=(shaderc)

prepare() {
    cd shaderc-${pkgver}
    patch -p1 < "../shaderc-changes.patch"
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
    cd shaderc-${pkgver}
    cmake \
    -B build \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS -ffat-lto-objects" \
    -DSHADERC_SKIP_TESTS=ON \
    -DPYTHON_EXECUTABLE=python \
    -Dglslang_SOURCE_DIR=/usr/include/glslang
    ninja -C build
    
    cd glslc
    asciidoctor -b manpage README.asciidoc -o glslc.1
}

check() {
    cd shaderc-${pkgver}
    ninja -C build test
}

package() {
    cd shaderc-${pkgver}
    DESTDIR="${pkgdir}" ninja -C build install
    install -Dm 644 glslc/glslc.1 -t "${pkgdir}/usr/share/man/man1"
    
    # Remove unused shaderc_static.pc
    #rm "${pkgdir}/usr/lib/pkgconfig/shaderc_static.pc"
}

# vim: ts=2 sw=2 et:
sha512sums=('ca80b22a80bf1a222e6deecbe63f99c6eed980c6c31b4f7981b6c8dc5637b7271c861543566e01aaf945df40da095b63a69f2e22f061a41faad2ecca5dc187ae'
'c18a24bbadc4cb1a26d6aa53861de248156d6f2068f18b887091440d3e2e268c2cf8dbee6ccd791edc1c8071662e1a67fc526ad74613fa1f071d1df927c23959')
b2sums=('f11f2acad796f41015d4738b964526f119e944b1cfa2103ab3452adcf5790a04adbd10f9d55423b3ce567e87f64eb241067c786c4a7b76bb884aa70c100d0eb8'
'93480c91f2e3fa20f29f60034676b1741f8ed2a0754c38127505506852378979c2020b69904e4913a6f204a022ccef9074b7bc192e3f5c85ecf77a498c4c5fef')
sha512sums=('ca80b22a80bf1a222e6deecbe63f99c6eed980c6c31b4f7981b6c8dc5637b7271c861543566e01aaf945df40da095b63a69f2e22f061a41faad2ecca5dc187ae'
'c18a24bbadc4cb1a26d6aa53861de248156d6f2068f18b887091440d3e2e268c2cf8dbee6ccd791edc1c8071662e1a67fc526ad74613fa1f071d1df927c23959')
b2sums=('f11f2acad796f41015d4738b964526f119e944b1cfa2103ab3452adcf5790a04adbd10f9d55423b3ce567e87f64eb241067c786c4a7b76bb884aa70c100d0eb8'
'93480c91f2e3fa20f29f60034676b1741f8ed2a0754c38127505506852378979c2020b69904e4913a6f204a022ccef9074b7bc192e3f5c85ecf77a498c4c5fef')
