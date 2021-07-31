# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgbase=libjxl
pkgname=('libjxl' 'libjxl-doc')
pkgver=0.3.7
pkgrel=4
pkgdesc='JPEG XL image format reference implementation'
arch=('x86_64')
url='https://jpeg.org/jpegxl/'
#license=('BSD') # license will change on the next release
license=('Apache')
makedepends=('git' 'cmake' 'clang' 'brotli' 'gdk-pixbuf2' 'giflib' 'gimp'
             'gperftools' 'libjpeg-turbo' 'libpng' 'openexr' 'zlib' 'libgl'
             'freeglut' 'gtest' 'gmock' 'python' 'asciidoc' 'doxygen'
             'graphviz')
source=("git+https://github.com/libjxl/libjxl.git#tag=v${pkgver}"
        'git+https://github.com/google/brotli.git'
        'git+https://github.com/lvandeve/lodepng.git'
        'git+https://github.com/mm2/Little-CMS.git'
        'git+https://github.com/google/googletest.git'
        'git+https://github.com/webmproject/sjpeg.git'
        'git+https://skia.googlesource.com/skcms.git'
        'git+https://github.com/veluca93/IQA-optimization.git'
        'git+https://github.com/Netflix/vmaf.git'
        'git+https://github.com/thorfdbg/difftest_ng.git'
        'git+https://github.com/google/highway.git'
        '010-libjxl-openexr-fix.patch')
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '55e6c00fa8293d5cdcf205c88f21764bb89a2c8d2d252d059ec68091e3ee57ee')

prepare() {
    git -C libjxl submodule init
    git -C libjxl config --local submodule.third_party/brotli.url "${srcdir}/brotli"
    git -C libjxl config --local submodule.third_party/lodepng.url "${srcdir}/lodepng"
    git -C libjxl config --local submodule.third_party/lcms.url "${srcdir}/Little-CMS"
    git -C libjxl config --local submodule.third_party/googletest.url "${srcdir}/googletest"
    git -C libjxl config --local submodule.third_party/sjpeg.url "${srcdir}/sjpeg"
    git -C libjxl config --local submodule.third_party/skcms.url "${srcdir}/skcms"
    git -C libjxl config --local submodule.third_party/IQA-optimization.url "${srcdir}/IQA-optimization"
    git -C libjxl config --local submodule.third_party/vmaf.url "${srcdir}/vmaf"
    git -C libjxl config --local submodule.third_party/difftest_ng.url "${srcdir}/difftest_ng"
    git -C libjxl config --local submodule.third_party/highway.url "${srcdir}/highway"
    git -C libjxl submodule update
    
    # https://gitlab.com/wg1/jpeg-xl/-/issues/162
    # https://gitlab.com/wg1/jpeg-xl/-/issues/238
    # https://github.com/libjxl/libjxl/commit/9a8f5195e4d1c45112fd65f184ebe115f4163ba2#diff-5302e2eb1ae00d323a83e482b68cbcc96bd3d717f3414663a5fffd29428808b3
    patch -d libjxl -Np1 -i "${srcdir}/010-libjxl-openexr-fix.patch"
}

build() {
    # https://github.com/libjxl/libjxl/issues/98
    export CXXFLAGS="${CXXFLAGS/ -Wp,-D_GLIBCXX_ASSERTIONS/}"
    
    export CC='clang'
    export CXX='clang++'
    cmake -B build -S libjxl \
        -DCMAKE_BUILD_TYPE:STRING='None' \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -DJPEGXL_ENABLE_BENCHMARK:BOOL='false' \
        -DJPEGXL_ENABLE_FUZZERS:BOOL='false' \
        -DJPEGXL_ENABLE_PLUGINS:BOOL='true' \
        -DJPEGXL_ENABLE_VIEWERS:BOOL='false' \
        -DJPEGXL_ENABLE_GIMP_SAVING:BOOL='ON' \
        -DJPEGXL_FORCE_SYSTEM_BROTLI:BOOL='true' \
        -DJPEGXL_FORCE_SYSTEM_GTEST:BOOL='true' \
        -DJPEGXL_FORCE_SYSTEM_HWY:BOOL='false' \
        -DJPEGXL_WARNINGS_AS_ERRORS:BOOL='false' \
        -Wno-dev
    make -C build all doc
}

check() {
    make -C build test
}

package_libjxl() {
    depends=('brotli')
    optdepends=('gdk-pixbuf2: for gdk-pixbuf loader'
                'giflib: for CLI tools'
                'gimp: for gimp plugin'
                'gperftools: for CLI tools and gimp plugin'
                'libjpeg-turbo: for CLI tools'
                'libpng: for CLI tools'
                'openexr: for CLI tools')
    provides=('libjpeg-xl' 'libjxl.so' 'libjxl_threads.so')
    conflicts=('libjpeg-xl')
    replaces=('libjpeg-xl')
    
    make -C build DESTDIR="$pkgdir" install
    rm -r "${pkgdir}/usr"/{include/{contrib,hwy},lib/{pkgconfig/,}libhwy*}
}

package_libjxl-doc() {
    pkgdesc+=' (documentation)'
    arch=('any')
    provides=('libjpeg-xl-doc')
    conflicts=('libjpeg-xl-doc')
    replaces=('libjpeg-xl-doc')
    
    install -d -m755 "${pkgdir}/usr/share/doc"
    cp -dr --no-preserve='ownership' build/html "${pkgdir}/usr/share/doc/libjxl"
}
