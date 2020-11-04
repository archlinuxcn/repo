# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>

_pkgbasename=vmaf
pkgname=("lib32-$_pkgbasename" "lib32-lib$_pkgbasename")
pkgver=1.5.2
pkgrel=1
pkgdesc='Perceptual video quality assessment algorithm based on multi-method fusion (32 bit)'
arch=('x86_64')
url='https://github.com/Netflix/vmaf/'
license=('BSD')
depends=(
        "$_pkgbasename"
        'lib32-gcc-libs'
    )
makedepends=(
        'meson'
#        'meson-cross-x86-linux-gnu>=1.0.4'
        'ninja'
    )
source=("${_pkgbasename}-${pkgver}.tar.gz"::"https://github.com/Netflix/${_pkgbasename}/archive/v${pkgver}.tar.gz")
sha256sums=('5f7785da0b0d66b2513ce11d3f81d0a9b3f79d49483c4652fde3a31c13f644da')

prepare() {
    mkdir -p "${_pkgbasename}-${pkgver}/libvmaf/build"
}

build() {
    export CC="gcc -m32"
    export CXX="g++ -m32"
    export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"   

    cd "${_pkgbasename}-${pkgver}/libvmaf"
    meson  build \
        --prefix=/usr \
        --libdir=lib32 \
        -D enable_tests=false \
        -D enable_docs=false

    ninja -v -C build
}

# check() {
#     ninja -v -C "${_pkgbasename}-${pkgver}/libvmaf/build" test
# }

package_lib32-libvmaf() {
    pkgdesc='Perceptual video quality assessment algorithm based on multi-method fusion - library (32 bit)'
    depends=(
      "$_pkgbasename"
      "lib32-gcc-libs"
    )
    provides=("lib32-vmaf")

    cd ${_pkgbasename}-${pkgver}/libvmaf

    DESTDIR="$pkgdir" ninja -v -C "build" install
    
    rm -r "$pkgdir"/usr/{include,share,bin}

#    install -D -m644 "${_pkgbasename}-${pkgver}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_lib32-vmaf() {
    pkgdesc='Perceptual video quality assessment algorithm based on multi-method fusion (32 bit)'
    depends=(
      "$_pkgbasename"
      "lib32-gcc-libs"
      "lib32-libvmaf"
    )

    DESTDIR="$pkgdir" ninja -v -C "${_pkgbasename}-${pkgver}/libvmaf/build" install
    
    install -D -m755 "${_pkgbasename}-${pkgver}/libvmaf/build/tools"/vmaf_{feature,rc} -t "${pkgdir}/usr/bin"

    # Use the same naming scheme as the one in the lib32-shaderc-git package for coherence
    # Arch wiki suggest to use the "-32" suffix for 32 bit executables: https://wiki.archlinux.org/index.php/32-bit_package_guidelines
    for i in "${pkgdir}/usr/bin/"*; do
        mv "$i" "$i"-32
    done

    rm -r "$pkgdir"/usr/{include,share,lib32}

#    install -D -m644 "${_pkgbasename}-${pkgver}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
