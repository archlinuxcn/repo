# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
pkgname=rocclr
pkgver=4.3.0
pkgrel=1
pkgdesc='Radeon Open Compute Common Language Runtime'
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCclr'
license=('MIT')
depends=('mesa' 'comgr' 'hsa-rocr' 'hsakmt-roct' 'rocm-cmake')
makedepends=('cmake')
_opencl='https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime'
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "$pkgname-opencl-$pkgver.tar.gz::$_opencl/archive/rocm-$pkgver.tar.gz")
sha256sums=('8a86b4f2a1b1c7ac628262e5b11b07ff42a224e62e594a4e0683aeb616062538'
            'd37bddcc6835b6c0fecdf4d02c204ac1d312076f3eef2b1faded1c4c1bc651e9')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake -Wno-dev -B build \
	-S "$srcdir/$_dirname" \
	-DCMAKE_INSTALL_PREFIX='/opt/rocm' \
    -DOPENCL_DIR="$srcdir/ROCm-OpenCL-Runtime-rocm-$pkgver"

    make -C build
}

package() {
    DESTDIR="$pkgdir" make -C build install
    sed -i "s@$srcdir/build@/opt/rocm@" "$pkgdir/opt/rocm/lib/cmake/rocclr/ROCclrConfig.cmake"
    install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
