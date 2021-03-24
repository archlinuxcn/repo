# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
pkgname=rocclr
pkgver=4.1.0
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
sha256sums=('9eb1d88cfc9474979aaf29b99bcf9d3769a0f7f1f8f10660941aabf83d9eeb0c'
            '0729e6c2adf1e3cf649dc6e679f9cb936f4f423f4954ad9852857c0a53ef799c')
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
