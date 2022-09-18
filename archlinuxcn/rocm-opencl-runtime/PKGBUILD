# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-opencl-runtime
pkgver=5.2.3
pkgrel=3
pkgdesc='OpenCL implementation for AMD'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime'
license=('MIT')
depends=('hsakmt-roct' 'hsa-rocr' 'comgr' 'mesa' 'opencl-icd-loader')
makedepends=('cmake' 'rocm-cmake')
provides=('opencl-driver')
_rocclr='https://github.com/ROCm-Developer-Tools/ROCclr'
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "$pkgname-rocclr-$pkgver.tar.gz::$_rocclr/archive/rocm-$pkgver.tar.gz")
sha256sums=('932ea3cd268410010c0830d977a30ef9c14b8c37617d3572a062b5d4595e2b94'
            '0493c414d4db1af8e1eb30a651d9512044644244488ebb13478c2138a7612998')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"
_rocclr_dir="$(basename "$_rocclr")-$(basename "${source[1]}" .tar.gz)"

build() {
    cmake \
        -Wno-dev \
        -B build-rocclr \
	    -S "$_rocclr_dir" \
        -DAMD_OPENCL_PATH="$srcdir/$_dirname"
    cmake --build build-rocclr

    cmake \
        -Wno-dev \
        -B build \
        -S "$_dirname" \
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
