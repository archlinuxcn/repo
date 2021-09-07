# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
pkgname=rocclr
pkgver=4.3.1
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
sha256sums=('bda52c65f03a69a9d8ab1a118d45646d76843249fb975d67e5141e63fa3acc79'
            '7f98f7d4707b4392f8aa7017aaca9e27cb20263428a1a81fb7ec7c552e60c4ca')
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
