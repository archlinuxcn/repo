# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-opencl-runtime
pkgver=5.2.1
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
        "$pkgname-rocclr-$pkgver.tar.gz::$_rocclr/archive/rocm-$pkgver.tar.gz"
        "enable-gfx800.patch")
sha256sums=('eb4ff433f8894ca659802f81792646034f8088b47aca6ad999292bcb8d6381d5'
            '465ca9fa16869cd89dab8c2d66d9b9e3c14f744bbedaa1d215b0746d77a500ba'
            'b186dd4a604d6e8a2c94ba6569638aaa8066558d764aa0d9cf76f998724ed90a')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"
_rocclr_dir="$(basename "$_rocclr")-$(basename "${source[1]}" .tar.gz)"

prepare() {
	#From xuhuisheng
	#at https://github.com/RadeonOpenCompute/ROCm/issues/1659#issuecomment-1041026624
	cd "$_rocclr_dir"
	patch -p1 -i "$srcdir/enable-gfx800.patch"
}

build() {
    cmake -Wno-dev -B build-rocclr \
	-S "$_rocclr_dir" \
    -DCMAKE_BUILD_TYPE=Release \
    -DAMD_OPENCL_PATH="$srcdir/$_dirname"

    make -C build-rocclr

    cmake -Wno-dev -B build \
    -S "$_dirname" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_BUILD_TYPE=Release \
    -DROCM_PATH=/opt/rocm \
    -DCMAKE_PREFIX_PATH="$srcdir/$_rocclr_dir;/opt/rocm" \
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
