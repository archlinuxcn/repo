# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-opencl-runtime
pkgver=4.3.1
pkgrel=1
pkgdesc='Radeon Open Compute - OpenCL runtime'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime'
license=('MIT')
depends=('hsakmt-roct' 'hsa-rocr' 'rocclr' 'opencl-icd-loader')
makedepends=('cmake' 'rocm-cmake')
provides=('opencl-driver')
conflicts=('opencl-amdgpu-pro-pal')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('7f98f7d4707b4392f8aa7017aaca9e27cb20263428a1a81fb7ec7c552e60c4ca')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    CFLAGS="$CFLAGS -isystem /opt/rocm/include/compiler/lib -isystem /opt/rocm/include/compiler/lib/include -isystem /opt/rocm/include/elf" \
    CXXFLAGS="$CXXFLAGS -isystem /opt/rocm/include/compiler/lib -isystem /opt/rocm/include/compiler/lib/include -isystem /opt/rocm/include/elf" \
    cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
          -DUSE_COMGR_LIBRARY=yes \
          -DBUILD_TESTING=OFF \
          "$_dirname"
    make
}

package() {
    DESTDIR="$pkgdir" make install
    install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/$pkgname.conf" <<-EOF
      /opt/rocm/lib
EOF
    install -Dm644 /dev/stdin "$pkgdir/etc/OpenCL/vendors/amdocl64.icd" <<EOF
/opt/rocm/lib/libamdocl64.so
EOF
}
