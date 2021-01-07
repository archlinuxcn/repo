# Maintainer Torsten Keßler <t dot kessler at posteo dot de>
pkgname=rocclr
pkgver=4.0.0
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
sha256sums=('8db502d0f607834e3b882f939d33e8abe2f9b55ddafaf1b0c2cd29a0425ed76a'
            'd43ea5898c6b9e730b5efabe8367cc136a9260afeac5d0fe85b481d625dd7df1')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake -Wno-dev -B build \
	-S "$srcdir/$_dirname" \
	-DCMAKE_INSTALL_PREFIX='/opt/rocm/rocclr' \
        -DOPENCL_DIR="$srcdir/ROCm-OpenCL-Runtime-rocm-$pkgver"

    make -C build
}

package() {
    DESTDIR="$pkgdir" make -C build install
    sed -i "s@$srcdir/build@/opt/rocm/rocclr@" "$pkgdir/opt/rocm/rocclr/lib/cmake/rocclr/ROCclrConfig.cmake"
    install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
