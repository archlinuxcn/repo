# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgbase=libjxl
pkgname=('libjxl' 'libjxl-doc')
pkgver=0.5
pkgrel=4
pkgdesc='JPEG XL image format reference implementation'
arch=('x86_64')
url='https://jpeg.org/jpegxl/'
license=('BSD')
makedepends=('git' 'cmake' 'clang' 'brotli' 'gdk-pixbuf2' 'giflib' 'gimp'
             'gperftools' 'libjpeg-turbo' 'libpng' 'openexr' 'zlib' 'libgl'
             'freeglut' 'gtest' 'gmock' 'python' 'asciidoc' 'doxygen'
             'graphviz' 'java-environment' 'highway')
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
        '010-libjxl-jdk7-fix.patch'::'https://github.com/libjxl/libjxl/commit/76df97ea2d7e91ceecc778d7c098dc376209ee73.patch')
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
            '40e22d47f073b8ccc9382451449360e01afed96ce5d80c89ff82ae8babb96303')

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
    
    # https://github.com/libjxl/libjxl/issues/396
    patch -d libjxl -Np1 -i "${srcdir}/010-libjxl-jdk7-fix.patch"
}

build() {
    export CC='clang'
    export CXX='clang++'
    export CFLAGS+=' -DNDEBUG'
    export CXXFLAGS+=' -DNDEBUG'
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
        -DJPEGXL_FORCE_SYSTEM_HWY:BOOL='true' \
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
                'java-runtime: for JNI bindings'
                'libjpeg-turbo: for CLI tools'
                'libpng: for CLI tools'
                'openexr: for CLI tools')
    provides=('libjpeg-xl' 'libjxl.so' 'libjxl_jni.so' 'libjxl_threads.so')
    conflicts=('libjpeg-xl')
    replaces=('libjpeg-xl')
    
    make -C build DESTDIR="$pkgdir" install
    install -D -m755 build/tools/libjxl_jni.so -t "${pkgdir}/usr/lib"
    install -D -m644 libjxl/{LICENSE,PATENTS} -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_libjxl-doc() {
    pkgdesc+=' (documentation)'
    arch=('any')
    provides=('libjpeg-xl-doc')
    conflicts=('libjpeg-xl-doc')
    replaces=('libjpeg-xl-doc')
    
    install -d -m755 "${pkgdir}/usr/share/doc"
    install -D -m644 libjxl/{LICENSE,PATENTS} -t "${pkgdir}/usr/share/licenses/${pkgname}"
    cp -dr --no-preserve='ownership' build/html "${pkgdir}/usr/share/doc/libjxl"
}
