# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=spirv-cross
pkgver=1.3.283.0
pkgrel=1
epoch=1
_glslang_commit=a7785ea1ff5b10bfc2d8ca77fdad5929562897b7
_spirv_tools_commit=afaf8fda2ad0364655909b56c8b634ce89095bb5
_spirv_headers_commit=e867c06631767a2d96424cbec530f9ee5e78180f
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
sha256sums=('9c2a148a1e4c7ca16ab54991980ed6393c1c21794081083f2779d880b3dbf1d4'
            'e057bbfcfef5392f7af0fcf034e01b62eb40f66cc3202bb4717e61199a8ce96d'
            'e1fca43e16eb9b9ea4f1914ab572ca0f66910b96bd8b1069d48dd1e7cdf30352'
            '7eab7bb5368f2f841812a5ce10400d5f3301c7ae700512997f2462909b10aeac')

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
