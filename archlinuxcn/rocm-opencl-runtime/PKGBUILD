# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-opencl-runtime
pkgver=5.3.3
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
sha256sums=('cab394e6ef16c35bab8de29a66b96a7dc0e7d1297aaacba3718fa1d369233c9f'
            'f8133a5934f9c53b253d324876d74f08a19e2f5b073bc94a62fe64b0d2183a18')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"
_rocclr_dir="$(basename "$_rocclr")-$(basename "${source[1]}" .tar.gz)"

build() {
    cmake \
        -Wno-dev \
        -B build-rocclr \
	    -S "$_rocclr_dir" \
        -DAMD_OPENCL_PATH="$srcdir/$_dirname"
    cmake --build build-rocclr

    # Tests do not compile with strict format security
    CXXFLAGS=${CXXFLAGS//-Werror=format-security/}
    cmake \
        -Wno-dev \
        -B build \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DROCM_PATH=/opt/rocm \
        -DBUILD_TESTS=ON \
        -DCMAKE_PREFIX_PATH="$srcdir/$_rocclr_dir;/opt/rocm" \
        -DAMD_OPENCL_PATH="$srcdir/$_dirname"
    cmake --build build
}

check() {
    # Two test targets are defined: runtime and performance.
    # Performance tests freeze video output thus we're not calling them here.
    cmake --build build --target test.ocltst.oclruntime
}

package() {
    DESTDIR="$pkgdir" cmake --install build

    install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    echo '/opt/rocm/lib' > "$pkgname.conf"
    install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"

    echo '/opt/rocm/lib/libamdocl64.so' > 'amdocl64.icd'
    install -Dm644 'amdocl64.icd' "$pkgdir/etc/OpenCL/vendors/amdocl64.icd"
}
