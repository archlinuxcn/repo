# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=spirv-cross
pkgver=1.4.304.1
pkgrel=1
epoch=1
_glslang_commit=142052fa30f9eca191aa9dcf65359fcaed09eeec
_spirv_tools_commit=fd96922e9a1814d92df46df03277788c799a4fad
_spirv_headers_commit=ea77f2a826bc820cb8f57f9b2a7c7eccb681c73
pkgdesc='A tool and library for parsing and converting SPIR-V to other shader languages'
arch=('x86_64')
url='https://github.com/KhronosGroup/SPIRV-Cross/'
license=('Apache-2.0')
depends=('gcc-libs')
makedepends=('git' 'cmake' 'python')
source=("git+https://github.com/KhronosGroup/SPIRV-Cross.git#tag=vulkan-sdk-${pkgver}"
        "git+https://github.com/KhronosGroup/glslang.git#commit=${_glslang_commit}"
        "git+https://github.com/KhronosGroup/SPIRV-Tools.git#commit=${_spirv_tools_commit}"
        "git+https://github.com/KhronosGroup/SPIRV-Headers.git#commit=${_spirv_headers_commit}")
sha256sums=('8371ce34474e37e06221ed70a949db5df4616c36da73b090643546103114445a'
            'be4a2494f139c3e04024d3bc5313a37a23ef901fb4d4dffa3a2ff9a5f2324709'
            '38b55d2abc1f351325640e891b862186114e7698204fcf5d693c9264b8239e64'
            '5e46d98e2c53326f11e34a225ddbf8bf17438ba5cf4b046b52fb5f650ec5c532')

prepare() {
    mkdir -p SPIRV-Cross/external/{glslang,spirv-tools}
    
    ln -sf "${srcdir}/glslang"       SPIRV-Cross/external/glslang
    ln -sf "${srcdir}/SPIRV-Tools"   SPIRV-Cross/external/spirv-tools
    ln -sf "${srcdir}/SPIRV-Headers" SPIRV-Tools/external/spirv-headers
}

build() {
    # NOTE: test suite fails when using 'None' build type
    local -a _common_opts=('-GUnix Makefiles' '-DCMAKE_BUILD_TYPE:STRING=Release' '-Wno-dev')
    
    export CFLAGS+=' -ffat-lto-objects'
    export CXXFLAGS+=' -ffat-lto-objects'
    
    # glslang (required for tests)
    cmake -B SPIRV-Cross/external/glslang-build -S glslang \
        "${_common_opts[@]}" \
        -DCMAKE_INSTALL_PREFIX:PATH='output' \
        -DENABLE_OPT:BOOL='OFF'
    cmake --build SPIRV-Cross/external/glslang-build --target install
    
    # spirv-tools (required for tests)
    cmake -B SPIRV-Cross/external/spirv-tools-build -S SPIRV-Tools \
        "${_common_opts[@]}" \
        -DCMAKE_INSTALL_PREFIX:PATH='output' \
        -DSPIRV_WERROR:BOOL='OFF'
    cmake --build SPIRV-Cross/external/spirv-tools-build --target install
    
    # spirv-cross
    cmake -B build-SPIRV-Cross -S SPIRV-Cross \
        "${_common_opts[@]}" \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -DSPIRV_CROSS_FORCE_PIC:BOOL='ON' \
        -DSPIRV_CROSS_SHARED:BOOL='ON'
    cmake --build build-SPIRV-Cross
}

check() {
    ctest --test-dir build-SPIRV-Cross --output-on-failure
}

package() {
    DESTDIR="$pkgdir" cmake --install build-SPIRV-Cross
}
