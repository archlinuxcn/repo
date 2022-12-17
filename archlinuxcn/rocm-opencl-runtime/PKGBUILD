# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-opencl-runtime
pkgver=5.4.1
pkgrel=1
pkgdesc='OpenCL implementation for AMD'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime'
license=('MIT')
depends=('hsakmt-roct' 'hsa-rocr' 'comgr' 'mesa' 'opencl-icd-loader')
makedepends=('rocm-cmake')
provides=('opencl-driver')
_rocclr='https://github.com/ROCm-Developer-Tools/ROCclr'
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "$pkgname-rocclr-$pkgver.tar.gz::$_rocclr/archive/rocm-$pkgver.tar.gz")
sha256sums=('2b3d7b365f569ce64d1408d6e745d005aa10eca3623891be50f6b1b2e802d875'
            'c0926fa5dad71cd02f21504d82e218d482779df579a400604e13864e6b2a7d9c')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"
_rocclr_dir="$(basename "$_rocclr")-$(basename "${source[1]}" .tar.gz)"

build() {
    cmake \
        -Wno-dev \
        -B build-rocclr \
        -S "$_rocclr_dir" \
        -DCMAKE_BUILD_TYPE=None \
        -DAMD_OPENCL_PATH="$srcdir/$_dirname"
    cmake --build build-rocclr

    cmake \
        -Wno-dev \
        -B build \
        -S "$_dirname" \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DROCM_PATH=/opt/rocm \
        -DCMAKE_PREFIX_PATH="$srcdir/$_rocclr_dir;/opt/rocm" \
        -DAMD_OPENCL_PATH="$srcdir/$_dirname"
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build

    install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    echo '/opt/rocm/lib' > "$pkgname.conf"
    install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"

    echo '/opt/rocm/lib/libamdocl64.so' > 'amdocl64.icd'
    install -Dm644 'amdocl64.icd' "$pkgdir/etc/OpenCL/vendors/amdocl64.icd"
}
