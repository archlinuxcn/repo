# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-opencl-runtime
pkgver=4.5.0
pkgrel=1
pkgdesc='Radeon Open Compute - OpenCL runtime'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime'
license=('MIT')
depends=('hsakmt-roct' 'hsa-rocr' 'comgr' 'mesa' 'opencl-icd-loader')
makedepends=('cmake' 'rocm-cmake')
provides=('opencl-driver')
conflicts=('opencl-amdgpu-pro-pal')
_rocclr='https://github.com/ROCm-Developer-Tools/ROCclr'
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "$pkgname-rocclr-$pkgver.tar.gz::$_rocclr/archive/rocm-$pkgver.tar.gz")
sha256sums=('3a163aed24619b3faf5e8ba17325bdcedd1667a904ea20914ac6bdd33fcdbca8'
            'ca8d6305ff0e620d9cb69ff7ac3898917db9e9b6996a7320244b48ab6511dd8e')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"
_rocclr_dir="$(basename "$_rocclr")-$(basename "${source[1]}" .tar.gz)"

build() {
    cmake -Wno-dev -B build-rocclr \
	-S "$_rocclr_dir" \
    -DAMD_OPENCL_PATH="$srcdir/$_dirname"

    make -C build-rocclr

    cmake -Wno-dev -B build \
    -S "$_dirname" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DUSE_COMGR_LIBRARY=yes \
    -DROCCLR_PATH="$srcdir/$_rocclr_dir" \
    -DAMD_OPENCL_PATH="$srcdir/$_dirname"

    make -C build
}

package() {
    DESTDIR="$pkgdir" make -C build install
    install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/$pkgname.conf" <<-EOF
      /opt/rocm/lib
EOF
    install -Dm644 /dev/stdin "$pkgdir/etc/OpenCL/vendors/amdocl64.icd" <<EOF
/opt/rocm/lib/libamdocl64.so
EOF
}
